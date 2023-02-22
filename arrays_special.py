import math

def float_range(start_value, end_value, step):
    arr = []
    i = 1
    start_value = float(start_value)
    end_value = float(end_value)
    step = float(step)
    value = start_value
    
    if start_value >= end_value or step <= 0.00:
        return arr

    while(value < end_value):
        #if the value is essentially the end value but due to floating point arithmetic, it is still included in the loop, do not add to array
        if math.isclose(value, end_value):
            continue
        arr.append(value)
        value = start_value + i * step
        i += 1
    return arr
