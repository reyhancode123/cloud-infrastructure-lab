import json
import threading
from urllib.request import urlopen

import pytest

from docker.app.app import create_server


@pytest.fixture
def server():
    http_server = create_server(host="127.0.0.1", port=0)

    thread = threading.Thread(
        target=http_server.serve_forever,
        daemon=True
    )
    thread.start()

    host, port = http_server.server_address

    yield f"http://{host}:{port}"

    http_server.shutdown()
    http_server.server_close()
    thread.join()


def test_server_returns_http_200(server):
    with urlopen(server) as response:
        assert response.status == 200


def test_server_returns_json(server):
    with urlopen(server) as response:
        data = json.loads(response.read().decode("utf-8"))

        assert data["project"] == "Cloud Infrastructure Lab"
        assert data["service"] == "Python Backend"
        assert data["status"] == "healthy"
        assert data["message"] == "Backend is running successfully"
        assert data["hostname"]


def test_content_type_is_json(server):
    with urlopen(server) as response:
        assert response.headers["Content-Type"] == "application/json"
