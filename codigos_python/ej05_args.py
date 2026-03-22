def sumar(*args):
    total =0
    for i in args:
        total = total+i
    print(total)


class Main():
    sumar(1,2,3)
    sumar(3,2)
#NO USAR ARGS
#USAR MULTIMETHOD
