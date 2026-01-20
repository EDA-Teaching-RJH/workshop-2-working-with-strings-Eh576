import math  

def main():
  A = int (input("Input "))
  B = int (input("Input "))
  pythag(A,B)


def pythag(A,B):
    C = math.sqrt((A**2)+(B**2))
    print (C)
main()
