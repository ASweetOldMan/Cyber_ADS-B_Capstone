import time



currentTime = time.time()
lastTime = 0
x = 0
interval = 1.0


while(1):
    lastTime = currentTime
    print("lastTime: " + str(lastTime))
    print("x: " + str(x))
    currentTime = time.time()
    print("currentTime:        " + str(currentTime))
    timeUntilNextFrame = interval - (currentTime - lastTime)
    print("timeUntilNextFrame: " + str(timeUntilNextFrame))
    time.sleep(timeUntilNextFrame)
    currentTime = time.time()
    x = x + 1


