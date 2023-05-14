try:
    a = int(input("输入被除数："))
    b = int(input("输入除数："))
    c = a / b
    print(f"你输入的两个数相除的结果是: {c}")
except(ValueError, ArithmeticError) as e:
    print(e)
    print("程序发生了数字格式异常算数异常")
except:
    print("未知异常")
print("程序继续执行")
