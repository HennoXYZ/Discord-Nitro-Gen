import random
import string

f = open("nitros.txt","w")
char = string.ascii_letters + string.digits + "@"

for i in range(10001):
    rnd = ""
    for l in range(17):
        rnd += random.choice(char)
    f.write("https://discord.gift/"+rnd+",\n")
    