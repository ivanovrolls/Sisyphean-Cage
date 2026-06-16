import json

with open('claude_2023.json', 'r') as file:
    data = file.read()

parsed = json.loads(data)
principles = 0
section_dict = {}

for section in parsed["sections"]:
    principles_in_section = len(section["principles"])
    #print(section["name"], ": ", principles_in_section)
    section_dict[section["name"]] = principles_in_section
    principles += len(section["principles"])


sections = len(parsed["sections"])
print("Sections: ", sections, "Principles: ", principles)
print(section_dict)