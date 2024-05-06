# -*- coding: utf-8 -*-
"""
Created on Mon May  6 14:37:50 2024

@author: ABrown
"""

# Fun with strings

print("""\
      
      Usage thingy omg
      -h-g                 Display with here
      fdsj)
    """)
    
3*'un'+'ium'

word= 'Python'

word[0]
word[5]

word[-1]    #Negative indices start from -1

word[0:2]
word[2:5]

word[:2]

word[4:]

word[-2:]

# +---+---+---+---+---+---+
# | P | y | t | h | o | n |
# +---+---+---+---+---+---+
# 0   1   2   3   4   5   6
#-6  -5  -4  -3  -2  -1

'J' + word[1:]

s='thisisasuperlongstringplasdiwfiubweifbwieubfwie'
len(s)

squares = [1,4,9,16,25]

squares + [36, 49, 65, 65, 65]

cubes = [1,8,27,65,125]
4**3
cubes[3]=64

cubes.append(216)

squares[0:2]=[]

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]

a,b=0,1


    