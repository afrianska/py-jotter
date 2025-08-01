def move_tower(height, from_pole, with_pole, to_pole):
    if height >= 1:
        move_tower(height - 1, from_pole, to_pole, with_pole)
        move_disk(from_pole, to_pole)
        move_tower(height - 1, with_pole, from_pole, to_pole)


def move_disk(from_pole, to_pole):
    print("Moving disk from", from_pole, "to", to_pole)


move_tower(5, "A", "B", "C")
