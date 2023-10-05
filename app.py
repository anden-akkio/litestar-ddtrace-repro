from litestar import Litestar, get

@get(path="/health", status_code=200)
def _controller_health() -> None:
    pass

app = Litestar(route_handlers=[_controller_health])