import random
import string
import requests as re

char = string.ascii_letters + string.digits + "@"
rnd = ""

while True:
    for l in range(17):
        rnd += random.choice(char)
    link = "https://discord.gift/"+rnd+",\n"
    res = re.get(link)
    html = res.text
    if "redeem" in html:
        print("Succeed:",link)
    else:
        print("Failed!")