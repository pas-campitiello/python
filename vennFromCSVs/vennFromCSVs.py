import csv
from matplotlib import pyplot as plt
from matplotlib_venn import venn2

# read in the data from the CSV file
with open('data.csv', 'r') as f:
  reader = csv.reader(f)
  data = list(reader)

# extract the items from the first and second tabs
set1 = set(data[0])
set2 = set(data[1])

# create the Venn diagram
venn2([set1, set2])
plt.show()
