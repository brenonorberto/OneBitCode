class Animal:
    name = ""
    size = ""
    color = ""

    def eat(self):
        print(f"{self.name} se alimentando...")


class Horse(Animal):
    race = ""

    def escape(self):
        print(f"{self.name} escapando...")


class Lion(Animal):
    mane = True

    def hunt(self):
        print(f"{self.name} caçando...")


h = Horse()
h.name = "Pé de pano"
h.color = "Cinza"
h.escape()
h.eat()

print("-----")

l = Lion()
l.name = "Simba"
l.color = "Amarelo"
l.hunt()
l.eat()
