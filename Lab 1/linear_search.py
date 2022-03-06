def linear_search(values, target):
    
    for i in range(len(values)):
        if values[i]==target:
            return i
    return -1