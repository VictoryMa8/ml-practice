x = 5 % 2

def fizz_buzz():
    for i in range(1, 100):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizz Buzz!")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def main():
    print(x)
    fizz_buzz()

if __name__ == "__main__":
    main()