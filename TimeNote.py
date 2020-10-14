# Scheduling tasks and launching programs

import time

# Time module -> time.time() / time.sleep()
# 1)Time module allow python program to read the system clock for the current time
#   Unix epoch is a time reference commonly used in programming 1/1/1970 (UTC)
#   time.time will return the number of second since UTC
#   notefunction()
# 2)U can use time.time to calculate the how long a piece of code takes to run
#   notefunction1()
#   cProfile.run() can provide much more information level of detail than the time.time()
# 3)If u need to pause your program for a while -> time.sleep()
#   ctrl-c will not interrupt time.sleep() calls in IDLE
# 4)Rounding number -> round()
#   Syntax: round(<num>,<how many decimal point>) ;  default it will round off become an integer

import datetime


# Datetime Module -> datetime
# 1)Figuring out what date was 205 days ago -> datetime module
# 2)Syntax : datetime.datetime.now(<year>,<month>,...) -> return datetime object by according to ur computer's clock
#          : datetime.datetime.fromtimestamp(<sec>) -> pass a datetime obj for the moment <sec> seconds after the Unix epoch
#          : save the date in a variable and use the methods to display the specify time such as year, month
#   notefunction2()
# 3)Datetime objects can be compared with each other using comparison operators to find out which one precedes the other
#   notefunction3()
# 4)Timedelta Data type -> represent a duration of time rather than a moment in time
#   notefunction4()
# 5)Datetime objects aren't very friendly to the human eye. So u can use strftime() method to display a datetime obj
# %Y Year with century, as in '2014'
# %y Year without century, '00' to '99' (1970 to 2069)
# %m Month as a decimal number, '01' to '12'
# %B Full month name, as in 'November'
# %b Abbreviated month name, as in 'Nov'
# %d Day of the month, '01' to '31'
# %j Day of the year, '001' to '366'
# %w Day of the week, '0' (Sunday) to '6' (Saturday)
# %A Full weekday name, as in 'Monday'
# %a Abbreviated weekday name, as in 'Mon'
# %H Hour (24-hour clock), '00' to '23'
# %I Hour (12-hour clock), '01' to '12'
# %M Minute, '00' to '59'
# %S Second, '00' to '59'
# %p 'AM' or 'PM'
# %% Literal '%' character
# notefunction5()
# In contrast, if you want to convert to strings into datetime Obj -> datetime.datetime.strptime()
# Syntax: datetime.datetime.strptime('October 21, 2015', '%B %d, %Y')


def notefunction():
    a = time.time()
    hours = a / 60 / 60
    days = hours / 24
    month = days / 30
    year = month / 12
    j = input("What do u want me to show ???  h/d/m/y???")
    if j == "h":
        print(hours)
    elif j == "d":
        print(days)
    elif j == "m":
        print(month)
    elif j == "y":
        print(year)


def sample():  # sub function of the notefunction1
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product


def notefunction1():
    startTime = time.time()
    sp = sample()
    endTime = time.time()
    print("The result is {0} digits long".format(len(str(sp))))
    print("It took {0} seconds to calculate".format(endTime - startTime))


def notefunction2():
    print(datetime.datetime.now())  # Show the time now
    var = datetime.datetime(2015, 10, 21, 19, 20, 0)  # save the time/date in a variable
    print(var.month)  # Different methods : var.year/var.day/var.hour/var.minute/var.second


def notefunction3():
    a = datetime.datetime(2015, 2, 25, 12, 32, 0)
    b = datetime.datetime(2016, 1, 24, 12, 12, 0)
    print(b > a)


def notefunction4():
    delta = datetime.timedelta(days=12, hours=12, minutes=12)  # there are no month / year arguments
    A = datetime.datetime.now()
    B = datetime.datetime(2020, 10, 16, 0, 0, 0)
    C = B - A
    print(delta.seconds)  # the methods only have days, seconds and microseconds
    print(delta.total_seconds())
    print(str(delta))
    print(str(C))
    print(C.total_seconds())


def notefunction5():
    oct21 = datetime.datetime(2015, 10, 21, 16, 29, 0)
    print(oct21.strftime("%Y/%m/%d %H:%M:%S %p"))  # example strftime()


def notefunction6():
    a = datetime.datetime.strptime('October 21, 2015', '%B %d, %Y')  # The sec arg is date information (must match)
    print(a)


def new_note(n):
    if n == '0':
        notefunction()
    elif n == '1':
        notefunction1()
    elif n == '2':
        notefunction2()
    elif n == '3':
        notefunction3()
    elif n == '4':
        notefunction4()
    elif n == '5':
        notefunction5()
    elif n == '6':
        notefunction6()


# Loop
def generator():
    while True:
        print("What example you want me to show ?")
        num = input()
        new_note(num)


if __name__ == "__main__":  # prevent the module run when this file is imported
    generator()
