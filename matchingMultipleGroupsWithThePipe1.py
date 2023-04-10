import re

heroRegex = re.compile(r'Batman|Tina Fey')

matchObject1 = heroRegex.search('Batman and Tina Fey')
print(matchObject1.group())

matchObject2 = heroRegex.search('Tina Fey and Batman')
print(matchObject2.group())
