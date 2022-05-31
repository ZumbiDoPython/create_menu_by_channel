import os
from flask import Flask, jsonify, request
import json
import whatsapp
import blipchat
import texts
import common

comment = "Por aqui está tudo bem"

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

    comment = "Por aqui está tudo bem"

    from flask import request
    
    data = request.get_json()


    list = data['list']
    channel = data['channel']
    text = data['text']
    description_list = data['description_list']

    channel = channel.lower()

    for position in list:

        size_menu = len(position)

        if size_menu > 20:

            if channel == "whatsapp":

                channel = "text"
                comment = "Você ultrapassou o limite de caracteres aceitos pelo WhatsApp, no titulo do botão ele aceita apenas 20 caracteres, sendo assim passamos seu menu para formato de texto"

    for position in description_list:

        size_menu = len(position)

        if size_menu > 72:

            if channel == "whatsapp":

                channel = "text"
                comment = "Você ultrapassou o limite de caracteres aceitos pelo WhatsApp, no sub titulo do botão ele aceita apenas 72 caracteres, sendo assim passamos seu menu para formato de texto"

    body = common.made_menu_description(list,channel, text, description_list, comment = comment)
    
    return body



@app.route('/create_dinamic_menu', methods=['POST'])

#{
#   "list":["Teste1","Teste2","Teste3","Teste4"],
#   "channel":"whatsapp",
#   "text":"Foi"
#}

def create_menu():

    comment = "Por aqui está tudo bem"

    

    from flask import request
    
    data = request.get_json()

    list = data['list']
    channel = data['channel']
    text = data['text']
    order = data['order']

    #list = list.split('/')
    #list = ['Comercial' ,'Financeiro' ,'Suporte' ]
    
    if order == None:

        order = True

    channel = channel.lower()

    size = len(list)

    for position in list:

        size_menu = len(position)

        if size_menu > 20:

            if channel == "whatsapp":

                channel = "text"

    

    if size <= 3:

        last_body = common.made_quick_reply (list = list,channel = channel, text = text, comment = comment, order = order)

    elif size <= 10 and size >3 :

        last_body = common.made_menu (list = list,channel = channel, text = text, comment = comment)

    

    else:

        comment = "Por padrão o WhatsApp tem como limite 3 opções para quick reply, e 10 para lista, sendo assim a API joga tudo que tiver mais que 10 opções para texto"

        last_body = common.made_text(list = list, text = text, comment = comment)

    return last_body


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)