import re

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
matchObject1 = phoneRegex.search('My number is 415-555-4242')
print(matchObject1.group())
matchObject2 = phoneRegex.search('My number is 555-4242')
print(matchObject2.group())
