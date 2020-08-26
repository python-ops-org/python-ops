import xml.etree.ElementTree as ET
xml = '''<?xml version="1.0" encoding="UTF-8"?>
<Automation_Config>
    <Path>
        <Log>.\SERVER.log</Log>
        <Flag_Path>.\Flag</Flag_Path>
        <files>.\PO</files>
    </Path>

</Automation_Config>'''

root = ET.fromstring(xml)
for idx,log_element in enumerate(root.findall('.//Log')):
  print('{}) Log value: {}'.format(idx,log_element.text))
