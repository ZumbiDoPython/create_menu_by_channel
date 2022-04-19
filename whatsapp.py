import os
import json

body = {}
list_option = []

def made_quick_reply (list, text):

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
                    "buttons": 

                        list_option
                      
                    
                }
            }
         },"header" : header}

def made_menu (list,text):
        
    header = "application/json"

    for position in list:

                title = position
                option = {
                                    "id": title,
                                    "title": title
                                }
                list_option.append(option)

    body ={  
        
        "body" :

        {
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
                            "rows": 

                                list_option
                                
                            
                        }
                    ]
                }
            }
        },

   "header" : header 

    }

    return body