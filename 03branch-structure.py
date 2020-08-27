'''ex1'''
username = input('username: ')
password = input('password: ')
if username == 'admin' and password == '123456':
    print('身份验证成功!')
else:
    print('身份验证失败!')



'''ex2

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
'''
x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))



"""ex3
		3x - 5	(x > 1)
f(x) =	x + 2	(-1 <= x <= 1)
		5x + 3	(x < -1)
"""
x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
else:
    if x >= -1:
        y = x + 2
    else:
        y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))



'''exe1'''
"""
英制单位英寸和公制单位厘米互换
"""
value = float(input('value = '))
unit = (input('unit = '))
if unit == 'inch':
    print('%finch = %fcm' % (value, value * 2.54))
elif unit== 'cm':
    print('%fcm = %finch' % (value, value / 2.54))
else:
    print('请输入有效的单位')



'''exe2'''
"""
百分制成绩转换为等级制成绩

"""
score = float(input('score: '))
if score >= 90:
    print('%s' % ('A'))
elif score >= 80:
    print('%s' % ('B'))
elif score >= 70:
    print('%s' % ('C'))
elif score >= 60:
    print('%s' % ('D'))
else:
    print('%s' % ('E'))




"""exe3
判断输入的边长能否构成三角形，如果能则计算出三角形的周长和面积

"""
x = float(input('sidex: '))
y = float(input('sidey: '))
z = float(input('sidez: '))
if x + y > z or x + z > y or y + z > x:
    perimeter = x + y + z 
    area = ((perimeter/2) * (perimeter/2-x) * (perimeter/2-y) * (perimeter/2-z)) ** 0.5
    print('perimeter=%.2f, area=%.2f' % (perimeter, area))
else:
    print('请输入有效的边长')