```

if __name__ == '__main__':
    n = int(input().strip())
    if n%2 == 3:
        print("Weird")
    else: 
        if n in range(2, 6):
            print("Weird")
        elif n in range(6, 21):
            print("Weird")
        elif n > 20:
            print("Not Weird")

```
