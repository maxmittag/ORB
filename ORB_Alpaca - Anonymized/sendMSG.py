import requests

def sendMessage(input_message):
    base_url = "https://api.telegram.org/bot6754066340:AAHRU8ai0qhSo9r3tPUNu8NkhALzBUYgRu4/sendMessage?chat_id=-SECRET&text={}".format(input_message)
    requests.get(base_url)
    return
