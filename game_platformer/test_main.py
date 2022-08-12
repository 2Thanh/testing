# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
if __name__ == "__main__":
    score = 0
    
    n,m = input().split()
    n,m = int(n),int(m)
    
    n_list = numpy.input().split()
    for i in range(n):
        n_list[i] = int(n_list[i])
        
    A_list = numpy.input().split()
    for i in range(m):
        A_list[i] = int(A_list[i])

    B_list = numpy.input().split()
    for i in range(m):
        B_list[i] = int(B_list[i])

    
    for i in n_list:
        if i in A_list:
            score+=1
        elif i in B_list:
            score -=1

    print(score)