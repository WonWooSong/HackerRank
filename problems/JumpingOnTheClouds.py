def jumpingOnClouds(c):
    i = 0
    jump = 0
    while i < len(c)-1:
        # if 2 steps away is not null and is not 1 it will count 1 step
        if i+2 < len(c) and c[i+2] != 1:
            i += 1
            
        # this is always 1 jump
        i += 1
        jump += 1

    return jump