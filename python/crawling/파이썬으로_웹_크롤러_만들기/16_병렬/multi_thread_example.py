# import threading
import threading
import time

def print_time(threadName, delay, iterations):
    start = int(time.time())

    for i in range(0, iterations):
        time.sleep(delay)
        seconds_elapsed = str(int(time.time()) - start)

        print("{} {} {}".format(i, seconds_elapsed, threadName))


# try:
#     threading.Thread(target = print_time, args=("Fizz", 3, 13)) #
#     threading.Thread(target = print_time, args=('Counter', 1, 30))
#     threading.Thread(target = print_time, args=('Buzz', 5, 8))
    
# except:
#     print("Error: unable to start thread") 

for i in range(1):
    try:
        threading.Thread(target = print_time, args=("Fizz", 3, 13)).start()
        threading.Thread(target = print_time, args=('Counter', 1, 30)).start()
        threading.Thread(target = print_time, args=('Buzz', 5, 8)).start()
    except:
        print("Error: unable to start thread")