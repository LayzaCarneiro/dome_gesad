def compare(list1 = list(), list2 = list()):
    for item in list1:
        if item in list2:
            return True
    return False

def compare_index(list_index = list(), list = list()):

    index = 0

    for item in list_index:
        if item in list:
           return index
        index += 1
    return -1