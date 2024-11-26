from itertools import combinations

items = {
    "r": (3, 25),
    "p": (2, 15),
    "a": (2, 15),
    "m": (2, 20),
    "i": (1, 5),
    "k": (1, 15),
    "x": (3, 20),
    "t": (1, 25),
    "f": (1, 15),
    "d": (1, 10),
    "s": (2, 20),
    "c": (2, 20)
}

backpack = [[" " for i in range(3)] for j in range(3)]
initial_score = 10


def calculate(items_taken, all_items, initial_score):
    taken_score = sum(all_items[item][1] for item in items_taken)
    not_taken_score = sum(all_items[item][1] for item in all_items if item not in items_taken)
    return initial_score + taken_score - not_taken_score


def arrange_items_to_backpack(items_taken, backpack):
    backpack_copy = [row[:] for row in backpack]
    free_slots = [(i, j) for i in range(len(backpack)) for j in range(len(backpack[0]))]

    for item in items_taken:
        item_size = items[item][0]
        placed = False
        for start_x, start_y in free_slots:
            if try_place_item(backpack_copy, item, item_size, start_x, start_y):
                free_slots = [(i, j) for i in range(len(backpack)) for j in range(len(backpack[0])) if
                              backpack_copy[i][j] == " "]
                placed = True
                break
        if not placed:
            return None
    return backpack_copy


def try_place_item(backpack, item, item_size, start_x, start_y):
    directions = [(0, 1), (1, 0)]
    for dx, dy in directions:
        positions = []
        x, y = start_x, start_y
        for _ in range(item_size):
            if 0 <= x < len(backpack) and 0 <= y < len(backpack[0]) and backpack[x][y] == " ":
                positions.append((x, y))
                x, y = x + dx, y + dy
            else:
                break
        if len(positions) == item_size:
            for x, y in positions:
                backpack[x][y] = item
            return True
    return False


valid_combinations = []

for r in range(1, len(items) + 1):
    for items_taken in combinations(items.keys(), r):
        final_score = calculate(items_taken, items, initial_score)
        if final_score > 0:
            arranged_backpack = arrange_items_to_backpack(items_taken, backpack)
            if arranged_backpack:
                valid_combinations.append((items_taken, final_score, arranged_backpack))

if valid_combinations:
    print(f"Найдено {len(valid_combinations)} подходящих комбинаций:\n")
    for idx, (items_taken, score, arranged_backpack) in enumerate(valid_combinations, 1):
        print(f"Комбинация {idx}:")
        for item in items_taken:
            print(f"  {item}: {items[item][1]} очков выживания ({items[item][0]} ячеек)")
        print(f"Итоговый счёт выживания: {score}")
        print("Рюкзак:")
        for row in arranged_backpack:
            print(" ".join(row))
        print("\n" + "-" * 20 + "\n")
else:
    print("Не найдено подходящих комбинаций.")
