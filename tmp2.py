def list_of_simple_num(lim_to):
    temp_list = ''
    for num in range(2, lim_to):
        cont = 0
        for i in range(2, num):
            if num % i == 0:
                cont += 1
        if cont < 1:
            temp_list += str(num) + ' '

    return(temp_list.split())


print(list_of_simple_num(100))