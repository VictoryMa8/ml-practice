'''
- a lambda function is a small anonymous function
- it can take any number of arguments, but can only have one expression
syntax: lambda <arguments> : <expression>
'''

example = lambda x : x + 10

def main():
    print(example(5)) # prints 5 --> lambda expression --> 5 + 10 --> 15

if __name__ == "__main__":
    main()