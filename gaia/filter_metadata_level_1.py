import json

# Input and output file paths
input_file = "./gaia/metadata_gaia.jsonl"  # Changed from .txt to .jsonl
output_file = "metadata.jsonl"

# Open the input file and process line by line
with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
    for line in infile:
        try:
            data = json.loads(line.strip())
            if data.get("Level") == 1:
                outfile.write(json.dumps(data, ensure_ascii=False) + "\n")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON on line: {line}")
            print(f"Error details: {e}")
            continue