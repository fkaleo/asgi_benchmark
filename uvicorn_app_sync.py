import time


def app(scope, receive, send):
    assert scope['type'] == 'http'
    # time.sleep(1)

    send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain'],
        ],
    })
    send({
        'type': 'http.response.body',
        'body': b'Hello, world!',
    })
