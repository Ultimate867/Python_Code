
#return.py
#Returns the number of positive integers in a list of integers.

def positive(integers): 
    n = 0
    for i in range(len(integers)):
        if integers[i] > 0:
            n = n + 1
    return n
            
def main():
    integers = eval(input("Enter a list of numbers: "))
    n = positive(integers)
    print("There are", n, "positive integers")

main()
