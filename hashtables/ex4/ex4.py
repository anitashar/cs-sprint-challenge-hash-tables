# find numbers which have negative values
def has_negatives(a):
    """
     YOUR CODE HERE
    """
    # Your code here
    dicti = {}
    result = []

    if len(a) < 1:
        return None
    # if index is greater than zero (ensures positive index), then add them to dict 
    for i in a:
        if i > 0:
            dicti[i] = i
            
    for i in a:
        if i * -1 in dicti:#creating negative values
            result.append(abs(i))#creating positive values
    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))