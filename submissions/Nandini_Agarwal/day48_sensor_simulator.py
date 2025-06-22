import time
import threading
import random

def temperature(i,j):
    n=random.randint(i,j)
    print(f"[Temperature Sensor] Temperature:{n}")

def humidity(i,j):
    n=random.randint(i,j)
    print(f"[Humidity Sensor] Humidity:{n}")

start_time = time.time()

while time.time() - start_time < 10:
    
    temp = threading.Thread(target=temperature, args=(20, 30))
    humid = threading.Thread(target=humidity, args=(40, 60))

    temp.start()
    humid.start()

    temp.join()
    humid.join()

    time.sleep(0.01)

print("Sensor simulation complete.")