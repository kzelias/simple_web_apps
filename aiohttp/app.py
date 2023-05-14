from aiohttp import web


def health(request):
    return web.json_response({"status": "ok"}, status=200)


app = web.Application()
app.router.add_route("GET", "/", health)

if __name__ == "__main__":
    web.run_app(app, host="0.0.0.0", port=8000)
