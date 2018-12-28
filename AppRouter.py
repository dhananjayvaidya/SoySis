from app import flaskAppInstance
class AppRouter(flaskAppInstance):
    def homePage(self):
        return flaskAppInstance.send_static_file("index.html")