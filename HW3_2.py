'''
Create a new module called arrays_special.py and define a function in it called
float_range(start_value, end_value, step)
with all the parameters real numbers, which returns an array of float values:
start_value, start_value + step, start_value + 2*step,…
while we are less than end_value. The end_value is not included.
This function should work like the standard range(…). Please recall that the latter works with integers
only. Our function resolves this inconvenience.
If start_value >= end_value or step <= 0.00, the function must return an empty array.
In the main program HW3_2.py, import the arrays_special module and test the function you created –
evaluate the sum of values starting from start_value and going up to stop_value with the given
step, including the stop_value in case it fits to the pattern (i.e., if stop_value = start_value
+ m * step for some positive integer m).
'''