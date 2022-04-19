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