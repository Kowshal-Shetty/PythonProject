import time

def time_decor(func):
    def wrapper():
        start_time = time.time()
        print("start the program")
        print(start_time)
        func()
        end_time = time.time()
        print("End the program")
        print(end_time)
        print("Total time taken is", start_time-end_time)
    return wrapper()

@time_decor
def test_funt_1():
    print("start function 1")
    time.sleep(3)
@time_decor
def test_funt_2():
    print("Start function 2")
    time.sleep(3)