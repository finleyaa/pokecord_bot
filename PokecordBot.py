import requests
import json
import keyboard
import time
from pprint import pprint
from pywinauto import application

authorization_id = ""

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
            "authorization": f"{authorization_id}"}

GOOGLE_URL = "https://images.google.com/searchbyimage?image_url="

discord_channel_id = ""

API_URL = f"https://discordapp.com/api/v6/channels/{discord_channel_id}/messages"

pokemon_msg = requests.get(API_URL, headers=headers)
json_pmsg = json.loads(pokemon_msg.text)

print("GOT MESSAGE")

index = 0

while index < 50:
    if len(json_pmsg[index]["embeds"]) > 0:
        try:
            if "PokecordSpawn" in json_pmsg[index]["embeds"][0]["image"]["url"]:
                image_url = json_pmsg[index]["embeds"][0]["image"]["url"]
                break
        except:
            continue
    index += 1

if index == 50:
    exit()

print("FOUND IMAGE LINK - UPLOADING IMAGE")

reverse_img_search = requests.get(GOOGLE_URL + image_url, headers=headers)
text_f = reverse_img_search.text.split(" (Pokémon) - Bulbapedia")[0][-20:].split(">")

pokemon_name = text_f[len(text_f) - 1]
print("Found pokemon: " + pokemon_name)

discord_window = application.Application()
discord_window.connect(title_re="#spam - Discord")

discord_appdialog = discord_window.top_window()
discord_appdialog.set_focus()

keyboard.write(f"p!catch {pokemon_name.lower()}")
keyboard.press_and_release("enter")

