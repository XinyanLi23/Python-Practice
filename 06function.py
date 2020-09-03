"""ex1 输入M和N计算C(M,N)"""
m = int(input('m= '))
n = int(input('n= '))
fm = 1
for num in range(1, m+1):
    fm *= num
fn = 1
for num in range(1, n+1):
    fn *= num
fm_n = 1
for num in range(1, m-n+1):
    fm_n *= num
print(fm // fn // fm_n)



"""set function"""
def fac(num):
    result = 1
    for n in range(1, num+1):
        result *= n
m = int(input('m= '))
n = int(input('n= '))
print(fac(m) // fac(n) // fac(m-n))



"""ex2 use function"""
from random import randint
def roll_dice(n=2):
    total = 0
    for _ in range(n):
        total += randint(1,6)
    return total

def add(a=0, b=0, c=0): 
      return a + b + c


print(roll_dice())   ### 2 rolls
print(roll_dice(3))  ### 3 rolls



"""variable parameter
def add(*args):
    total = 0
    for val in args:
        total += val
    return total
"""



"""distinguish module
module1.py
def foo():
    print('hello, world!')
module2.py
def foo():
    print('goodbye, world!')

test.py
from module1 import foo
# 输出hello, world!
foo()
from module2 import foo
# 输出goodbye, world!
foo()

or

test.py
import module1 as m1
import module2 as m2
m1.foo()
m2.foo()
"""



"""ex1 greatest common diviser & lease common multiple"""
def gcd(x,y):
    (x,y) = (y,x) if x > y else (y,x)
    for factor in range(x,0,-1):
        if x % factor == 0 and y % factor == 0:
            return factor

def lcm(x,y):
    return x * y // gcd(x,y)

num1 = int(input("x= "))
num2 = int(input("y= "))
gcd_f = gcd(num1, num2)
lcm_f = lcm(num1, num2)
print("greatest common diviser: %d" % gcd_f)
print("lease common multiple: %d" % lcm_f)



"""ex2 Palindromic number"""
def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num
x = is_palindrome(int(input('x= ')))
print("Is Palindrom: %s" % x)




"""ex3 Prime number"""
def is_prime(num):
    for factor in range(2, int(num ** 0.5) + 1):
        if num % factor == 0:
            return False
    return True if num != 1 else False
x = is_prime(int(input('x= ')))
print("Is Prime: %s" % x)



"""positive integer - Palindromic number"""
if __name__ == '__main__':
    num = int(input('请输入正整数: '))
    if is_palindrome(num) and is_prime(num):
        print('%d是回文素数' % num)

