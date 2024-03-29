def best_items(racers):
    winner_item_counts = {}
    for rango in range(len(racers)):
        racer = racers[rango]
        if racer['finish'] == 1:
            for item in racer['items']:
                if item not in winner_item_counts:
                    winner_item_counts[item] = 0
                winner_item_counts[item] += 1

        if racer['name'] is None:
            print("WARNING: Encountered racer with unknown name on iteration {}/{} (racer = {})".format(
                rango+1, len(racers), racer['name'])
                 )
    return winner_item_counts


sample = [
    {'name': 'Peach', 'items': ['green shell', 'banana', 'green shell',], 'finish': 3},
    {'name': 'Bowser', 'items': ['green shell',], 'finish': 1},
    {'name': None, 'items': ['mushroom',], 'finish': 2},
    {'name': 'Toad', 'items': ['green shell', 'mushroom'], 'finish': 1},
]

print(best_items(sample))