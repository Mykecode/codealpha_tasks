def fibonacci_generator(num = None):       #helper function to generate fibonacci sequence

    a = 0 # first term of a fibonacci series
    
    b = 1 # second term of a fibonacci series
    
    count = 1 #a counter
    
    while num is None or count < num:
          yield a # At every loop,  the value of a is given out. This helps in memory management
          
          a, b = b, a+b # values are assigned to variables
          
          count += 1 # increament the counter by 1 for every time the loop runs
          
          
def main():
    
    fib = fibonacci_generator(10)
    
    for num in fib:
        print(num, end=' ')
      
    fib = fibonacci_generator()  
    for num in fib:
        if num > 100:
            break
        print(num, end=' ')
        
if __name__ == '__main()__':
    main()
    
    
main()