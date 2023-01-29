import random
import os
import time
import datetime
from translate import Translator
from termcolor import colored
from datetime import datetime
from pyfiglet import Figlet
import pytz

f = Figlet(font='big')

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
        timezone = pytz.timezone('UTC')
        print(f.renderText('Reloj')) # Using Figlet for text art
        print(time.strftime(colored(day, 'yellow') + " %d " + "de " + month + " %X %p \n" + colored(s, 'red')))
        print("Zona horaria: " + str(datetime.now(timezone).strftime('%Z')))
