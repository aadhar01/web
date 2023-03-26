#In python the function is just like any other value
#it can be passed this is called as the functional programming


def announce(f):
    def wrapper():
        print("about to run a function f")
        f()
        print("done with the function")
    return wrapper
        
@announce     
def hello():
    print("hello")


hello()
    
    