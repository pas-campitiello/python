import json
from matplotlib import pyplot as plt
from matplotlib_venn import venn2

# read in the data from the JSON file
with open('data.json', 'r') as f:
  data = json.load(f)

# extract the items from the two sets
set1 = set(data['etf1'])
set2 = set(data['etf2'])

# create the Venn diagram
diagram = venn2([set1, set2])

# show the data in the diagram
diagram.get_label_by_id('10').set_text(', '.join(set1 - set2))
diagram.get_label_by_id('01').set_text(', '.join(set2 - set1))
diagram.get_label_by_id('11').set_text(', '.join(set1 & set2))

# display the Venn diagram
plt.show()