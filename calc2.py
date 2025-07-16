#承接Lesson-9，加入input function 及input 空白為error
print("Lesson-10")
print("version 1-1")

def check_num(num):
    try:
        return float(num)
    except ValueError:
        print(f"input error " + str(num))
        exit() #此處check到有error便不再繼續執行
def check_op(operator):
    if operator in ['+', '-', '*', '/']:
        return True
    else:
        print("Wrong operator")
        return False
    
def calc(a,b,op):
    result = 0
    a = check_num(a)
    b = check_num(b)
    if check_op(op):
        if op == '+':
            result = a + b
        if op == '-':
            result = a - b
        if op == '*':
            result = a * b
        if op == '/':
            if b == 0:
                print('** b can not be zero **') #捉b不能等於零
            else :
                result = a / b
        return result

result = 0
exp = input("Please input your expression with spacing for calculation:") #輸入表達式
if " " not in exp: #檢查是否包含空格
    print("Input must contain spaces between numbers and operators.")
    exit()

exp = exp.split() #將表達式分割成list
print(exp) #印出list

if len(exp) % 2 !=1:
    print("Wrong expression length")
else :
    while (len(exp) >= 3 and len(exp) % 2):
        a = exp[0]
        b = exp[2]
        op = exp[1]
        result = calc(a,b,op)
        del exp[:2]
        exp[0] = result
        print(exp)
        
print("expression result is :" + str(result))