

n = [1,2,3]
for i in n:
    if i == min(n):
        print(f"smallest number: {i}")


from collections import Counter

def double(s):
    return [char for char, count in Counter(s).items() if count > 1]
s='linuxi'
print(double(s))

def doubl(s1):
    return [word for word, count in Counter(s1).items() if count > 1]
s1 = ["linux", "unix", "unix", "ubuntu"]
print(doubl(s1))


def uniqe(u):
    return [word for word, count in Counter(s).items() if count == 1]

s = ["linux", "unix", "unix", "ubuntu"]
print(uniqe(s))


def swap(a, b):
    return b, a

a = 'virat'
b = 'kohli'

a, b = swap(a, b)
print(a, b)

a = "kohlivirat"
b = a[::-1]
print(b)

n = 5

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
print(fact(n))


fibo = [0,1]
for i in range(5):
    fibo.append(fibo[-1]+fibo[-2])
print(fibo)


def d(n):
    return bin(n).replace("0b", "")
if __name__ == '__main__':
    print(d(5))



def b(n):
    return int(n,2)
if __name__ == '__main__':
    print(b('100'))
    

