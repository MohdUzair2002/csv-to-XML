import csv
import xml.etree.ElementTree as ET

# Define a dictionary that maps original column names to desired column names
column_names = {'Supplier code': 'Supplier name', 'column2': 'new_name2', 'column3': 'new_name3'}

# Open the CSV file
with open('Data.csv', 'r') as csvfile:
    # Read the CSV data
    csvdata = csv.reader(csvfile)

    # Get the header row and switch the column names
    header = next(csvdata)
    header = [column_names.get(col, col) for col in header]

    # Create the root element of the XML file
    root = ET.Element('data')

    # Loop through the CSV data and create the XML elements
    for row in csvdata:
        element = ET.SubElement(root, 'row')
        for i, value in enumerate(row):
            ET.SubElement(element, header[i]).text = value

    # Write the XML file
    tree = ET.ElementTree(root)
    tree.write('output1.xml', encoding='utf-8', xml_declaration=True)
