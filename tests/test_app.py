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
