class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def introduce(self):
        print(f"Hello, my name is {self.name}. I am a {self.age} year old {self.gender}.")
        
intro = Person("Locha", 25, "male")

intro.introduce()
    