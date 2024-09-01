from math import degrees


def function1(arg1, arg2):
    floatVal = 0.0
    #correct Pep8 type checking
    if isinstance(arg1, float):
        floatVal = arg1    
    # Wrong
    # if (type(arg1) is float):
    #     floatVal = arg1
        
    return "Hello World! {a1} {a2} {f1}".format(a1=arg1,a2=arg2,f1=floatVal)

print(function1("test1", "test2"))
print(function1(float(1.0), "test2"))