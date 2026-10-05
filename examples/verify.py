from decimal import Decimal
from pathlib import Path
import json

rows = json.loads(Path(__file__).with_name('scenario.json').read_text(encoding='utf-8'))
for row in rows:
    counted = row['counted']
    difference = None if counted is None else Decimal(counted) - Decimal(row['expected'])
    state = 'Sin contar' if difference is None else 'Coincide' if difference == 0 else 'Faltante' if difference < 0 else 'Sobrante'
    assert state == row['state'], row['article']
    assert difference == (None if row['difference'] is None else Decimal(row['difference'])), row['article']
assert sum(row['counted'] is not None for row in rows) == 4
assert sum(row['counted'] == '0' for row in rows) == 1
print('5 casos sintéticos correctos: igualdad, faltante, sobrante, cero y pendiente.')
