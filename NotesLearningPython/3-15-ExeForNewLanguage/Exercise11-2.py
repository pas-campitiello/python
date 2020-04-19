import xml.etree.ElementTree as etree

with open("table-input.htm", "r") as f:
    read_data = f.read()
    print ("File content:")
    print(read_data)

tree = etree.fromstring(read_data)

with open("table-input.csv", "w") as f:
    for amt, unit, item in tree.getiterator('tr'):
        print("%s,%s,%s" % (amt.text, unit.text, item.text))
        f.write("%s,%s,%s\n" % (amt.text, unit.text, item.text))
