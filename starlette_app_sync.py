from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route


def homepage(request):
    return PlainTextResponse('Hello, world!')


app = Starlette(debug=True, routes=[
    Route('/', homepage),
])
