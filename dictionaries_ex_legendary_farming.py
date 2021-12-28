next_line = input()
key_materials_dict = {'shards': 0, 'motes': 0, 'fragments': 0}
junk_dict = {}
material_obtained = False
while not material_obtained:
    materials = next_line.split(" ")
    for item in range(0, len(materials), 2):
        quantity = int(materials[item])
        material = materials[item+1].lower()
        if material == 'shards' or material == 'motes' or material == 'fragments':
            key_materials_dict[material] += quantity
        else:
            if material not in junk_dict:
                junk_dict[material] = quantity
            else:
                junk_dict[material] += quantity
        for key, value in key_materials_dict.items():
            if value >= 250:
                if key == 'shards':
                    print('Shadowmourne obtained!')
                if key == 'fragments':
                    print('Valanyr obtained!')
                if key == 'motes':
                    print('Dragonwrath obtained!')
                key_materials_dict[key] -= 250
                material_obtained = True
                break
        if material_obtained:
            for material, qty in sorted(key_materials_dict.items(), key=lambda x: (-x[1], x[0])):
                print(f'{material}: {qty}')
            for material, qty in sorted(junk_dict.items(), key=lambda x: x[0]):
                print(f'{material}: {qty}')
            break
    if not material_obtained:
     next_line = input()







