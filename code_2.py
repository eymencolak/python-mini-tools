import time

def rocket_countdown(seconds):
    while seconds > 0:
        print(seconds)
        time.sleep(1)
        seconds -= 1
    print("Blast off!")

rocket_countdown(10)