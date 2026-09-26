from app import app


def test_home_page():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"CineTrack" in response.data


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json == {"status": "ok"}


def test_movies_api():
    client = app.test_client()

    response = client.get("/api/movies")

    assert response.status_code == 200
    assert response.is_json


def test_add_movie():
    client = app.test_client()

    response = client.post(
        "/",
        data={
            "movie_name": "Inception",
            "genre": "Sci-Fi",
            "rating": "4.5",
            "status": "Watched"
        }
    )

    assert response.status_code == 200
    assert b"Inception" in response.data
