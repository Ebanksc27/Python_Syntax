def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """

    for num in range(start, stop +1): # iterates over the range of numers from 'start' to 'stop + 1'. Stop +1 used to ensure stopping value is included in range
        print(num)


count_up(5, 7)        
