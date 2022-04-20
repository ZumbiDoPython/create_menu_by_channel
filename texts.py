import os
import json

body = ''
list_option = ''

def made_text(list,channel, text):

    count = 0

    for position in list:

            title = position

            count = count + 1

            couter = str(count)

            list_option = list_option + '\n' + couter + " " + title

    body = text + "\n\n" + list_option

    return body