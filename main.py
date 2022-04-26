import os
from flask import Flask, jsonify, request
import json
import whatsapp
import blipchat
import texts



def made_menu (list,channel, text):

    if channel == 'whatsapp': 

        header = "application/json"           
        body = whatsapp.made_menu(list = list, text = text)

    elif channel == 'blipchat'or channel == 'instagram' or channel == 'messenger' :

        header = "application/vnd.lime.select+json"
        body = blipchat.made_menu(list = list, text = text)

    else:

        header = "text/plain"
        body = texts.made_text(list = list, text = text)

    
    body_blip = json.dumps({

        "body" : body,
        "header" : header

    })

  


    return body_blip



def made_quick_reply (list,channel, text):

    body = {}
    list_option = []

    if channel == 'whatsapp':   
        
        header = "application/json"
        body = whatsapp.made_quick_reply(list = list, text = text)

    elif channel == 'blipchat'or channel == 'instagram' or channel == 'messenger' :

        header = "application/vnd.lime.select+json"
        body = blipchat.made_quick_reply(list = list, text = text)
        
    else:
      
        header = "text/plain"
        body = texts.made_text(list = list, text = text)

    body_blip = json.dumps({

        "body" : body,
        "header" : header

    })

    
    return body_blip

def made_text(list, text):

    header = "text/plain"
    body = texts.made_text(list = list, text = text)

    body_blip = json.dumps({

        "body" : body,
        "header" : header

    })
    return body_blip


app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():
    if request.headers.get('Authorization') == '42':
        return jsonify({"42": "a resposta para a vida, o universo e tudo mais"})
    return jsonify({"message": "Não entre em pânico!"})

@app.route('/create_dinamic_menu', methods=['POST'])

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

        body = made_quick_reply (list = list,channel = channel, text = text)

    elif size <= 10 and size >3 :

        body = made_menu (list = list,channel = channel, text = text)

    

    else:

        body = made_text(list = list, text = text)

    return body


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)