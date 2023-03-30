import re

greedyHaRegex = re.compile(r'(Ha){3,5}')
matchObject1 = greedyHaRegex.search('HaHaHaHaHa')
print(matchObject1.group())
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
matchObject2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(matchObject2.group())
