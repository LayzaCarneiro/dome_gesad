def compare(list1 = list(), list2 = list()):
    for item in list1:
        if item in list2:
            return True
    return False