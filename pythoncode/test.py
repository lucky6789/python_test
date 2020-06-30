#有参数有返回值
def fun1(arg):
    arg = arg
    print("有返回值")
    return arg

#无参数无返回值，无返回值默认返回None
def fun2():
    print("无返回值")

if __name__  == "__main__":
    print(fun1("a"))
    print(fun2())