import os
import json

body = {}
list_option = []

def made_quick_reply (list, text):

    body = {}
    list_option = []

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
    body = {
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
         }

    return body

def made_menu (list,text):

    body = {}
    list_option = []

    for position in list:

                title = position
                option = {
                                    "id": title,
                                    "title": title
                                }
                list_option.append(option)

    body ={  
        
        
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
        }

    return body

def made_menu_with_descripiton (list, text, description):

    body = {}
    list_option = []
    count = 0

    for position in list:


                
                title = position
                option = {
                                    "id": title,
                                    "title": title,
                                    "decription" : description[count] 
                                }
                list_option.append(option)
                count = count + 1

    body ={  
        
        
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
        }

    return body
