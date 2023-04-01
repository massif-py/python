import re

phoneNumRegex = re.compile(r'(\(\d{3}\)) (\d{3}-\d{4})')
matchObject = phoneNumRegex.search('My phone number is (415) 555-4242')

print(matchObject.group(1))
print(matchObject.group(2))
print(matchObject.groups())
