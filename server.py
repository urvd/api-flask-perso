from routes.app import App
from routes.objectif import objectifRoutes
from routes.personne import personRoutes

server = App
server.register_blueprint(personRoutes)
server.register_blueprint(objectifRoutes)

@server.route('/')
def main():
    return "-- hello the world !! --"
# TODO: Variabilisé les donnée en dure et creer des env var pour le url mongo
# TODO : impl les routes update et delete
# TODO : impl toutes les routes
# TODO: prevenir dans un try catch, un retours en cas d'exception

if __name__ == '__main__':
    server.run(debug=True)