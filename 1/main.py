"""https://adventofcode.com/2022/day/1"""

input_file: str = "input.txt"

with open(input_file, 'r') as input_:
    calories: list[tuple] = [(n, sum([int(food) for food in \
        elf.split('\n') if food not in ['']])) for n, elf in \
        enumerate(input_.read().split('\n\n'))
    ]

elfs, calories = zip(*calories)
top: int = max(calories)

print(f"""The elf carrying most calories is elf \
#{elfs[calories.index(top)]} which is \
carrying {top} calories.
The sum of the calories carried by the three elves which are carrying more \
calories is {sum(sorted(calories, reverse = True)[:3])}""")
