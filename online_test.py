import xml.etree.ElementTree as ET


def timestamps_by_description(xml, description):


    myroot = ET.fromstring(xml)
    for x in myroot:
    #  print(x.tag, x.attrib)
     print("sdfgdfg: ", x.get('timestamp'))
     print("fgdfgf: ", x[0].text)
     if description == x[0].text:
         return x.get('timestamp')

    return None


xml = """<?xml version="1.0" encoding="UTF-8"?>
<log>
    <event timestamp="1614285589">
        <description>Intrusion detected</description>
    </event>
    <event timestamp="1614286432">
        <description>Intrusion ended</description>
    </event>
</log>"""

print(timestamps_by_description(xml, 'Intrusion ended'))
