# from flask import Flask, jsonify, request
# import json

# app = Flask(__name__)


# # @app.route('/<int:numero>', methods=['GET','POST'])
# # def ola(numero):
# #     return 'Olá Mundo. {}'.format(numero)

# # @app.route('/<int:id>')
# # def pessoa(id):
# #     return jsonify({'id':id,'nome':'Andressa'})

# # @app.route('/soma', methods=['POST', 'GET'])
# # def soma():
    
# #     if request.method == 'POST':
# #         dados = json.loads(request.data)
# #         total = sum(dados['valores'])
    
# #     elif request.method == 'GET':
# #         total = 1+1    
    
# #     return jsonify({'soma':total})



# if __name__=='__main__':
#     app.run(debug=True)