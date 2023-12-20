from math import factorial
def pascal_triangle(n):
    # YOUR CODE HERE 
    for i in range(n):
        # for j in range(n-i+1):
    
        #     # for left spacing
        #     print(end=" ")
    
        for j in range(i+1):
    
            # nCr = n!/((n-r)!*r!)
            print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
    
        # for new line
        print()
        
pascal_triangle(5)