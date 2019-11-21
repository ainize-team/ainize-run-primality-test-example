from server import Server
from primality import Primality_test

def main():
  # Server.run()
  primality = Primality_test()
  result = primality.isPrime(11)
  print(result)
  '''
  while True:
    number = input("Enter a number: ")
    try:
        number = int(number)
        if number < 0:
            print("Positive integer only.")
            continue
        break
    except ValueError:
        print("Only positive integer allowed.") 

  if isPrime(number):
    print("Number %d is prime." % (number))
  else:
    print("Number %d is NOT prime." % (number))
    '''

if __name__ == '__main__':
  main()
