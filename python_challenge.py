############################################################
######### https://pythonprinciples.com/challenges/ #########
############################################################
""""
Capital indexes

Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters.

For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
"""

'''
def capital_indexes(a):
    index = 0
    list_cap = []
    for i in a:
        
        if i.isupper() == True:
            list_cap.append(index)
            
        index = index + 1
    return list_cap
    
print(capital_indexes("HeLlO"))
'''

'''
def capital_indexes(a):
    list_cap = []
    for i in range(len(a)):
        
        if a[i].isupper() == True:
            list_cap.append(i)
            
    return list_cap
    
print(capital_indexes("HeLlO"))
'''
###########################################################
###########################################################
###########################################################
"""
Middle letter

Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.

For example, mid("abc") should return "b" and mid("aaaa") should return "".
"""
'''
def mid(a):
    sol = ""
    if len(a) % 2 != 0:
        sol = a[int(len(a)/2)]
    return sol

print(mid("abc"))
'''
'''
# this approach uses // which is integer division in Python 3
# alternatively, use / and int() in combination.
def mid(string):
    if len(string) % 2 == 0:
        return ""
    return string[len(string)//2]
'''

###########################################################
###########################################################
###########################################################
"""
Online status

The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.

For example, consider the following dictionary:

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

In this case, the number of people online is 2.

Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.

Your function should return the number of people who are online.
"""
'''
statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

def online_count(a):
    onl = list(a.values()).count("online")
    return onl
'''
'''
# long version
def online_count(people):
    count = 0
    for person, status in people.items():
        if status == "online":
            count += 1
    return count

# short version
def online_count(people):
    return len([p for p in people if people[p] == "online"])
'''
###########################################################
###########################################################
###########################################################
"""
Randomness

Define a function, random_number, that takes no parameters. The function must generate a random integer between 1 and 100, both inclusive, and return it.

Calling the function multiple times should (usually) return different numbers.

For example, calling random_number() some times might first return 42, then 63, then 1.
"""

'''
import random
def random_number():
    return random.randint(1, 100)
'''
###########################################################
###########################################################
###########################################################
"""
Type check

Write a function named only_ints that takes two parameters. Your function should return True if both parameters are integers, and False otherwise.

For example, calling only_ints(1, 2) should return True, while calling only_ints("a", 1) should return False.
"""
'''
def only_ints(a, b):
    return type(a) == int and type(b) == int
'''
###########################################################
###########################################################
###########################################################

"""
Double letters

The goal of this challenge is to analyze a string to check if it contains two of the same letter in a row. For example, the string "hello" has l twice in a row, while the string "nono" does not have two identical letters in a row.

Define a function named double_letters that takes a single parameter. The parameter is a string. Your function must return True if there are two identical letters in a row in the string, and False otherwise.
"""

''' #ChatGPT
def double_letters(string):
    for i in range(len(string) - 1):
        if string[i] == string[i+1]:
            return True
    return False
'''
'''
# naive solution
def double_letters(string):
    for i in range(len(string) - 1):
        letter1 = string[i]
        letter2 = string[i+1]
        if letter1 == letter2:
            return True
    return False

# shorter solution
# using a list comprehension, zip, and any
def double_letters(string):
    return any([a == b for a, b in zip(string, string[1:])])
'''
###########################################################
###########################################################
###########################################################
"""
Adding and removing dots

Write a function named add_dots that takes a string and adds "." in between each letter. For example, calling add_dots("test") should return the string "t.e.s.t".

Then, below the add_dots function, write another function named remove_dots that removes all dots from a string. For example, calling remove_dots("t.e.s.t") should return "test".

If both functions are correct, calling remove_dots(add_dots(string)) should return back the original string for any string.

(You may assume that the input to add_dots does not itself contain any dots.)
"""
'''
def add_dots(a):
    return ".".join(list(a))

def remove_dots(b):
    return b.replace(".","")
'''

'''# the longer way
def add_dots(s):
    out = ""
    for letter in s:
        out += letter + "."
    return out[:-1]

def remove_dots(s):
    out = ""
    for letter in s:
        if letter != ".":
            out += letter
    return out


# the short way
def add_dots(s):
    return ".".join(s)

def remove_dots(s):
    return s.replace(".", "")
'''
###########################################################
###########################################################
###########################################################
"""
Counting syllables

Define a function named count that takes a single parameter. The parameter is a string. The string will contain a single word divided into syllables by hyphens, such as these:

"ho-tel"
"cat"
"met-a-phor"
"ter-min-a-tor"

Your function should count the number of syllables and return it.

For example, the call count("ho-tel") should return 2.
"""
'''
def count(a):
    return len(a.split("-"))
'''
'''
# naive solution
def count(word):
    syllables = 1
    for letter in word:
        if letter == "-":
            syllables = syllables + 1
    return syllables

# using the count method
def count(word):
    return word.count("-") + 1

# using split
def count(word):
    return len(word.split("-"))
'''
###########################################################
###########################################################
###########################################################
"""
Anagrams

Two strings are anagrams if you can make one from the other by rearranging the letters.

Write a function named is_anagram that takes two strings as its parameters. Your function should return True if the strings are anagrams, and False otherwise.

For example, the call is_anagram("typhoon", "opython") should return True while the call is_anagram("Alice", "Bob") should return False.
"""
'''
def is_anagram(a,b):
    return sorted(a) == sorted(b)
'''
'''
# harder solution:
# count how many times each letter appears in each string,
# and make sure all the counts are the same.
def count_letters(string):
    return {l: string.count(l) for l in string}
def is_anagram(string1, string2):
    return count_letters(string1) == count_letters(string2)
'''
###########################################################
###########################################################
###########################################################
"""
Flatten a list

Write a function that takes a list of lists and flattens it into a one-dimensional list.

Name your function flatten. It should take a single parameter and return a list.

For example, calling:

flatten([[1, 2], [3, 4]])

Should return the list:

[1, 2, 3, 4]
"""
'''
def flatten(a):
    b = []
    for i in a:
        b.extend(i)
    return b
'''
'''
# naive solution
def flatten(outer_list):
    result = []
    for inner_list in outer_list:
        for item in inner_list:
            result.append(item)
    return result

# solution with nested list comprehensions
# (can be put on a single line for conciseness)
def flatten(outer_list):
    return [
        item
        for inner_list in outer_list
        for item in inner_list
'''
###########################################################
###########################################################
###########################################################
"""
Min-maxing

Define a function named largest_difference that takes a list of numbers as its only parameter.

Your function should compute and return the difference between the largest and smallest number in the list.

For example, the call largest_difference([1, 2, 3]) should return 2 because 3 - 1 is 2.

You may assume that no numbers are smaller or larger than -100 and 100.
"""

'''
def largest_difference(a):
    return max(a) - min(a)
'''
'''
# naive solution
def largest_difference(numbers):
    smallest = 100
    for n in numbers:
        if n < smallest:
            smallest = n

    largest = -100
    for n in numbers:
        if n > largest:
            largest = n

    difference = largest - smallest
    return difference
'''
###########################################################
###########################################################
###########################################################
"""
Divisible by 3

Define a function named div_3 that returns True if its single integer parameter is divisible by 3 and False otherwise.

For example, div_3(6) is True because 6/3 does not leave any remainder. However div_3(5) is False because 5/3 leaves 2 as a remainder.
"""
'''
def div_3(a):
    return a % 3 == 0
'''
###########################################################
###########################################################
###########################################################
"""
Tic tac toe input

Here's the backstory for this challenge: imagine you're writing a tic-tac-toe game, where the board looks like this:

1:  X | O | X
   -----------
2:    |   |  
   -----------
3:  O |   |

    A   B  C

The board is represented as a 2D list:

board = [
    ["X", "O", "X"],
    [" ", " ", " "],
    ["O", " ", " "],
]

Imagine if your user enters "C1" and you need to see if there's an X or O in that cell on the board. To do so, you need to translate from the string "C1" to row 0 and column 2 so that you can check board[row][column].

Your task is to write a function that can translate from strings of length 2 to a tuple (row, column). Name your function get_row_col; it should take a single parameter which is a string of length 2 consisting of an uppercase letter and a digit.

For example, calling get_row_col("A3") should return the tuple (2, 0) because A3 corresponds to the row at index 2 and column at index 0in the board.
"""
'''
def get_row_col(a):
    a = a.replace("A","0").replace("B","1").replace("C","2")
    return (int(a[1])-1,int(a[0]))
'''
'''
def get_row_col(choice):
    translate = {"A": 0, "B": 1, "C": 2}
    letter = choice[0]
    number = choice[1]
    row = int(number) - 1
    column = translate[letter]
    return (row, column)
'''
###########################################################
###########################################################
###########################################################
"""
Palindrome

A string is a palindrome when it is the same when read backwards.

For example, the string "bob" is a palindrome. So is "abba". But the string "abcd" is not a palindrome, because "abcd" != "dcba".

Write a function named palindrome that takes a single string as its parameter. Your function should return True if the string is a palindrome, and False otherwise.
"""
'''
def palindrome(a):
    return a == a[::-1]
'''
'''
# iterative solution:
# keep chopping off the head and tail of the string,
# and compare the two. If they are not equal, it's
# not a palindrome. Stop when the string gets too short.
def palindrome(string):
    while len(string) > 1:
        head = string[0]
        tail = string[-1]
        string = string[1:-1]
        if head != tail:
            return False
    return True

# recursive solution: equivalent to the above.
def palindrome(string):
    if len(string) < 2:
        return True
    return string[0] == string[-1] and palindrome(string[1:-1])

# smarter solution:
# check if reversing the string gives the same string.
def palindrome(string):
    return string == string[::-1]
'''
###########################################################
###########################################################
###########################################################
"""
Up and down

Define a function named up_down that takes a single number as its parameter. Your function return a tuple containing two numbers; the first should be one lower than the parameter, and the second should be one higher.

For example, calling up_down(5) should return (4, 6).
"""
'''
def up_down(a):
    return (a-1,a+1)
'''
###########################################################
###########################################################
###########################################################
"""
Consecutive zeros

The goal of this challenge is to analyze a binary string consisting of only zeros and ones. Your code should find the biggest number of consecutive zeros in the string. For example, given the string:

"1001101000110"

The biggest number of consecutive zeros is 3.

Define a function named consecutive_zeros that takes a single parameter, which is the string of zeros and ones. Your function should return the number described above.
"""
'''
def consecutive_zeros(a):
    c = 0
    l_cero = [0]
    for i in  a:
        if i == '0':
            c = c + 1
            l_cero.append(c)
        elif i == '1':
            c = 0
    return max(l_cero)
'''
'''
# naive solution
def consecutive_zeros(bin_str):
    result = 0
    streak = 0
    for letter in bin_str:
        if letter == "0":
            streak += 1
        else:
            streak = 0
        result = max(result, streak)
    return result

# shorter solution
def consecutive_zeros(bin_str):
    return max([len(s) for s in bin_str.split("1")])
'''
###########################################################
###########################################################
###########################################################
"""
All equal

Define a function named all_equal that takes a list and checks whether all elements in the list are the same.

For example, calling all_equal([1, 1, 1]) should return True.
"""
'''
def all_equal(a):
    b = [i == a[0] for i in a]
    if False in b:
        return False
    else:
        return True
'''
'''
All equal

Define a function named all_equal that takes a list and checks whether all elements in the list are the same.

For example, calling all_equal([1, 1, 1]) should return True.
'''
###########################################################
###########################################################
###########################################################
"""
Boolean and

Define a function named triple_and that takes three parameters and returns True only if they are all True and False otherwise.
"""
'''
def triple_and(a,b,c):
    return a and b and c
'''
###########################################################
###########################################################
###########################################################
"""
Writing short code

Define a function named convert that takes a list of numbers as its only parameter and returns a list of each number converted to a string.

For example, the call convert([1, 2, 3]) should return ["1", "2", "3"].

What makes this tricky is that your function body must only contain a single line of code.
"""
'''
def convert(a):
    return list(map(str,a))
'''
'''
# using a list comprehension
def convert(ns):
    return [str(n) for n in ns]

# using map
def convert(ns):
    return list(map(str, ns))
'''
###########################################################
###########################################################
###########################################################
"""
Custom zip

The built-in zip function "zips" two lists. Write your own implementation of this function.

Define a function named zap. The function takes two parameters, a and b. These are lists.

Your function should return a list of tuples. Each tuple should contain one item from the a list and one from b.

You may assume a and b have equal lengths.

If you don't get it, think of a zipper.

For example:

zap(
    [0, 1, 2, 3],
    [5, 6, 7, 8]
)

Should return:

[(0, 5),
 (1, 6),
 (2, 7),
 (3, 8)]

"""
'''
def zap(a,b):
    c = []
    for i in range(len(a)):
        c.append((a[i],b[i]))
    return c
'''
'''
# ugly but understandable solution
def zap(a, b):
    result = []
    for i in range(len(a)):
        item_from_a = a[i]
        item_from_b = b[i]
        tup = (item_from_a, item_from_b)
        result.append(tup)
    return result

# concise solution with list comprehensions
def zap(a, b):
    return [(a[i], b[i]) for i in range(len(a))]
'''
###########################################################
###########################################################
###########################################################
"""
Solution validation

The aim of this challenge is to write code that can analyze code submissions. We'll simplify things a lot to not make this too hard.

Write a function named validate that takes code represented as a string as its only parameter.

Your function should check a few things:

    the code must contain the def keyword
        otherwise return "missing def"
    the code must contain the : symbol
        otherwise return "missing :"
    the code must contain ( and ) for the parameter list
        otherwise return "missing paren"
    the code must not contain ()
        otherwise return "missing param"
    the code must contain four spaces for indentation
        otherwise return "missing indent"
    the code must contain validate
        otherwise return "wrong name"
    the code must contain a return statement
        otherwise return "missing return"

If all these conditions are satisfied, your code should return True.

Here comes the twist: your solution must return True when validating itself.
"""
'''
def validate(a):
    if "def" not in a:
        return "missing def"
    elif ":" not in a:
        return "missing :"
    elif "(" not in a:
        return "missing paren"    
    elif ")" not in a:
        return "missing paren"
    elif "("+")" in a:
        return "missing param"
    elif "    " not in a:
        return "missing indent"
    elif "validate" not in a:
        return "wrong name"
    elif "return" not in a:
        return "missing return"
    else:
        return True
'''
'''
def validate(code):
    if "def" not in code:
        return "missing def"
    if ":" not in code:
        return "missing :"
    if "(" not in code or ")" not in code:
        return "missing paren"
    if "(" + ")" in code:
        return "missing param"
    if "    " not in code:
        return "missing indent"
    if "validate" not in code:
        return "wrong name"
    if "return" not in code:
        return "missing return"
    return True
'''
###########################################################
###########################################################
###########################################################
"""
List xor

Define a function named list_xor. Your function should take three parameters: n, list1 and list2.

Your function must return whether n is exclusively in list1 or list2.

In other words, if n is in both lists or in none of the lists, return False. If n is in only one of the lists, return True.

For example:

list_xor(1, [1, 2, 3], [4, 5, 6]) == True
list_xor(1, [0, 2, 3], [1, 5, 6]) == True
list_xor(1, [1, 2, 3], [1, 5, 6]) == False
list_xor(1, [0, 0, 0], [4, 5, 6]) == False
"""
'''
def list_xor(n,list1,list2):
    if (n in list1 and n not in list2) or (n in list2 and n not in list1):
        return True
    else:
        return False
'''
'''
# smart solution: uses the built-in xor operator ^
def list_xor(n, list1, list2):
    return (n in list1) ^ (n in list2)

# naive solution: check each case at a time
def list_xor(n, list1, list2):
    if n not in list1 and n not in list2:
        return False
    if n in list1 and n in list2:
        return False
    return True
'''
###########################################################
###########################################################
###########################################################
"""
Counting parameters

Define a function param_count that takes a variable number of parameters. The function should return the number of arguments it was called with.

For example, param_count() should return 0, while param_count(2, 3, 4) should return 3.
"""
'''
def param_count(*a):
    return len(a)
'''
###########################################################
###########################################################
###########################################################
"""
Thousands separator

Write a function named format_number that takes a non-negative number as its only parameter.

Your function should convert the number to a string and add commas as a thousands separator.

For example, calling format_number(1000000) should return "1,000,000".
"""
'''###********** No esta del todo bien**********###
def format_number(a):
    l = list(str(a))[::-1]
    k = len(l)
    print(k)
    for i in range(3,k+1,4):
        print(i)
        l.insert(i,",")
    return "".join(l)[::-1]
print(format_number(1000000000))
'''
'''
# DIY solution
def format_number(n):
    result = ""
    for i, digit in enumerate(reversed(str(n))):
        if i != 0 and (i % 3) == 0:
            result += ","
        result += digit
    return result[::-1]

# built-in solution
def format_number(n):
    return "{:,}".format(n)
'''