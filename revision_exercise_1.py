from random import randint

def ran_num():
    return randint(1,11)

def is_equal(a, b):
    return a==b


if __name__ == '__main__':
    num = ran_num()
    while True:
        inp = int(input("Please enter your number: "))
        if is_equal(inp, num):
            print("You guessed the right number")
            break
        print("You guessed the wrong number")
        


