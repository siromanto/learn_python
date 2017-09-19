one = 0b1
two = 0b10
three = 0b11
four = 0b100
five = 0b101
six = 0b110
seven = 0b111
eight = 0b1000
nine = 0b1001
ten = 0b1010
eleven = 0b1011
twelve = 0b110

A BIT of This AND That
a:   00101010   42
     b:   00001111   15       
===================
 a & b:   00001010   10

0 & 0 = 0
0 & 1 = 0
1 & 0 = 0
1 & 1 = 1

 print bin(0b1110 & 0b101)

A BIT of This OR That
 a:  00101010  42
    b:  00001111  15       
================
a | b:  00101111  47

0 | 0 = 0
0 | 1 = 1 
1 | 0 = 1
1 | 1 = 1

print bin(0b1110 | 0b101)

This XOR That?
a:  00101010   42
    b:  00001111   15       
================
a ^ b:  00100101   37

0 ^ 0 = 0
0 ^ 1 = 1
1 ^ 0 = 1
1 ^ 1 = 0

print bin(0b1110 ^ 0b101)

print ~1
print ~2
print ~3
print ~42
print ~123

def check_bit4(input):
  mask = 0b1000
  result = input & mask
  if result > 0:
    return "on"
  else:
    return "off"


"""
  Use a bitmask and the value a in order to achieve a result
  where the third bit from the right of a is turned on.
"""

a = 0b10111011
mask = 0b100

print bin(a | mask)

Use a bitmask and the value a in order to achieve a result where all of the bits in a are flipped. Be sure to print your answer as a bin() string!

a = 0b11101110
mask = 0b11111111

print bin(a ^ mask)

Flip the nth bit (with the ones bit being the first bit) and store it in result.

def flip_bit(number, n):
  flip_bit = 0b1 << n-1
  print bin(flip_bit)
  result = number ^ 
  return bin(result)