import csv
import json
from datetime import date
import re


class Client:
    def __init__(self, name, surname, birth_date, bonuses):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.bonuses = bonuses

    def validate(self):
        if not re.match(r'^[А-Яа-яЁё]+$', self.name):
            return False
        if not re.match(r'^[А-Яа-яЁё]+$', self.surname):
            return False
        try:
            birth_date = date.fromisoformat(self.birth_date)
            if birth_date > date.today() or birth_date < date(1950, 1, 1):
                return False
        except ValueError:
            return False
        try:
            bonuses = int(self.bonuses)
            if bonuses < 0 or bonuses > 10000000:
                return False
        except ValueError:
            return False
        return True


skipped = 0
processed = 0

clients = []
with open('clients.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        name, surname, birth_date, bonuses = row
        client = Client(name, surname, birth_date, bonuses)
        if client.validate():
            processed += 1
            clients.append(client)
        else:
            skipped += 1

with open('clients.json', 'w') as f:
    json.dump([c.__dict__ for c in clients], f, ensure_ascii=False)

print(f'Обработано записей: {processed}')
print(f'Пропущено записей: {skipped}')
