import random
import os
import time

list = ["¡Ten un buen día!", "Si te caes tres veces, levántate cuatro", "Prohibido rendirse", "Lucha por ti mismo, por lo que eres, por quien eres", "Comienza a ser ahora, lo que serás de ahora en adelante"]
s = random.choice(list)

start_time = time.time()

while True:
    current_time = time.time()
    if current_time - start_time >= 1:
        start_time = current_time
        os.system('clear')
        print(time.strftime("%d, %A %B %X %p " + s))
