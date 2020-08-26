import re

"""
t="A fat cat doesn't eat oat but a rat eats bats."
p=re.findall("[force]at", t)
print(p[1])
"""

#c="Python Training Course for Beginners: 15/Aug/2011 - 19/Aug/2011;Python Training Course Intermediate: 12/Dec/2011 - 16/Dec/2011;Python Text Processing Course:31/Oct/2011 - 4/Nov/2011"
#i=re.findall("[^:]*:[^;]*;?", c)
#print(i[1])

t="course location is london or paris"
i=re.search(r"location.*(london)", t)
print(t)
