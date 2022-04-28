import os
from flask import Flask, jsonify, request
import json
import whatsapp
import blipchat
import texts

def made_menu_description (list,channel, text, description):

    if channel == 'whatsapp': 

        header = "application/json"
        body = whatsapp.made_menu_with_descripiton (list = list, text = text, description = description )

    elif channel == 'blipchat': 

        header = "application/vnd.lime.select+json"
        body = blipchat.made_menu_with_descripiton (list = list, text = text, description = description )
    
    body_blip = json.dumps({

        "body" : body,
        "header" : header

    })

    return body_blip

def made_menu (list,channel, text):
   
    body = {}

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

    body = {}

    header = "text/plain"
    body = texts.made_text(list = list, text = text)

    body_blip = json.dumps({

        "body" : body,
        "header" : header

    })
    return body_blip