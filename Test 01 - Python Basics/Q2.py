'''
Question 2
'''
def find_median(numbers: list)->  float:
    '''
    :param numbers: list of numbers
    :return: median of numbers, if
    '''
    numbers.sort()
    n = len(numbers)
    if n == 0:
        return 0
    elif n == 1:
        return float(numbers[0])
    elif n % 2 == 1:
        return float(numbers[n // 2])
    else:
        a = numbers[(n // 2)-1]
        b = numbers[n // 2]
        return (a+b)/2
print(find_median([3,1,4,1,5]))
print(find_median([7,2,9,10]))
print(find_median([1,2,3,4,5,6]))
print(find_median([1]))
print(find_median([42]))
print(find_median([]))