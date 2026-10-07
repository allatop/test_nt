import sys
import json

values_file = sys.argv[1]
tests_file = sys.argv[2]
report_file = sys.argv[3]

with open(values_file, encoding="utf-8") as f:
    values_data = json.load(f)

values_map = {}
for item in values_data["values"]:
    values_map[item["id"]] = item["value"]

with open(tests_file, encoding="utf-8") as f:
    tests_data = json.load(f)

def fill_values(node):
    if "id" in node and node["id"] in values_map:
        node["value"] = values_map[node["id"]]

    if "values" in node:
        for child in node["values"]:
            fill_values(child)

for test in tests_data["tests"]:
    fill_values(test)

with open(report_file, "w", encoding="utf-8") as f:
    json.dump(tests_data, f, ensure_ascii=False, indent=2)

print(report_file)