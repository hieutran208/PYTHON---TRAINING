def variable_Example(a,b,*args,**kwargs):
    print(a)
    print(b)
    for arg in args:
        print(arg)
    for kwarg_key, kwang_value in kwargs.items():
        print(kwarg_key, kwang_value)
if __name__ == "__main__":
    variable_Example('a','b','Tran Trung Hieu','2001',name="Hieu",age=22)
    
    