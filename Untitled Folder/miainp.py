import re

string = \
"""\
010-1234-1234
010-1234-5678
+82-10-5678-5678
+82-10-4123-1234\
"""

pattern = r'^(?:0|\+82-)\d{1,2}-(\d{4})-\1$'
print(re.sub(pattern,"치환됨",string,flags=re.MULTILINE))

