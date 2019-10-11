import sys
from lxml import etree 
#doc = etree.parse("book.xml")

root = etree.parse(open(sys.argv[1],'r'))
count = sum(1 for _ in root.iter("*"))
print(count)

