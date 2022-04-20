import os
import json

body = {}
list_option = []
count = 0

def made_menu (list, text):

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
            "options": 

                list_option
                
            
        }

    return body



def made_quick_reply (list,channel, text):

    for position in list:

            title = position

            count = count + 1

            option = {
                    "order": count,
                    "text": title
                }
            list_option.append(option)

    body = {
        "scope":"immediate",
        "text":text,
        "options":
            list_option
        
    }

    return body