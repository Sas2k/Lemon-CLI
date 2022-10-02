from Lemon.components import Component
from Lemon.Server import server

Root = Component("App")
App = server.Server(None)

class Index(Component):
    name = "Index"
    def item(props: dict):
        return "<h1>Hello World!</h1>"

Root.add(Index)

@App.route("/")
def index(request, response):
    response.text = Root.render("<Index/>")

App.run()