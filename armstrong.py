import functools
import os
import time 
import tracemalloc



def timer(func):
    """
    Print the runtime of the decorated function
    """
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"\033[37mTime Taken          :\033[36m {run_time:.8f}\033[0m")
        return value
    return wrapper_timer

def measure_memory(func):
    """
    Print the memory taken by the function
    """
    @functools.wraps(func)
    def wrapper_memory(*args, **kwargs):
        tracemalloc.start()
        value = func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        print(f"\033[37mCurrent memory usage:\033[36m {current / 10**6}MB\033[0m")
        print(f"\033[37mPeak                :\033[36m {peak / 10**6}MB\033[0m")
        tracemalloc.stop()
        return value
    return wrapper_memory

def function_name(func):
    """
    print the name of function
    """
    @functools.wraps(func)
    def wraper_print(*args, **kwargs):
        value = func(*args, **kwargs)
        print(f"\n\033[37mFunction Name       :\033[35;1m {func.__name__}\033[0m")
        return value
    return wraper_print


def is_armstrong(number):
    """
    If number is armstrong number
    it returns number and armstrong_number as true
    """
    sum = 0
    order = len(str(number))
    temp = number
    while temp > 0:
        sum += (temp % 10) ** order
        temp //= 10
    if number == sum:
        return True
    else:
        return False

def get_closest_lower_armstrong_number(number):
    """
    finds the closest lower armstrong number
    """
    for num in range(number-1, 0, -1):
        if is_armstrong(num):
            return num

def get_closest_higher_armstrong_number(number):
    """
    finds the closest lower armstrong number
    """
    is_armstrong_number = False
    while not is_armstrong_number:
        number += 1
        if is_armstrong(number):
            return number


@measure_memory
@timer
@function_name
def get_armstrong_number(number):
    """
    number should be an positive integer
    it return the number if it is an armstrong number
    if it is not an armstrong number then it will return,
    the closest arm strong number lower and higher
    """
    if is_armstrong(number):
        print(number)
        return {
            'arm_strong_number': number
        }
    else:
        return {
            'closest_lower_armstrong_number' :
                get_closest_lower_armstrong_number(number),
            'closest_higher_armstrong_number' :
                get_closest_higher_armstrong_number(number)
        }



if __name__ == "__main__":
    while True:
        try:
            number = int(input("please enter a number to find armstrong number: "))
            break
        except ValueError:
            print("Invalid number try again")
    output = get_armstrong_number(number)
    print("********Output***********")
    print(output)