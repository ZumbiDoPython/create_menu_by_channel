import os
from flask import Flask, jsonify, request
import json
import whatsapp
import blipchat
import texts
import common



app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():
    if request.headers.get('Authorization') == '42':
        return jsonify({"42": "a resposta para a vida, o universo e tudo mais"})
    return jsonify({"message": "Não entre em pânico!"})

@app.route('/create_menu_with_description', methods=['POST'])

#{
#    "list":["Teste1","Teste2","Teste3","Teste4"],
#    "description_list" : ["Teste10","Teste20","Teste30","Teste40"],
#    "channel":"whatsapp",
#    "text":"Foi"
#}

def create_menu_with_description():

    from flask import request
    
    data = request.get_json()


    list = data['list']
    channel = data['channel']
    text = data['text']
    description_list = data['description_list']

    body = common.made_menu_description(list,channel, text, description_list)
    
    return body



@app.route('/create_dinamic_menu', methods=['POST'])

#{
#   "list":["Teste1","Teste2","Teste3","Teste4"],
#   "channel":"whatsapp",
#   "text":"Foi"
#}

def create_menu():

    from flask import request
    
    data = request.get_json()

    list = data['list']
    channel = data['channel']
    text = data['text']

    #list = list.split('/')
    #list = ['Comercial' ,'Financeiro' ,'Suporte' ]
   

    size = len(list)

    if size <= 3:

        last_body = common.made_quick_reply (list = list,channel = channel, text = text)

    elif size <= 10 and size >3 :

        last_body = common.made_menu (list = list,channel = channel, text = text)

    

    else:

        last_body = common.made_text(list = list, text = text)

    return last_body


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)