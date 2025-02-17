import json

with open("lab4/json/sample-data.json", "r") as file:

    data = json.load(file)


interfaces = data["imdata"]

print("Interface Status")

print("=" * 80)

print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU':<6}")

print("-" * 80)

for item in interfaces:

    attributes = item["l1PhysIf"]["attributes"]

    dn = attributes["dn"]

    if attributes["descr"]:
        description = attributes["descr"]
    else:
        description = ""

    speed = attributes["speed"]

    mtu = attributes["mtu"]

    print(f"{dn:<50} {description:<20} {speed:<8} {mtu:<6}")