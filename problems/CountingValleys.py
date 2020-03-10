def countingValleys(n, s):
    i = 0
    result = 0
    sea_level = 0

    while i < len(s):
        if s[i] == 'D':
            sea_level -= 1
            i+=1
        else:
            if sea_level == -1:
                result += 1
            sea_level += 1
            i+=1
    
    return result