#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    line = ""
    for i in my_list:
        if counter < x:
            try:
                line += str(i)
                counter += 1
            except IndexError:
                print("Error en el programa")
    print(line)
    return counter
