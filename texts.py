import os
import json

body = ''
list_option = ''
count = 0

def made_text(list,channel, text):

  

    header = "text/plain"

    for position in list:

            title = position

            count = count + 1

            couter = str(count)

            list_option = list_option + '\n' + couter + " " + title

    body = text + "\n\n" + list_option

    return body