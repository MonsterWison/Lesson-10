print("case 1")
if 0 :
    print("Hello World")
elif 1 :
    print("second ture")
else:
    print("false")
print("out of if condition")

print("case 2")
if [] :
    print("Hello World")
elif 1 :
    print("second ture")
else:
    print("false")
print("out of if condition")

print("case 3")
if [1] :
    print("Hello World")
elif 1 :
    print("second ture")
else:
    print("false")
print("out of if condition")

print("case 4")
if [0] :
    print("Hello World")
elif 1 :
    print("second ture")
else:
    print("false")
print("out of if condition")

print("case 5")
def a():
    print("Hello") #沒call function，所以結果是沒東西
    
# print("case 6")
# def a(x):
#     # x =
#     print ("hello")
# a() #Type Error

# print("case 7")
# def a(x):
#     # x =
#     print ("hello")
# x =  #invalid syntax

# print("case 8")
# def a():
#      = 1
#     print("hello")
# a() #Type Error

print("case 8")
def a(x=1):
    x = 1
    x = 2
    print("hello")
a(2)

print("case 9")
def a(x):
    x = 1
    x = 2
    print("hello")
a(2)

print("case 10")
def a(x):
    x = 1 #少了 x = 1，所以x = 2
    x = 2
    print("hello")
a(x=2)

print("case 11")
if 10 + 1 == 11:
    print("hello")
else :
    print("false") #https://www.w3schools.com/python/python_operators.asp 查看權限權重
# + 權限大於 ==，所以先計算10 + 1，再判斷是否等於11

print("case 12")
if not 1 == 11:
    print("hello")
else :
    print("false") #https://www.w3schools.com/python/python_operators.asp 查看權限權重
#先執行not 1 == 11，結果是True，所以print("hello")

# print("case 13")
# if 1 == not 11:
#     print("hello")
# else :
#     print("false")
#因==權限大於not，所以先執行1 == 11，結果是False，再執行not，結果Syntax Error

print("case 14")
y = 6
x = (y !=10)
print(x) #因為y != 10，所以x = True