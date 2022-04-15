import os
from flask import Flask, jsonify, request
import json



def made_menu (list,channel, text):

    if channel == 'whatsapp':   

            body = {}
            list_option = []
        
            header = "application/json"

            for position in list:

                title = position
                option = {
                                    "id": title,
                                    "title": title
                                }
                list_option.append(option)

            list_option = list_option[1:]
            body =  {
            "recipient_type": "individual",
            "type": "interactive",
            "interactive": {
                "type": "list",
                "body": {
                    "text": text
                },
                "action": {
                    "button": "Menu",
                    "sections": [
                        {
                            "title": "Menu",
                            "rows": [

                                list_option
                                
                            ]
                        }
                    ]
                }
            }
        }
            

    elif channel == 'blip'or channel == 'instagram' or channel == 'messenger' :

        count = 0
        header = "application/vnd.lime.select+json"
        body = {}
        list_option = []
        

        for position in list:

            title = position

            count = count + 1

            option = {
                    "order": count,
                    "text": title
                }
            list_option.append(option)

        body = {
            "text": text,
            "options": [

                list_option
                
            ]
        }
       

    else:

        header = "text/plain"

        count = 0

        body = ''
        list_option = ''

        for position in list:

            title = position

            count = count + 1

            couter = str(count)

            list_option = list_option + '\n' + couter + " " + title

        body = text + "\n\n" + list_option
    
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

            for position in list:

                title = position

                option = {
                            "type": "reply",
                            "reply": {
                                "id": title,
                                "title": title
                            }
                        }
                #list_option = list_option + option

                list_option.append(option)
            #list_option = list_option[1:]
            body = {"body":{
            "recipient_type": "individual",
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {
                    "text": text
                },
                "action": {
                    "buttons": [

                        list_option
                      
                    ]
                }
            }
         },"header" : header}
    
            

    elif channel == 'blip'or channel == 'instagram' or channel == 'messenger' :

        count = 0
        header = "application/vnd.lime.select+json"
        

        for position in list:

            title = position

            count = count + 1

            option = {
                    "order": count,
                    "text": title
                }
            list_option.append(option)

        body = {"body" :
        {
        "scope":"immediate",
        "text":text,
        "options":[
            list_option
        ]
    },
    "header" : header}
        

    else:
        print("else")
        header = "text/plain"
        body = ''
        list_option = ''

        count = 0

        for position in list:

            title = position

            count = count + 1

            couter = str(count)

            list_option = list_option + '\n' + couter + " " + title

        body = text + "\n\n" + list_option
        body = json.dumps({

        "body" : body,
        "header" : header

    })
    print(body)
    print('na função')
    
    return body

def made_text(list,channel, text):

    body = ''
    list_option = ''

    header = "text/plain"

    count = 0

    for position in list:

            title = position

            count = count + 1

            couter = str(count)

            list_option = list_option + '\n' + couter + " " + title

    body = text + "\n\n" + list_option
    
    body_blip = {

        "body" : body,
        "header" : header

    }

    return body_blip

app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():
    if request.headers.get('Authorization') == '42':
        return jsonify({"42": "a resposta para a vida, o universo e tudo mais"})
    return jsonify({"message": "Não entre em pânico!"})

@app.route('/made_body', methods=['POST'])

def made_body():

    from flask import request
    
    data = request.get_json()

    list = data['list']
    channel = data['channel']
    text = data['text']

    list = list.split('/')
 
   

    size = len(list)

    if size <= 3:

        body = made_quick_reply (list = list,channel = channel, text = text)

    if size <= 10 and size >3 :

        body = made_menu (list = list,channel = channel, text = text)

    

    if size > 10:

        body = made_text(list = list,channel = channel, text = text)

    return body


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)