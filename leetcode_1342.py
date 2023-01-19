def steps_to_reach_zero(value):
    counter = 0
    if value == 0:
        return 0
    while value > 0:
        if value % 2 != 0:
            value = value - 1
        else:
            value = value / 2
        counter+=1
    return counter


print(steps_to_reach_zero(14))