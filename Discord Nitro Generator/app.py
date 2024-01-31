import random
import string
import requests as re

f = open("trying.txt","r+")
char = string.ascii_letters + string.digits + "@"
rnd = ""

while True:
    for l in range(17):
        rnd += random.choice(char)
    link = "https://discord.gift/"+rnd
    read = f.read()
    splt = read.split(",\n")
    splt.pop(-1)
    if link not in splt:
        f.write("https://discord.gift/"+rnd+",\n")
        res = re.get(link)
        html = res.text
        if "redeem" in html.lower():
            print("Succeed:",link)
        else:
            print("Failed!")
    rnd = ""