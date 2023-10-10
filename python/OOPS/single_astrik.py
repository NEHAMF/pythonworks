# variable length argument method
# def product(*args):#tuple format any number of parameters
#     res=1
#     for n in args:
#         res*=n
#     print(res)
# product(2,3,5,6)
# product(4,9,10)   

# def greetings(**kwargs):dictionary format
#     print(f"hello {kwargs.get('msg')} app user {kwargs.get('user_name')}")
# greetings(msg="good morning",user_name="neha")

def dispatch_order(**kwargs):#DICTIONARY FORMAT
    print(f"hello user {kwargs.get('name')} your order {kwargs.get('code')} {kwargs.get('item')} is ready to {kwargs.get('status')} ")
dispatch_order(item="ucb shirt",code="123abc",status="deliver",name="vijay")    