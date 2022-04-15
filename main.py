import json
import uuid
import email
import imaplib
import qrcode
import os
import re
from flask import Flask
from flask import jsonify
from datetime import datetime
from urllib import request, parse
from urllib.error import URLError, HTTPError
from datetime import datetime
from email.message import EmailMessage

def made_menu (list,channel, text):

    if channel == 'whatsapp':   

            body = ''
            list_option = ''
        
            header = "application/json"

            for position in list:

                title = position
                option = json.dumps( {
                                    "id": title,
                                    "title": title
                                })
                list_option = list_option +','+ option

            list_option = list_option[1:]
            body = json.dumps( {
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
        })
            body = body.replace('\\','')

    elif channel == 'blip'or channel == 'instagram' or channel == 'messenger' :

        count = 0
        header = "application/vnd.lime.select+json"
        

        for position in list:

            title = position

            count = count + 1

            option = json.dumps({
                    "order": count,
                    "text": title
                })
            list_option = list_option +','+ option

        body = json.dumps({
            "text": text,
            "options": [

                list_option
                
            ]
        })
        body = body.replace('\\','')

    else:

        header = "text/plain"

        count = 0

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

    if channel == "whatsapp" or channel == "blip":

        body_blip = body_blip.replace('\\','')


    return body_blip



def made_quick_reply (list,channel, text):

    body = ''
    list_option = ''

    if channel == 'whatsapp':   
        
            header = "application/json"

            for position in list:

                title = position

                option = json.dumps({
                            "type": "reply",
                            "reply": {
                                "id": title,
                                "title": title
                            }
                        })
                list_option = list_option +','+ option

                #list_option.append(option)
            list_option = list_option[1:]
            body = json.dumps({
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
         })
            body = body.replace('\\','')

    elif channel == 'blip'or channel == 'instagram' or channel == 'messenger' :

        count = 0
        header = "application/vnd.lime.select+json"
        

        for position in list:

            title = position

            count = count + 1

            option = json.dumps({
                    "order": count,
                    "text": title
                })
            list_option = list_option +','+ option

        body = json.dumps({
        "scope":"immediate",
        "text":"Choose an option",
        "options":[
            list_option
        ]
    })
        body = body.replace('\\','')

    else:

        header = "text/plain"

        count = 0

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

    if channel == "whatsapp" or channel == "blip":

        body_blip = body_blip.replace('\\','')

    return body_blip

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
    
    body_blip = json.dumps({

        "body" : body,
        "header" : header

    })

    return body_blip

app = Flask(__name__)

@app.route('/')
def hello_world():
    
    return 'Hello World!'

app.run(debug=True) 

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
    
    
        

                
   