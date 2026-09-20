'''
Break, continue and pass are loop control statements in python.

Break- is used to exit/break a loop prematurely before the loop has iterated through 
all the items or reached a condition.

Continue- is used to skip the rest of the code in a loop and moves the to the next iteration of the loop.

Pass- is a null operation or placeholder. It is used when a statement is semantically required but we don't
want to execute any code. It does nothing but allows us to maintain the structure of our program.
'''

#Prints numbers from 1 to 100 excluding multiples of 3, 5 and 15 replaced by  "Fizz", "Buzz" and "FizzBuzz" respectively.
for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


count = 1
while True:#while count<101
    if count % 15 == 0:
        print("FizzBuzz")
        count += 1
        continue
    if count % 3 == 0:
        print("Fizz")
        count += 1
        continue
    if count % 5 == 0:
        print("Buzz")
        count += 1
        continue 
    if count > 100:
        break
    print(count)
    count += 1


       