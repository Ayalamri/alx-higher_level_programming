#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for i in range(list_length):
        vv = 0

        try:
            if isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float)):
                vv = my_list_1[i] / my_list_2[i]
            else:
                raise TypeError("wrong type")

        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")

        finally:
            result_list.append(vv)

    return result_list
