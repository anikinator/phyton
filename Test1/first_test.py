def spam(number):

    return 'bulochka'*number


def my_sum(list_of_numbers):

    summ = 0

    for i in list_of_numbers:
        summ += i
    return summ


def shortener(string):

    result = ''
    string = string.split()

    for i in string:
        if (len(i) > 6):
            result += str(i[0:6] + '*' + ' ')
        else:
            result += str(i) + ' '

    return result.strip()


def compare_ends(words):

    my_counter = 0

    for i in words:
        if len(i) >= 2 and i[0] == i[-1]:
            my_counter += 1

    return my_counter