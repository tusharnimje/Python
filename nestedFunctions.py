#Function inside function
def outerFunction(text):  
    text = text  
    
    def innerFunction(): 
       nonlocal text
        text = text.upper() #cannot edit directly nonlocal variable. Need previous line
        print(text)  
    
    innerFunction()  
    
if __name__ == '__main__':  
    outerFunction('Hey !')
