import json
with open("inventory.json", "r", encoding="utf-8") as file:
    inventory = json.load(file)

# выводим список материалов, которые необходимо закупить, если их количество меньше минимально необходимого


def need_to_buy(inventory):
    need_to_buy = {}
    for name in inventory["inventory"]:
        if name["quantity"] < name["min_quantity"]:
            need_to_buy = (
                f"Необходимо закупить: {name['item']} {name['quantity']} шт.")
    return need_to_buy


inventory_need_to_buy = need_to_buy(inventory)
for item in inventory_need_to_buy:
    print(item)
