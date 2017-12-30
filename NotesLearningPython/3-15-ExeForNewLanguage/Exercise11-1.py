dinner_recipe = '''<html><body><table>
<tr><th>amt</th><th>unit</th><th>item</th></tr>
<tr><td>24</td><td>slices</td><td>baguette</td></tr>
<tr><td>2+</td><td>tbsp</td><td>olive oil</td></tr>
<tr><td>1</td><td>cup</td><td>tomatoes</td></tr>
<tr><td>1</td><td>jar</td><td>pesto</td></tr>
</table></body></html>'''

import xml.etree.ElementTree as etree
tree = etree.fromstring(dinner_recipe)

f = open("table.csv", "w")

for amt, unit, item in tree.getiterator('tr'):
    print("%s,%s,%s" % (amt.text, unit.text, item.text))
    f.write("%s,%s,%s\n" % (amt.text, unit.text, item.text))

f.close()
