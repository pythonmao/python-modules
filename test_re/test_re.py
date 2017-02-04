import re

mm = re.search('\Aab', 'abs')
print mm.group(0)

mm = re.search('ab\Z', 'sab')
print mm.group(0)

# mm = re.search(r'\bcsd', '1csd')
# print mm.group(0)

mm = re.search(r'a\Bcsd', 'acsd')
print mm.group(0)

mm = re.search('(ab)', 'absabsab')
print mm.group()

mm = re.match('(ab)', 'absabsab')
print mm.groups()

mm = re.findall('(ab)', 'absabsab')
print mm

mm = re.search(r'\d(?<=\d)a', 'a3av')
print mm.group(0)


p = re.compile(r'\d+')
for m in p.finditer('one1two2three3four4'):
    print m.group(),

print '\n'

p = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world'
print p.sub(r'\2 \1', s)
print p.subn(r'\2 \1', s)

m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
print m.groupdict()


# mm = re.search('(?P<id>ab)', 'absabsab')


# mm = re.search((?p<name>'ab'), 'absabsab')
# print mm.group(0)


