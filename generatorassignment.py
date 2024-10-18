# Your first name: Zabrina
# Your section:Intro to programming

import random
import matplotlib.pyplot as plt

# Write your functions with their docstrings here

# nextMiddleSquare
def next_middle_square(random_numb:int)->int:
       random_numb2 = str(random_numb ** 2)
       if len(random_numb2) <= 3:
               random_numb3 = random_numb2.rjust(4, '0')
               return int(random_numb3[1:3])
       else:
               return int(str(random_numb2[1:3]))

# listMiddleSquare
def listMiddleSquare(x:int)->int:
       list = []
       count = 0
       while count < 10:
               x = next_middle_square(x)
               count += 1
               list.append(x / 100)
       return list
   
# nextLehmer
def nextLehmer(a:int, m:int, x:int):
       return(a * x % m)

# listLehmer
def listLehmer(random_number:int)->float:
       a = 17
       m = 101
       count = 0
       list = []
       while count < 10:
               random_number = (nextLehmer(a, m, random_number))
               count += 1
               list.append(random_number / m)
       return list

# listRandom
def listRandom():
  count = 0
  list = []
  while count < 10:
     y = random.random()
     list.append(y)
     count += 1
  return list

def chartRandomNumbers(mid, lehmer, rand):
  '''
  This function draws a histogram of the three lists on the same plot
  :param mid: a list of random numbers from middle squares
  :param lehmer: a list of random numbers from lehmer
  :param rand: a list of random numbers from Python random module
  '''
  multi = [mid, lehmer, rand]
  plt.hist(multi, histtype='bar', label=['middle square', 'lehmer', 'random module'])
  plt.legend(prop={'size': 10})
  plt.show()
  


def main():
  start = 29
  list1 = listMiddleSquare(start)
  list2 = listLehmer(start)
  list3 = listRandom()
  chartRandomNumbers(list1, list2, list3)

if __name__ == "__main__":
  main()
