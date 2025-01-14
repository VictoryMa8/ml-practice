'''
- a lambda function is a small anonymous function
- it can take any number of arguments, but can only have one expression
syntax: lambda <arguments> : <expression>
'''

example = lambda x : x + 10

# template for a function with lambda
def template(n):
  return lambda a : a * n

# create a new function from this template function
# the argument passed through will be n
doublingFunction = template(2)
    # return a <- a * 2

def main():
    print(example(5)) # prints 5 --> lambda expression --> 5 + 10 --> 15
    print(doublingFunction(50))

if __name__ == "__main__":
    main()