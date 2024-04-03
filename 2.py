import json
with open("inventory.json", "r", encoding="utf-8") as file:
    inventory = json.load(file)

# выводим список материалов, которые необходимо закупить, если их количество меньше минимально необходимого


def need_to_buy(inventory):
    need_to_buy = {}
    for name in inventory["inventory"]:
        if name["quantity"] < name["minimum_quantity"]:
            need_to_buy[name["item"]] = name["quantity"] 
    return need_to_buy


inventory_need_to_buy = need_to_buy(inventory)
for item, quantify in inventory_need_to_buy.items():
    print(f"Необходимо закупить: {item} {quantify} шт.")
