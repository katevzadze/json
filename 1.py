import json
with open("sales.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# складываем выручку товаров одной категории файла json


def profit(client_data):
    total_profit = {}
    for sale in client_data["sales"]:
        category = sale.get("category")
        profit = sale.get("total_price") * sale.get("quantity")
        if category not in total_profit:
            total_profit[category] = profit
        else:
            total_profit[category] += profit
    return total_profit


shop_sales = profit(data)
for category in shop_sales:
    print(f"Выручка по категории {category}: {shop_sales[category]} руб.")
