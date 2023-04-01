import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
matchObject = phoneNumRegex.search('My number is 415-555-4242')

print(matchObject.group(1))
print(matchObject.group(2))
print(matchObject.group(0))
print(matchObject.group())
print(matchObject.groups())

areaCode, mainNumber = matchObject.groups()

print(areaCode)
print(mainNumber)


