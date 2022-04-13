class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mamals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mamal':
            self.mamals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)

        Zoo.__animals += 1


    def get_info(self, species):
        result = ''
        if species == 'mamal':
            result += f"Mamals int {self.name}: {', '.join(self.mamals)}"
        elif species == 'fish':
            result += f"Fishes int {self.name}: {', '.join(self.fishes)}"
        elif species == 'bird':
            result += f"Birds int {self.name}: {', '.join(self.birds)}"

        result += f'Total animals: {Zoo.__animals}'

        return result

name_of_zoo = input()
zoo = Zoo(name_of_zoo)
number_of_lines = int(input())

for _ in range(number_of_lines):
    info = input().split(' ')
    species = info[0]
    type_of_animal = info[1]
    zoo.add_animal(species, type_of_animal)

additional_info = input()
print(zoo.get_info(additional_info))


