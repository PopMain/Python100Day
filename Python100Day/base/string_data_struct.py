

#string
#def println():
#    print('\n')

def println(str=''):
    print(str)
    print('\n')

def printDivider():
    divider = ''
    println(divider.rjust(100, '#'))

s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'
print(s1, s2, end='')
println()
s1 = 'hello'* 3
print(s1)
s2 = 'world'
println()
s1 += s2
print(s1)
println()
print('ll' in s1)
println()
print('good' in s1)
println()

printDivider()

str = 'abc123456'
# 从字符串中取出指定位置的字符(下标运算)
print(str[2]) #c
# 字符串切片(从指定的开始索引到指定的结束索引)
println()
print(str[2:]) #c123456
println()
print(str[2:5]) #c12
println()
print(str[2::2])  #c246
println()
print(str[::2]) #ac246
println()
print(str[::-1]) #654321cba
println()
print(str[-3::-1]) #4321cba

printDivider()

str1 = 'hello world!'
# 通过内置函数len计算字符串的长度
println('len=%d'% len(str1))
# 获得字符串首字母大写的拷贝
println('capitalize=%s' % str1.capitalize())
# 获得字符串每个单词首字母大写的拷贝
println('title=%s'% str1.title())
# 获得字符串变大写后的拷贝
println(str1.upper())
# 从字符串中查找子串所在位置
println(str1.find('or'))
println(str1.find('shit'))
# 与find类似但找不到子串时会引发异常
#println(str1.index('or'))
#println(str1.index('shit'))
# 检查字符串是否以指定的字符串开头
println(str1.startswith('He'))
println(str1.startswith('hel'))
# 检查字符串是否以指定的字符串结尾
println(str1.endswith('!'))
# 将字符串以指定的宽度居中并在两侧填充指定的字符
println(str1.center(50, '*'))
# 将字符串以指定的宽度靠右放置左侧填充指定的字符
println(str1.rjust(50, ' '))
str2 = 'abc123456'
# 检查字符串是否由数字构成
println('isdigit=%r' % str2.isdigit())
# 检查字符串是否以字母构成
println('isalpha=%r' % str2.isalpha())
# 检查字符串是否以数字和字母构成
println('isalnum=%r' % str2.isalnum())
str3 = '  popmain@gmail.com'
println(str3)
# 获得字符串修剪左右两侧空格之后的拷贝
println(str3.strip())
a, b = 5, 10
print('%d * %d = %d' % (a, b, a * b))
print('{0} * {1} = {2}'.format(a, b, a * b))

printDivider()

#list
list1 = [1, 2, 3, 4, 5, 6]

println(list1)

list2 = ['hello'] * 3

println(list2)

println(len(list1))

println(list1[0])

println(list1[-1])

println(list1[-3])

list1[2] = 300

println(list1)

for index in range(len(list1)):
    print(list1[index])

for elem in list1:
    print(elem)

for index, elem in enumerate(list1):
    print(index, elem)


printDivider()

list1 = [1,3,5, 7,100]

list1.append(200)
list1.insert(1, 400)
print(list1)

list1 += [10000, 20000]

print(list1)

if 3 in list1:
    list1.remove(3)

if 1234 in list1:
    list1.remove(1234)

print(list1)

list1.pop(0)
print(list1)

list1.pop(len(list1) - 1)
print(list1)

list1.clear()
print(list1)

printDivider()

fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
print(fruits)
fruits2 = fruits[1:4]
print(fruits2)
# 可以通过完整切片操作来复制列表
fruits3 = fruits[:]
print(fruits3)

fruits4 = fruits[-3:-1]
print(fruits4)

fruits5 = fruits[::-1]
print(fruits5)

printDivider()

list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list1)
# sorted函数返回列表排序后的拷贝不会修改传入的列表
# 函数的设计就应该像sorted函数一样尽可能不产生副作用
list3 = sorted(list1, reverse=True)
# 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
list4 = sorted(list1, key=len)
print(list1)
print(list2)
print(list3)
print(list4)
# 给列表对象发出排序消息直接在列表对象上进行排序
list1.sort(reverse=True)
print(list1)

printDivider()