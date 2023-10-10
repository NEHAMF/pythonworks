# to reduce redundancy
def swap_nums(fn):
    def wrapper(n1,n2):
        if(n1<n2):
            (n1,n2)=(n2,n1)
        return fn(n1,n2)
    return wrapper
def smart_div(fn):
    def inner_fn(n1,n2):
        if n2==0:
            print("/ by zero nop")
            return
        return fn(n1,n2)
    return inner_fn

@swap_nums
def sub(n1,n2):
    return n1-n2
@swap_nums
@smart_div
def div(n1,n2):
    return n1/n2
print(sub(5,10))
print(div(0,8)) 
# 14
# 16 last decorator program
