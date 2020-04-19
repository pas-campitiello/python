# taken from https://stackoverflow.com/questions/5084743/how-to-print-pretty-string-output-in-python

template = "{0:8}|{1:10}|{2:15}|{3:7}|{4:10}" # column widths: 8, 10, 15, 7, 10
print(template.format("CLASSID", "DEPT", "COURSE NUMBER", "AREA", "TITLE")) # header
for rec in [["21","21","54","98","32"],["21","4","89","65","23"]]: 
  print(template.format(*rec))
