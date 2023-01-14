# Q. Write a python program to get a Fibonacci series between 0 and 50.

num = int(input('Enter your range : '))
first_value = 0
second_value = 1
print('Fibonacci Series')
for i in range(num):
        fib = first_value + second_value
        first_value = second_value
        second_value = fib
        if fib<=num:
         print(fib,end=" ")