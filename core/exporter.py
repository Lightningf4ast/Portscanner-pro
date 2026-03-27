import json
import os

os.makedirs("output", exist_ok=True)

def save_txt(results, path="output/results.txt"):
    with open(path, "w") as f:
        for r in results:
            f.write(f"{r['port']} | {r['service']}\n")


def save_json(results, path="output/results.json"):
    with open(path, "w") as f:
        json.dump(results, f, indent=4)
