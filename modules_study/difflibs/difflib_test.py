from difflib import *
import sys

s1 = ['bacon\n', 'eggs\n', 'ham\n', 'guido\n']
s2 = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']
sys.stdout.writelines(context_diff(s1, s2, fromfile='before.py', tofile='after.py'))

get_close_matches('appel', ['ape', 'apple', 'peach', 'puppy'])

print '='*80
diff = ndiff('one\ntwo\nthree'.splitlines(),'ore\ntree\nemu'.splitlines())
# print ''.join(diff)
print ' '.join(restore(diff, 1))


sys.stdout.writelines(unified_diff(s1, s2, fromfile='before.py', tofile='after.py'))

# difflib.IS_LINE_JUNK(line)
# Return true for ignorable lines. The line line is ignorable if line is blank or contains a single '#'
# difflib.IS_CHARACTER_JUNK(ch)
# Return true for ignorable characters. The character ch is ignorable if ch is a space or tab,
# difflib.diff_bytes(dfunc, a, b, fromfile=b'', tofile=b'', fromfiledate=b'', tofiledate=b'', n=3, lineterm=b'\n')
# Compare a and b (lists of bytes objects) using dfunc

s = SequenceMatcher(None, 'abc', 'ab')
print s.ratio()

s = SequenceMatcher(lambda x: x=='',
                    "private private Thread currentThread;",
                    "private volatile Thread currentThread;")

print


