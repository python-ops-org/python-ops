n=5
for i in range(1, 6):
    print(' '*n, end='')
    print('* '*(i))
    n-=1  



for i in range(1,5):
    for j in range(i):
        print("* ", end="")
    print()


    
 for i in range(1, 6):
  print (' ' * (5 - i), '* ' * i)

def pattern(n):
      k = 2 * n - 2
      for i in range(0,n):
           for j in range(0,k):
               print(end=" ")
           k = k - 1
           for j in range(0, i+1):
                print("*", end=" ")
           print("\r")
 
pattern(5)
