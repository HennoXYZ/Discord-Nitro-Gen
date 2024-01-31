import requests as re

nitrolar = []
f = open("nitros.txt","r")
r = f.read()
nitrolar = r.split(",\n")

for i in nitrolar:
    res = re.get(i)
    html = res.text
    if "redeem" in html.lower():
        print("Succeed:",i)
    else:
        print("Failed!")




