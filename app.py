from flask import Flask, render_template, request,  redirect
import subprocess

app = Flask(__name__)

movies = []


def get_commit_id():
    try:
        commit_id = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"]
        ).decode().strip()
        return commit_id
    except Exception:
        return "local"


@app.route("/", methods=["GET", "POST"])
def home():
    error = None

    if request.method == "POST":
        movie_name = request.form["movie_name"].strip()
        genre = request.form["genre"].strip()
        rating = request.form["rating"]
        status = request.form["status"]

        if not movie_name or not genre:
            error = "Movie name and genre cannot be empty."

        elif not rating:
            error = "Rating is required."

        else:
            try:
                rating_value = float(rating)
            except ValueError:
                error = "Rating must be a number."
            else:
                if rating_value < 0 or rating_value > 5:
                    error = "Rating must be between 0 and 5."

                elif status not in ["Watched", "Not Watched"]:
                    error = "Invalid status."

                else:
                    movie = {
                        "name": movie_name,
                        "genre": genre,
                        "rating": rating,
                        "status": status
                    }

                    movies.append(movie)

    return render_template(
        "index.html",
        movies=movies,
        error=error,
        commit_id=get_commit_id()
    )


@app.route("/health")
def health():
    return {"status": "ok"}


@app.route("/api/movies")
def get_movies():
    return movies


@app.route("/clear", methods=["POST"])
def clear_movies():
    movies.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
