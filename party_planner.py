import argparse

items = {
    0: {"name": "Cake", "value": 20},
    1: {"name": "Balloons", "value": 21},
    2: {"name": "Music System", "value": 10},
    3: {"name": "Lights", "value": 5},
    4: {"name": "Catering Service", "value": 8},
    5: {"name": "DJ", "value": 3},
    6: {"name": "Photo Booth", "value": 15},
    7: {"name": "Tables", "value": 7},
    8: {"name": "Chairs", "value": 12},
    9: {"name": "Drinks", "value": 6},
    10: {"name": "Party Hats", "value": 9},
    11: {"name": "Streamers", "value": 18},
    12: {"name": "Invitation Cards", "value": 4},
    13: {"name": "CakParty Gamese", "value": 2},
    14: {"name": "Cleaning Service", "value": 11},
}

parser = argparse.ArgumentParser(description="Party Planner")
parser.add_argument(
    "--choices",
    type=str,
    help="comma-separated list of items e.g. 0,1,2",
)

args = parser.parse_args()

selected_items = None

if args.choices:
    selected_items = [int(idx.strip()) for idx in args.choices.split(",")]
else:
    for idx, item in items.items():
        print(f"{idx}: {item['name']}")
    choices = input("Enter item indices separated by commas (e.g., 0, 2): ")
    selected_items = [int(idx.strip()) for idx in choices.split(",")]

items_name = [items[selected_items[0]]["name"]]
base_codes = [items[selected_items[0]]["value"]]
base_code = items[selected_items[0]]["value"]
for idx in selected_items[1:]:
    item = items[idx]
    base_code &= item["value"]
    base_codes.append(item["value"])
    items_name.append(item["name"])

output = f"Selected items: {', '.join(items_name)}\n<br>\nBase Party Code: {' & '.join(map(str, base_codes))} = {str(base_code)}\n<br>\n"
message = ""
if base_code == 0:
    output += (
        f"Adjusted Party Code: {str(base_code)} + 5 = {str(base_code + 5)}\n<br>\n"
    )
    base_code += 5
    message = "Epic Party Incoming!"
elif base_code > 5:
    output += (
        f"Adjusted Party Code: {str(base_code)} - 2 = {str(base_code - 2)}\n<br>\n"
    )
    base_code -= 2
    message = "Let's keep it classy!"
else:
    message += f"Chill vibes only!"
output += f"Final Party Code: {str(base_code)}\n<br>\n<br>\nMessage: {message}"

print(output)
