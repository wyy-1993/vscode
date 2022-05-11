import random

random_number = random.randint(1,100)
print(random_number)

while True:
    input_number = int(input("please input a number:"))
    if input_number > random_number:
        print("it is too big!")
    elif input_number < random_number:
        print("it is too small")
    else:
        print("Bingo!!")
        break

"""
test
"""

print("test!!")


    