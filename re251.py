import json

myjson =  json.loads(input())
#myjson = [{"name": "AAAA", "parents": []}, {"name": "B", "parents": ["AAAA", "C"]}, {"name": "C", "parents": ["AAAA"]}]
#myjson = [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

dic = {} 
# превращаю список словарей в один словарь {'B': {'A', 'C'}, 'A': set(), 'C': {'A'}}
for i in list(myjson):
    dic[i['name']] = set(i['parents'])
print(dic) #  {'B': {'A', 'C'}, 'A': set(), 'C': {'A'}}

def dfs(graph, start): 
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return list(visited)

allist = []
for item in dic:
    allist.extend(dfs(dic, item))
    print(item, '---', dfs(dic, item)) # B --- ['B', 'A', 'C']     A --- ['A']      C --- ['A', 'C']

print(allist) #  ['B', 'A', 'C', 'A', 'A', 'C']

#  подсчет дублей в списке
counter = {} 
for elem in allist: 
    counter[elem] = counter.get(elem, 0) + 1
    doubles = {element: count for element, count in counter.items() if count >= 1}

print(doubles) #  {'B': 1, 'A': 3, 'C': 2}

list_keys = list(doubles.keys()) #  сортировка словаря по ключам
list_keys.sort()
for i in list_keys:
    print(i, ':', doubles[i])
