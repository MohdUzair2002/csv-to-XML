import csv
import xml.etree.ElementTree as ET

csv_file = 'Data.csv'
xml_file = 'output.xml'

# Read CSV file and extract data
data = []
with open(csv_file, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        data.append(row)

# Create root element
root = ET.Element('data')

# Add data to root element
for row in data:
    row_elem = ET.SubElement(root, 'row')
    for col in ['Supplier code', 'Supplier name', 'Site code','Site name','Site country']:  # Replace with your column headers
        col_elem = ET.SubElement(row_elem, col)
        col_elem.text = row[col]

# Create XML tree and write to file
tree = ET.ElementTree(root)
tree.write(xml_file, xml_declaration=True, encoding='UTF-8')