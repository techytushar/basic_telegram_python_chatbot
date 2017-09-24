import requests
import json

TOKEN = "429694129:AAG8wl8YSYw32P6DDJW0I9cal733XAEPs9Y"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

def json_response(url):
	r = requests.get(url).content.decode("utf8")
	j = json.loads(r)
	return j

def get_updates():
	url = URL+"getUpdates"
	js = json_response(url)
	return js

def get_chat_id_text(js):
	total = len(js["result"])
	last = total-1
	#text = js["result"][int(last)]["message"]["text"]
	id = js["result"][int(last)]["message"]["chat"]["id"]
	name = js["result"][int(last)]["message"]["from"]["first_name"]
	return(name,id)

def send_message(name,id):
	url = URL+"sendMessage?text=Hello {} I am a chatbot&chat_id={}".format(name,id)
	requests.get(url)

name,id = get_chat_id_text(get_updates())
send_message(name,id)
