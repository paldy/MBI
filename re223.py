import requests
import re

line1 = 'https://stepic.org/media/attachments/lesson/24472/sample1.html'
line2 = 'https://stepic.org/media/attachments/lesson/24472/sample2.html'
#line1 = input()
#line2 = input()


pattern = r'<a\s+(?:[^>]*?\s+)?href="(https?:.*?)"'
allinks = []

res_html = requests.get(line1)
fromline1 = re.findall(pattern, res_html.text)

for i in fromline1:
    res = requests.get(i)
    froml = re.findall(pattern, res.text)
    allinks = allinks + froml

if line2 not in allinks: 
    print('No')
else:
    print('Yes')
# the end# the end
# the end
# the end
# the end again
# the end again
