import requests
import csv
from io import StringIO

url = "https://www.bring.no/postnummerregister-ansi.txt"

response = requests.get(url)
response.raise_for_status()

data = StringIO(response.text)

csv_reader = csv.reader(data, delimiter="\t")

js_file = "const postalCodeMap = {\n"
for row in csv_reader:
    postnummer, poststed, kommunekode, kommune, _ = row
    js_file += f'  "{postnummer}": {{ "city": "{poststed}", "municipality": "{kommune}" }},\n'
    print(postnummer, poststed)
js_file += "};\n"

js_file += "function getPostalCodeInfo(postalCode) {\n"
js_file += "  const info = postalCodeMap[postalCode];\n"
js_file += "  if (!info) {\n"
js_file += '    return { "city": "UNKNOWN", "municipality": "UNKNOWN" };\n'
js_file += "  }\n"
js_file += "  return info;\n"
js_file += "}\n"

js_file += "module.exports = getPostalCodeInfo;\n"

with open("index.js", "w") as file:
    file.write(js_file)
