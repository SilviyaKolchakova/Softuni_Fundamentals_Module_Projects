from math import floor
biscuit_per_worker_per_day = int(input())
workers_count = int(input())
competing_factory_production = int(input())
production = 0
day = 0
production_per_day = biscuit_per_worker_per_day * workers_count
for days in range(30):
    day += 1
    if day % 3 == 0:
        production += floor(production_per_day * 0.75)
    else:
        production += production_per_day
print(f'You have produced {production} biscuits for the past month.')
if production > competing_factory_production:
    print(f'You produce {(production-competing_factory_production) / competing_factory_production * 100:.2f} percent more biscuits.')
else:
    print(f'You produce {abs((production-competing_factory_production) / competing_factory_production * 100):.2f} percent less biscuits.')


