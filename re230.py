import requests, re

#line1 = input()
line1 = 'https://stepik.org'

line1.strip()

pattern = r'<a\s+(?:[^>]*?\s+)?href=(?:\'|\")?(?:[a-z,-]+?://)?(\w[\w,\d,\.,-]*)(?:\'|\"|/|:)'

res_html = requests.get(line1)
fromline1 = re.findall(pattern, res_html.text)

print(len(fromline1))

set(fromline1) # убираю дубли в списке
fromline1 = list(set(fromline1))
fromline1.sort()
print(*fromline1, sep='\n')
