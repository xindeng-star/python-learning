# Lab01, CS 8
# [Xin Deng]
# [type your partner's name here if you worked with someone]

def isMultiple(num1, num2):
    ''' Function that takes two integers (num1) and (num2).
    Returns True if num2 is a multiple of num1, and returns
    False otherwise (you may assume num2 >= num1 for this function).
    * If num1 is equal to 0, your function should return None.
    '''
    if num1 == 0:
        return None
    if num2 % num1 == 0:
        return True
    else:
        return False

assert isMultiple(1,1) == True
assert isMultiple(1,10) == True
assert isMultiple(2,3) == False
assert isMultiple(4,16) == True
assert isMultiple(4,7) == False
assert isMultiple(0,3) == None
assert isMultiple(3,0) == True





def incrementKeyCount(D, key):
   
   ''' Function that takes in a Dictionary object (D) containing KEY:VALUE
   pairs where the VALUE is a count representing the number of times the KEY
   is incremented.
   * If the parameter key does not exist in D, then a new KEY:VALUE
   pair is created in D with key:1 (the first time the key is incremented).
   * If the parameter key does exist in D, then the key's VALUE is
   incremented by 1.
   * Note that since dictionaries are mutable, this function does
   not return a value.
   * Consider using the in operator to check if a key exists in a Dictionary
   * Assert examples below illustrate correct behavior for this function
   '''
   if key in D:
       D[key]+=1
   else:
       D[key]=1

dict1 = {}
assert len(dict1) == 0
assert incrementKeyCount(dict1, "CS8") == None
assert len(dict1) == 1
assert ("CS8" in dict1) == True
assert dict1["CS8"] == 1
assert incrementKeyCount(dict1, "CS8") == None
assert len(dict1) == 1
assert dict1["CS8"] == 2
assert incrementKeyCount(dict1, "MATH3A") == None
assert len(dict1) == 2
assert ("MATH3A" in dict1) == True
assert dict1["MATH3A"] == 1




def computeGrade(percentage):
   ''' Return the corresponding letter grade string based on the value of
   percentage using the following scale:
   [100 - 90]: 'A'
   (90 - 80] : 'B'
   (80 - 70] : 'C'
   (70 - 60] : 'D'
   (60 - 0]  : 'F'
   * If percentage is not a number type (int or float) OR if percentage is
   outside the range of [100 - 0], return an empty string ("").
   * Note, you can check if percentage is an int with
   type(percentage) == int, and a float with type(percentage) == float
   '''
   if type(percentage) !=int and type(percentage) !=float:
       return ""
   if percentage < 0 or percentage > 100:
       return ""
   if percentage >= 90 and percentage <= 100:
       return "A"
   elif percentage >= 80 and percentage <= 90:
       return "B"
   elif percentage >= 70 and percentage <= 80:
       return "C"
   elif percentage >= 60 and percentage <=70:
       return "D"
   else:
       return "F"
    

assert computeGrade(90) == "A"
assert computeGrade("80") == ""
assert computeGrade(80) == "B"
assert computeGrade(79.9) == "C"
assert computeGrade(64) == "D"
assert computeGrade(60) == "D"
assert computeGrade(56) == "F"
assert computeGrade(101) == ""
assert computeGrade(-1) == ""
assert computeGrade(100) == "A"
assert computeGrade(0) == "F"

# Definition of a Book namedtuple object used for the following
# function below.
from collections import namedtuple

def updateBookPrice(percentIncrease, bookObject):
   ''' Function that takes in a namedtuple Book object (bookObject)
   and a positive float (percentIncrease), and returns a new namedtuple
   Book object with the same values of bookObject except the price
   is increased by percentIncrease (inflation is real!)
   '''
   new_price = bookObject.price * (1+percentIncrease)
   return Book(bookObject.title, bookObject.author, new_price)
Book = namedtuple("Book", ["title", "author", "price"])
b1 = Book("Title1", "Author1", 10)
b2 = Book("Title2", "Author2", 15)
b3 = Book("Title3", "Author3", 50)
assert updateBookPrice(0, b1) == Book("Title1", "Author1", 10)
assert updateBookPrice(0.2, b1) == Book("Title1", "Author1", 12)
assert updateBookPrice(1.1, b1) == Book("Title1", "Author1", 21)
assert updateBookPrice(0.1, b2) == Book("Title2", "Author2", 16.5)
assert updateBookPrice(0.5, b3) == Book("Title3", "Author3", 75)
