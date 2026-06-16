import json

json_format = {}

with open('claude_const_2026.txt', 'r') as file:
    content = file.read()

pages = content.split("======= PAGE")

for i, page in enumerate(pages):
    json_format[i] = page