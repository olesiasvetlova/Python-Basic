class Animal:
    """
    Class describing an animal.
    """
    def __init__(self, name: str, weight: float, speed: float):
        self.name = name
        self.weight = weight
        self.speed = speed

    def move(self):
        print(f"The {self.name} is moving.")

    def eat(self):
        print(f"The {self.name} is eating.")


class Bird(Animal):
    """
    Class describing a bird.
    """
    def __init__(self, name: str, weight: float, speed: float, wingspan: float):
        super().__init__(name, weight, speed)
        self.wingspan = wingspan

    def fly(self):
        print(f"The {self.name} is flying.")


class Crow(Bird):
    """
    Class describing a crow.
    """
    def __init__(self, name: str, weight: float, speed: float, wingspan: float):
        super().__init__(name, weight, speed, wingspan)

    def caw(self):
        print(f"The {self.name} is cawing.")


class Seagull(Bird):
    """
    Class describing a seagull.
    """
    def __init__(self, name: str, weight: float, speed: float, wingspan: float):
        super().__init__(name, weight, speed, wingspan)

    def squawk(self):
        print(f"The {self.name} is squawking.")


class Reptile(Animal):
    """
    Class describing a reptile.
    """
    def __init__(self, name: str, weight: float, speed: float, length: float):
        super().__init__(name, weight, speed)
        self.length = length

    def slither(self):
        print(f"The {self.name} is slithering.")


class Snake(Reptile):
    """
    Class describing a snake.
    """
    def __init__(self, name: str, weight: float, speed: float, length: float):
        super().__init__(name, weight, speed, length)

    def hiss(self):
        print(f"The {self.name} is hissing.")


class Crocodile(Reptile):
    """
    Class describing a crocodile.
    """
    def __init__(self, name: str, weight: float, speed: float, length: float):
        super().__init__(name, weight, speed, length)

    def snap(self):
        print(f"The {self.name} is snapping its jaws.")


class Mammal(Animal):
    """
    Class describing a mammal.
    """
    def __init__(self, name: str, weight: float, speed: float, fur_color: str):
        super().__init__(name, weight, speed)
        self.fur_color = fur_color

    def nurse_young(self):
        print(f"The {self.name} is nursing its young.")


class Cat(Mammal):
    """
    Class describing a cat.
    """
    def __init__(self, name: str, weight: float, speed: float, fur_color: str):
        super().__init__(name, weight, speed, fur_color)

    def meow(self):
        print(f"The {self.name} is meowing.")


class Dog(Mammal):
    """
    Class describing a dog.
    """
    def __init__(self, name: str, weight: float, speed: float, fur_color: str):
        super().__init__(name, weight, speed, fur_color)

    def bark(self):
        print("The dog is barking.")


crow = Crow("Crow", 1.5, 20, 1.2)
seagull = Seagull("Seagull", 2, 30, 4)
snake = Snake("Snake", 5, 5, 0)
crocodile = Crocodile("Crocodile", 100, 10, 0)
cat = Cat("Cat", 4, 15, 'white')
dog = Dog("Dog", 10, 20, 'black')

crow.fly()
seagull.fly()
snake.slither()
crocodile.snap()
cat.meow()
dog.bark()