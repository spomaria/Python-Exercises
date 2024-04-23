def toCelsius(x):
    return (x - 32)*5/9

# the function range below generates an array of numbers
# from 0 to 100 where the differnce between every two consecutive numbers is 10
for x in range(0, 101, 10):
    print("{:>3} F | {:>6.2f} C".format(x, toCelsius(x)))