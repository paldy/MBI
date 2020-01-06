import requests

strings = []
out = []
def whichNumber(num):
    
    api_url = 'http://numbersapi.com/'+num+'/math?json' 

# requests.get(f'http://******.com/{num}/****') - можно и так
# http://numbersapi.com/31,999,1024,502/math?json=true - и так можно

    res = requests.get(api_url)
    if res.json()['found']:
        return 'Interesting'
    else:
        return 'Boring'
        

with open("/home/dipp/py/dataset_24476_3.txt") as f:
    strings = f.read().strip()
strings = strings.split('\n')
print(strings)

for num in strings:
    out.append(whichNumber(num))
print(out)


with open("/home/dipp/py/dataset_my.txt", 'w') as m:
    for an in out:
        an = an+'\n'
        m.write(an)

# print('ok')
