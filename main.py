from server import Server

def main():
  simpleServer = Server()
  simpleServer.run()
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
