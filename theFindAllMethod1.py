import re

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))
