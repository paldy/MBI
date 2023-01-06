from xml.etree import ElementTree#, XMLParser

# myxml = """
# <cube color="blue">
#     <cube color="red">
#         <cube color="green">
#             <cube color="green">
#                 <cube color="green">
#                     <cube color="blue">
#                     </cube>
#                     <cube color="green">
#                     </cube>
#                     <cube color="red">
#                     </cube>
#                 </cube>
#             </cube>
#         </cube>
#     </cube>
#     <cube color="red">
#         <cube color="blue">
#         </cube>
#     </cube>
# </cube>
# """


myxml ='''<cube color="blue">
            <cube color="red">
                <cube color="green">
                </cube>
            </cube>
            <cube color="red">
            </cube>
        </cube>'''

#newxml = ElementTree.fromstring(input())
newxml = ElementTree.fromstring(myxml)


def counterlvl(lvl, color):
	pathcube = '/cube'*lvl
	sko = len(newxml.findall('.'+pathcube+'[@color='+'"'+color+'"'+']'))
	summa = sko * (lvl+1)
	return sko, color, lvl, summa

cv = {}
sumelements = len(newxml.findall(".//cube[@color]"))+1 
for c in range(1000):
	if sumelements == 0:
		break	
	for clr in ['red', 'green', 'blue']:
		[sko, color, lvl, summa] = counterlvl(c, clr)
		sumelements -= sko
		# print(sko, color, lvl, summa, '---', sumelements)
		if clr in cv:
			cv[clr] = cv[clr] + summa
		else:
			cv[clr] = summa


print(cv['red'], cv['green'], cv['blue'])
# the end
# the end
