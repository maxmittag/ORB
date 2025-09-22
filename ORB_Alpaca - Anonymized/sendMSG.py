import requests

def sendMessage(input_message):
    base_url = "https://api.telegram.org/botSECRET/sendMessage?chat_id=-SECRET&text={}".format(input_message)
    requests.get(base_url)
    return

