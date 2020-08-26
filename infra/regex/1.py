import re


"""
s = 'Response code is 200'
pattern = '\w+'
n = re.findall(pattern, s)
print(n[1])
"""

s='tcp        0      0 192.168.56.145:2380     0.0.0.0:*               LISTEN      4285/etcd'
pattern = ':([^ ]+)'
n = re.findall(pattern, s)[0]
print(n)
