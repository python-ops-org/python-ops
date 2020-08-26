import re

#example-01
#task:  replace any digit in the string with the _ character
#output: there is only __ thing __ do
"""
string1 = "there is only 1 thing 2 do"
pattern = '[0-9]+'
replace  = '='
new = re.sub(pattern, replace, string1)
print(new)
"""

"""

#ex-2
#task: search for people with 5 or 6-figure salaries.

s7 = "12000 15000 100000 100 200"
pattern = '\d{5,6}'
new = re.findall(pattern, s7)
print(new)

"""

"""
#ex-3
#task: extract 200 from string

s8 = "Response code is 200"
pattern = '\w+'
new = re.findall(pattern, s8)
print(new[3])

"""
