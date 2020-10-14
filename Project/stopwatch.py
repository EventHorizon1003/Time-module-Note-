#! python3
#Name: stopwatch.py - A simple stopwatch program

import time

# Display the program's instruction
print("Press Enter to begin.")
print("Press Enter to start the stopwatch")
print("Press Ctrl + c to quit the program")

input("press enter to begin")
print("Started.")
startTime = time.time() # get the first lap's start time
lastTime = startTime
lapNum = 1

# Start tracking the lap times
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2) # last time
        totalTime = round(time.time() - startTime, 2) # Total time
        print('Lap #%s: Passed: %s (%s)' %(lapNum, totalTime,lapTime),end="")
        lapNum += 1
        lastTime = time.time()  # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-c exception to keep its error message from displaying
    print("\n Done.")

