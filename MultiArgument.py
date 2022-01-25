def addall(*arguments):
    result=0
    for number in arguments:
        result+=number
    return result

# function definition
def displayArgument(**arguments): 
    for arg in arguments.items():
        print(arg)
        
        
print(addall(3,5,7,1,2))
displayArgument(arg1='great')