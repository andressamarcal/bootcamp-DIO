from flask_restful import Resource


lista_habilidades = ['Python', 'Javascript', 'HTML', 'CSS']


class Habilidades(Resource):
    
    def get(self):
        return lista_habilidades