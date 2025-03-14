class Dogs:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self, u_name):
        return f"Привет {u_name} меня зовут {self.name} мне {self.age}"

u_name = input("Привет как тебя зовут")

dog1 = Dogs("Барбос", 7)
print(dog1.bark(u_name))
