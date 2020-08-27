'''ex1'''
a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))    #print('{} + {} = {}'.format(a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))


'''ex2'''
a = 10
b = 3
a += b        # a = a + b
a *= a + 2    # a = a * (a + 2)
print(a) 


'''ex3'''
flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not (1 != 2)
print('flag0 =', flag0)    # flag0 = True
print('flag1 =', flag1)    # flag1 = True
print('flag2 =', flag2)    # flag2 = False
print('flag3 =', flag3)    # flag3 = False
print('flag4 =', flag4)    # flag4 = True
print('flag5 =', flag5)    # flag5 = False


'''exe1'''
f = float(input('f:'))
c = (f - 32) / 1.8
print('%.1fFahrenheit = %.1fCelsius' % (f, c))


'''exe2'''
radius = float(input('r:'))
perimeter = 2 * 3.1416 * radius
area = 3.1416 * radius * radius
print('perimeter: %.2f' % perimeter)
print('area: %.2f' % area)


'''exe3'''
year = int(input('year: '))
is_leap = year % 4 == 0 and year % 100 != 0 or \
          year % 400 == 0
print(is_leap)