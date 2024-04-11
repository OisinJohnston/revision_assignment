(lambda x: print(f'{x} is {"not " if x[:len(x)//2] != x[len(x)//2:] else ""}symettrical and is {"not " if x[::-1] != x else ""}a palindrome'))(input("Enter the test string: "))


