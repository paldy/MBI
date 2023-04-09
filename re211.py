import sys
import re

pattern = r'(cat.*){2,}'        

res = []
#  Считать все строки по одной из стандартного потока ввода
for line in sys.stdin:
    line = line.rstrip()
    
    result = re.findall(pattern, line)
    if result:
        res.append(line)
    if line == "":
        break

for p in res:
    print(p)

'''
# чужое красивое решение:
import sys
import re

inp = [line.rstrip() for line in sys.stdin]
out = [line for line in inp if re.search(r'(cat).*(cat)', line) is not None]

print(*out, sep='\n')
'''


'''
wer
catcat
cat and cat
tac
cat
catac
catcatcatcat
cat ertwrgg cat
catsdfscat
cat 0549682-=-+ ?:"{}][;/cat

Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.

'''
# the end
# the end
# the end
