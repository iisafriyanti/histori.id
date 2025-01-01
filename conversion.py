import json

# Input and output file paths
input_file = "Dataset/train_doclevel.json"
output_file = "Dataset/output.jsonl"

# Read the JSON file
with open(input_file, "r", encoding="utf-8") as infile:
    data = json.load(infile)

# Write to a JSONL file
with open(output_file, "w", encoding="utf-8") as outfile:
    for item in data:
        json_line = json.dumps(item, ensure_ascii=False)
        outfile.write(json_line + "\n")

print(f"Data successfully converted to {output_file}.")
