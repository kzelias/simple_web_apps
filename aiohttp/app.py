from aiohttp import web

def index(request):
    return web.json_response({'status': 'ok'}, status=200)


app = web.Application()
app.router.add_route('GET', '/', index)

if __name__ == "__main__":
    web.run_app(app)