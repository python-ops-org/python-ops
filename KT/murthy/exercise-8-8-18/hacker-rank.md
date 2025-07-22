```


    n = 5
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

```

try:
    n = 5

    if not isinstance(n, int):
        raise ValueError("Input must be an integer")

    if n % 2 != 0:
        print("Weird")
    else:
        if n in range(2, 6):
            print("Not Weird")
        elif n in range(6, 21):
            print("Weird")
        elif n > 20:
            print("Not Weird")

except Exception as e:
    print(f"An error occurred: {e}")

```
