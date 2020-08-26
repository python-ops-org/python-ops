##https://scotch.io/tutorials/an-introduction-to-regex-in-python
#w = Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
#/s = Returns a match where the string contains a white space character
#+ = One or more occurrences
#[^...] = Matches any single character not in brackets
#[...] = Matches any single character in brackets.
#(?= re)Specifies position using a pattern. Doesn't have a range.
#(?: re)Groups regular expressions without remembering matched text.
#(?! re)Specifies position using pattern negation. Doesn't have a range.
#(?> re)Matches independent pattern without backtracking.
#[^0-9]Match anything other than a digit
#[0-9]	Returns a match for any digit between 0 and 9
#\d=Returns a match where the string contains digits (numbers from 0-9)	"\d"	
#\D=Returns a match where the string DOES NOT contain digits
#{}=Exactly the specified number of occurrences
#*=Zero or more occurrences	"aix*"	
#+=One or more occurrences
#.=Any character (except newline character)
#[]=A set of characters



import re

"""
#example-01
#task:  replace any digit in the string with the _ character
#output: there is only __ thing __ do   
string1="there is only 1 thing 2 do"
pattern='[0-9]+'
replace='__'
new=re.sub(pattern, replace, string1)
print(new)
"""

"""
#example-02
#task: replace the words in the s2 with the word "regex"
#output: regex regex regex regex    
string2="Lorem ipsum with steroids"
pattern='\w+'
replace='regex'
new=re.sub(pattern, replace, string2)
print(new)
"""

"""
#example-03
#task: Instead of matching from the start of the string, match an entity that's followed by the pattern
#output: The
string3="The quick brown fox"
#w = Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
#/s = Returns a match where the string contains a white space character
#(?= re)Specifies position using a pattern. Doesn't have a range.
pattern='\w+(?=\squick)'
new=re.search(pattern, string3)
print(new.group())

"""


"""

#example-04
#task: match all instances of characters that is followed by a comma
#output: [ 'Me', 'myself' ]
string4="Me, myself, and I"
pattern='\w+(?=,)'
new=re.findall(pattern, string4)
print(new)
"""

"""
#example-05
#task: we want to include a +(a reserved quantifier) in a string to be matched by a pattern
#output: file
string5="file+"
pattern='\w+'
new=re.search(pattern, string5)
print(new.group())

"""



"""
#example-06
#task: monetizes a number using thousands separator commas.
#output: 1,234,568
string6="1234568"
pattern='\d{1,3}(?=(\d{3})+(?!\d))'
replace='\g<0>,'
new=re.sub(pattern, replace , string6)
print(new)
"""



"""

#example-07
#task: search for people with 5 or 6-figure salaries.
#output: 12000 15000 10000
string7="12000 15000 10000 1000 200"
pattern='\d{5,6}'
new=re.findall(pattern , string7)
print(new)
"""




"""
#example-08
#task: extract 200 from string
#output: 200
string8="Respone Code is 200"
pattern='\w+'
new=re.findall(pattern, string8)
print(new[3])

"""




"""
#example-09
#task: splits a string into a list delimited by the passed pattern.
#output: ['Jane Doe', 'Jane Doe', 'Jin Du', 'Chin Doe']
s9 = "John Doe Chin Doe"

p=re.compile(r"\n+")
r=p.split(s9)
print(r)

"""
"""
#example-10
#task: grep dreamer keyword
#output: dream
string10="\n dreamer"
pattern='\w+'
new=re.search(pattern, string10)
print(new.group())

"""

#example-11
#task: [^\s$] or just [^\s] will tell regex to match anything 
#that is not a whitespace character. [^ ... ] it means not
#output: dance
"""
string11="dance more"
pattern='[^\d+]'
new=re.search(pattern, string11)
print(new)
"""
"""

#example-12
#task: 
#output:
string12="007 James Bond"
pattern='\d{1,}'
new=re.match(pattern, string12)
print(new.group())
"""







