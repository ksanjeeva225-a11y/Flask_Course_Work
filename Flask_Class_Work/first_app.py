from flask import Flask

x=Flask(__name__)

@x.route("/")
def fn_wish():
    return"hello guys how are you"

@x.route("/function2")
def fn_2():
    return"this is a function no-2"

def fn_3():
    return"this is function 3"

x.add_url_rule("/fn3", "abcd", fn_3)
x.add_url_rule("/fn2", "mnbv", fn_2)

x.add_url_rule("/fn3", "dfgh", fn_wish)

if __name__=="__main__": 
    x.run(debug=True)

