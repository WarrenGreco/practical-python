# bounce.py
#
# Exercise 1.5

height = 100 * 3/5
bounce = 1
number = 10

while bounce <= number:
    print(round(bounce,4), round(height,4))
    bounce = bounce + 1
    height = height * 3/5

print('Number of bounces', round(bounce,4))
print('Final height', round(height,4))
