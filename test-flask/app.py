from flask import Flask, jsonify
from db import create_tech_db, get_tech_db


web_app = Flask('web_app')


@web_app.route('/tech/<string:nome>')
def get_tech(nome):
    return jsonify('ok'), 200


@web_app.route('/tech' , methods=['POST'])
def create_tech():
    return jsonify('ok'), 201


if __name__=='__main__':
    web_app.run()