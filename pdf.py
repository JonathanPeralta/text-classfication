import tika
tika.initVM()
from tika import parser
from tika import detector
parsed = parser.from_file('aa.pdf')
# print(parsed["metadata"])
print(parsed["content"])

# print(detector.from_file('sobras.docx'))