global_var=10# global variables can be used in outer func and inner func.
def f1():
    print(global_var)
    def f2():
        print(global_var)
    f2()

f1()