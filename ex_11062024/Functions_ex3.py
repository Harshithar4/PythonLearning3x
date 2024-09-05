def outer_func():
    a=10
    print("outer")
    def inner_func():
        print("inner")
        print(a)

    inner_func()

outer_func()