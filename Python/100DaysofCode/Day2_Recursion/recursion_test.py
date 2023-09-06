def fun_1():
    print("Function1 is called")
    fun_2()

def fun_2():
    print("Function 2 is called")
    fun_1()

fun_1()