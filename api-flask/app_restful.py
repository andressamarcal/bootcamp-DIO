from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import json
from habilidades import Habilidades


app = Flask(__name__)
api = Api(app)


desenvolvedores = [
    {
        'id':0,
        'nome':'Andressa',
        'habilidades':['Python', 'Django']
    },
    
    {   
        'id':1,
        'nome':'Marçal',
        'habilidades':['Python','Flask']
    }
]


class Desenvolvedor(Resource):
    
    def get(self, id):
        try:
            response = desenvolvedores[id]
        
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe.' .format(id)
            response = {'status':'erro', 'mensagem':mensagem}
        
        except Exception:
            mensagem = 'Erro desconhecido. Procure o Administrador da API'
            response = {'status':'erro', 'mensagem':mensagem}
        
        return response

    def post(self, id):
        pass

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados
    
    def delete(self, id):
        desenvolvedores.pop(id)
        dados = json.loads(request.data)
        return jsonify(response = {'status':'sucesso!', 'mensagem':'Registro Excluido!'})


class ListaDesenvolvedores(Resource):
    
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])        


#rota
api.add_resource(Desenvolvedor, '/dev/<int:id>/') 
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')


if __name__ == '__main__':
    app.run(debug=True)