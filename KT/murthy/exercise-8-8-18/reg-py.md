

```
 normal="Hello"
 print (normal)

 raw=r"Hello"
 print (raw)

 normal="Hello\nWorld"
 print (normal)

```


```

import re
line = "Cats are smarter than dogs"
matchObj = re.match( r'Cats', line)
print (matchObj.start(), matchObj.end())
print ("matchObj.group() : ", matchObj.group())

```

match checks for a match only at the beginning of the string, while search checks for a match anywhere in the string



```
import re
line = "Cats are smarter than dogs"
matchObj = re.search( r'than', line)
print (matchObj.start(), matchObj.end())
print ("matchObj.group() : ", matchObj.group())

```

```
import re
line = "Cats are smarter than dogs";
matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
   print ("match --> matchObj.group() : ", matchObj.group())
else:
   print ("No match!!")

```

```

searchObj = re.search( r'dogs', line, re.M|re.I)
if searchObj:
   print ("search --> searchObj.group() : ", searchObj.group())
else:
   print ("Nothing found!!")

```

```
import re
string="Simple is better than complex."
obj=re.findall(r"ple", string)
print (obj)

```


The findall() function returns all non-overlapping matches of pattern in string, as a list of strings or tuples

```

import re
string="Simple is better than complex."
obj=re.findall(r"\w*", string)
print (obj)

```

```

import re
phone = "2004-959-559 # This is Phone Number"

# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print ("Phone Num : ", num)

# Remove anything other than digits
num = re.sub(r'\D', "", phone)
print ("Phone Num : ", num)


```
sub() function to substitute all occurrences of is with was word

```

import re
string="Simple is better than complex. Complex is better than complicated."
obj=re.sub(r'is', r'was',string)
print (obj)

```

```

import re
text = "He was carefully disguised but captured quickly by police."
obj = re.findall(r"\w+ly\b", text)
print (obj)

```

```
import re
text = 'Errors should never pass silently. Unless explicitly silenced.'
obj=re.findall(r'\b[aeiouAEIOU]\w+', text)
print (obj)

```

```
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

```

```
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

```

The split() function returns a list where the string has been split at each match

```
import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

```


```
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())

```
"[a-m]" : A set of characters

```
import re

txt = "The rain in Spain"

#Find all lower case characters alphabetically between "a" and "m":

x = re.findall("[a-m]", txt)
print(x)

```

"\d": Signals a special sequence 


```
import re

txt = "That will be 59 dollars"

#Find all digit characters:

x = re.findall("\d", txt)
print(x)


```
"he..o": Any character (except newline character)	

```

import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

x = re.findall("he..o", txt)
print(x)

```

"^hello": Starts with	


```
import re

txt = "hello planet"

#Check if the string starts with 'hello':

x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")


```
"planet$": Ends with


```
import re

txt = "hello planet"

#Check if the string ends with 'planet':

x = re.findall("planet$", txt)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")

```

"he.*o": Zero or more occurrences



```
import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":

x = re.findall("he.*o", txt)

print(x)

```

+: One or more occurrences



```
import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":

x = re.findall("he.+o", txt)

print(x)

```
?: Zero or one occurrences



```

import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":

x = re.findall("he.?o", txt)

print(x)

#This time we got no match, because there were not zero, not one, but two characters between "he" and the "o"


```





{},"he.{2}o": Exactly the specified number of occurrences


```

import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":

x = re.findall("he.{2}o", txt)

print(x)

```


"falls|stays": Either or

```

import re

txt = "The rain in Spain falls mainly in the plain!"

#Check if the string contains either "falls" or "stays":

x = re.findall("falls|stays", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


```







\A Returns a match if the specified characters are at the beginning of the string

```
import re

txt = "The rain in Spain"

#Check if the string starts with "The":

x = re.findall("\AThe", txt)

print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")

```

\b Returns a match where the specified characters are at the beginning or at the end of a word

```
import re

txt = "The rain in Spain"

#Check if "ain" is present at the beginning of a WORD:

x = re.findall(r"\bain", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

```

\B Returns a match where the specified characters are present, but NOT at the beginning

```
import re

txt = "The rain in Spain"

#Check if "ain" is present, but NOT at the beginning of a word:

x = re.findall(r"\Bain", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


```

\d Returns a match where the string contains digits (numbers from 0-9)


```
import re

txt = "The rain in Spain"

#Check if the string contains any digits (numbers from 0-9):

x = re.findall("\d", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


```
\D Returns a match where the string DOES NOT contain digits 

```
import re

txt = "The rain in Spain"

#Return a match at every no-digit character:

x = re.findall("\D", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

```

\s Returns a match where the string contains a white space character

```

import re

txt = "The rain in Spain"

#Return a match at every white-space character:

x = re.findall("\s", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


```

\S Returns a match where the string DOES NOT contain a white space character

```
import re

txt = "The rain in Spain"

#Return a match at every NON white-space character:

x = re.findall("\S", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


```

\w Returns a match where the string contains any word characters

```

import re

txt = "The rain in Spain"

#Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):

x = re.findall("\w", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

```

\W Returns a match where the string DOES NOT contain any word characters

```
import re

txt = "The rain in Spain"

#Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):

x = re.findall("\W", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

```

\Z Returns a match if the specified characters are at the end of the string

```

import re

txt = "The rain in Spain"

#Check if the string ends with "Spain":

x = re.findall("Spain\Z", txt)

print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")

```

[arn]: Returns a match where one of the specified characters (a, r, or n) is present

```
import re

txt = "The rain in Spain"

#Check if the string has any a, r, or n characters:

x = re.findall("[arn]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

```

[a-n]: Returns a match for any lower case character, alphabetically between a and n


```
import re

txt = "The rain in Spain"

#Check if the string has any characters between a and n:

x = re.findall("[a-n]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


```

[^arn]: Returns a match for any character EXCEPT a, r, and n

```
import re

txt = "The rain in Spain"

#Check if the string has other characters than a, r, or n:

x = re.findall("[^arn]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

```

[a-n]: Returns a match for any lower case character, alphabetically between a and n


```

import re

txt = "The rain in Spain"

#Check if the string has any characters between a and n:

x = re.findall("[a-n]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")



```

[^arn]: Returns a match for any character EXCEPT a, r, and n


```
import re

txt = "The rain in Spain"

#Check if the string has other characters than a, r, or n:

x = re.findall("[^arn]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

```

[0123]: Returns a match where any of the specified digits (0, 1, 2, or 3) are present

```
import re

txt = "The rain in Spain"

#Check if the string has any 0, 1, 2, or 3 digits:

x = re.findall("[0123]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

```

[0-9]: Returns a match for any digit between 0 and 9

```
import re

txt = "8 times before 11:45 AM"

#Check if the string has any digits:

x = re.findall("[0-9]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


```

[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59

```
import re

txt = "8 times before 11:45 AM"

#Check if the string has any two-digit numbers, from 00 to 59:

x = re.findall("[0-5][0-9]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

```
[a-zA-Z]:	Returns a match for any character alphabetically between a and z, lower case OR upper case

```
import re

txt = "8 times before 11:45 AM"

#Check if the string has any characters from a to z lower case, and A to Z upper case:

x = re.findall("[a-zA-Z]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

```




```

import re

txt = "8 times before 11:45 AM"

#Check if the string has any + characters:

x = re.findall("[+]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


```































































































































































































































