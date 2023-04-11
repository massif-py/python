import re

batRegex = re.compile(r'Bat(wo)+man')
matchObject1 = batRegex.search('The Adventures of Batwoman')
print(matchObject1.group())
matchObject2 = batRegex.search('The Adventures of Batwowowowowowoman')
print(matchObject2.group())
matchObject3 = batRegex.search('The Adventures of Batman')
print(matchObject3 == None)
