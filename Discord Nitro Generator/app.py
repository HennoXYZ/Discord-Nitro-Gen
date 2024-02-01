import random
import string
import requests as re

char = string.ascii_letters + string.digits + "@"
rnd = ""
splt = []

while True:
    for l in range(17):
        rnd += random.choice(char)
    link = "https://discord.gift/"+rnd
    if link not in splt:
        splt.append("https://discord.gift/"+rnd)
        res = re.get(link)
        html = res.text
        if "redeem" in html.lower():
            print("Succeed:",link)
        else:
            print("Failed!")
    rnd = ""
