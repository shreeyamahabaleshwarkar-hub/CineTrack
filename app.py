from flask import Flask, render_template, request

app = Flask(__name__)

movies = []


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
            rating_value = float(rating)

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
        error=error
    )


@app.route("/health")
def health():
    return {"status": "ok"}


@app.route("/api/movies")
def get_movies():
    return movies


if __name__ == "__main__":
    app.run(debug=True)
