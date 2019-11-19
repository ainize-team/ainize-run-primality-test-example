import random

def doFermatPrimalityTest(n: int, round: int = 200) -> bool:
  for _ in range(round):
    a = random.randint(2, n - 1)
    if pow(a, n - 1, n) == 1:
      pass
    else:
      return False
  return True

def doMillerRabinPrimalityTest(n: int, round: int = 100) -> bool:
  for _ in range(round):
    a = random.randint(2, n - 2)
    d = n - 1
    r = 0
    while pow(d, 1, 2) == 1:
      r += 1

    x = pow(a, r, n)
    if x == 1 or x == n - 1:
      pass
    else:
      for _ in range(r - 1):
        x = pow(x, 2, n)
        if x == n - 1:
          break
        else:
          pass
      return False   # composite
  return True

def isPrime(randomNumber: int) -> bool:
  if randomNumber <= 1:
    return False
  elif randomNumber % 2 == 0:
    return False
  else:
    # Fermat's primality test
    if doFermatPrimalityTest(randomNumber, 10):   # probably true
      # Miller-Rabin primality test
      if doMillerRabinPrimalityTest(randomNumber, 100):   # probably true
        return True
      else: # composite found
        return False
    else: # witness found
      return False


def main():
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

if __name__ == '__main__':
  main()
