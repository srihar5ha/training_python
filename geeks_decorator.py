# Adds a welcome message to the string
# returned by fun(). Takes fun() as
# parameter and returns welcome().
def decorate_message(fun):
 
    # Nested function
    def addWelcome(a,b):
        print("inside addwelcom")
        return a-b + fun(a,b)
    print("outside add welcom")
    # Decorator returns a function
    return addWelcome
 
@decorate_message
def site(a,b):
    print("inside site")
    return a+b
 
# Driver code
 
# This call is equivalent to call to
# decorate_message() with function
# site("GeeksforGeeks") as parameter
print (site(2,6))
