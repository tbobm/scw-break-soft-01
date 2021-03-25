from webserver import app


def test_app():
    flask_app = app.create_app()  # type: flask.app.Flask
    assert flask_app is not None


def test_routes():
    flask_app = app.create_app()  # type: flask.app.Flask
    client = flask_app.test_client()
    data = {
        "name": "validate",
        "pomodoros": 3,
        "author": "bob",
    }
    res = client.post('/todos', json=data)
    assert res.status_code == 201

    data['id'] = 1
    todos = client.get('/todos')
    assert data in todos.json

    res = client.get('/todos/1')
    assert res.status_code == 200
    # TODO: Test bad cases (wrong types, missing fields, ...?)

