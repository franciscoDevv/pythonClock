import random
import os
import time
from translate import Translator

list = ["¡Ten un buen día!", "Si te caes tres veces, levántate cuatro", "Prohibido rendirse", "Lucha por ti mismo, por lo que eres, por quien eres", "Comienza a ser ahora, lo que serás de ahora en adelante"]
s = random.choice(list)

start_time = time.time()

d = time.strftime("%A")
m = time.strftime("%B")
translator = Translator(to_lang="es")
day = translator.translate(d)
month = translator.translate(m)
while True:
    current_time = time.time()
    if current_time - start_time >= 1:
        start_time = current_time
        os.system('clear')
        print(time.strftime(day + " %d " + "de " + month + " %X %p \n" + s))
