import time

def blink_square():
    while True:
        print("○", end="")
        time.sleep(1.0)

if __name__ == "__main__":
    blink_square()