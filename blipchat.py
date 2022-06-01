import os
import json

body = {}
list_option = []


def made_menu (list, text):

    body = {}
    list_option = []

    count = 0

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



def made_quick_reply (list, text, order):

    body = {}
    list_option = []
    option = {}

    count = 0

    for position in list:

            title = position

            count = count + 1

            if order == True:

                option['order'] = count

            

            option ['text'] =  title
                
            list_option.append(option)
            print(option)
            print(list_option)

    body = {
        "scope":"immediate",
        "text":text,
        "options":
            list_option
        
    }

    return body

def made_menu_with_descripiton(list, text, description):

    body = {}
    list_option = []

    count = 0

    for position in list:

            title = position + " - " + description[count]

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
