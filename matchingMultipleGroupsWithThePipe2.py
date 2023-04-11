import re

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
matchObject = batRegex.search('Batmobile lost a wheel')
print(matchObject.group())
print(matchObject.group(1))
