"""Create a sample sales.csv so the dashboard has data to show."""
import csv
import random
from datetime import date, timedelta

random.seed(42)
regions = ["North", "South", "East", "West"]
products = {"Laptop": 800, "Phone": 500, "Tablet": 300, "Headphones": 80}

start = date(2025, 1, 1)
with open("sales.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["date", "region", "product", "units", "revenue"])
    for i in range(365):
        d = start + timedelta(days=i)
        for _ in range(random.randint(1, 4)):
            product = random.choice(list(products))
            units = random.randint(1, 10)
            w.writerow([d, random.choice(regions), product, units, units * products[product]])
print("sales.csv created")
