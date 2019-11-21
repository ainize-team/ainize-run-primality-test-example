import random

class Primality_test():
  def __init__(self):
    pass

  def doFermatPrimalityTest(self, n: int, round: int = 200) -> bool:
    for _ in range(round):
      a = random.randint(2, n - 1)
      if pow(a, n - 1, n) == 1:
        pass
      else:
        return False
    return True

  def doMillerRabinPrimalityTest(self, n: int, round: int = 100) -> bool:
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

  def isPrime(self, randomNumber: int) -> bool:
    if randomNumber <= 1:
      return False
    elif randomNumber % 2 == 0:
      return False
    else:
      # Fermat's primality test
      if self.doFermatPrimalityTest(randomNumber, 10):   # probably true
        # Miller-Rabin primality test
        if self.doMillerRabinPrimalityTest(randomNumber, 100):   # probably true
          return True
        else:   # composite found
          return False
      else:   # witness found
        return False
