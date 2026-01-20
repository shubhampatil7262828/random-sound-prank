import time
import random
import winsound

while True:
    wait_time = random.randint(120, 600)   # 2 to 5 minutes
    time.sleep(wait_time)
    winsound.PlaySound("sound.wav", winsound.SND_FILENAME)
    