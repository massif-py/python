import re

haRegex = re.compile(r'(Ha){3}')
matchObject1 = haRegex.search('HaHaHa')
print(matchObject1.group())
matchObject2 = haRegex.search('Ha')
print(matchObject2 == None)
