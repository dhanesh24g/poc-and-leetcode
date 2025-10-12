from pathlib import Path
from xml.etree.ElementTree import tostring, fromstring

from lxml import etree as et

file_read = Path(__file__).parent / "files" / "AccountProcess.process"

with open(file_read, "r+") as f:
    tree = et.parse(f)

print(et.tostring(tree, xml_declaration=True, pretty_print=True))
tree.xpath('ProcessDefinition')