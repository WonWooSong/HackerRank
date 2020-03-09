def sockMerchant(n, ar):

    # sorts list
    result = 0
    i = 0   # counter for the while loop
    ar.sort()

    while i < len(ar) - 1:
        # if the current item is last item of the list, break the while loop.
        if i == len(ar):
            break
        # check if current item is same as next item. Then, increase the result
        if ar[i] == ar[i+1]:
            i = i + 2
            result+=1
        # else just increase the counter
        else:
            i = i +1
    # returns the result
    return result