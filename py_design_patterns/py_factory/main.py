from abc import ABC, abstractmethod

class PetInterface(ABC):
    @abstractmethod
    def speak():
        """pet will say something here"""

class Dog(PetInterface):
    name: str

    def speak(self):
        print("im a dog!")

class Cat(PetInterface):
    name: str

    def speak(self):
        print("im a cat!")
        
def get_pet(pet = "dog"):
    pets = dict(dog = Dog("Hope"), cat = Cat("Peace"))
    return pets[pet]

class PetFactory:
    pets = {"dog": Dog(), "cat": Cat()}

    def GetPet(self, pet_type: str) -> PetInterface:
        return self.pets[pet_type]

if __name__ == "__main__":
    
    # creating the pet factory
    factory = PetFactory()
    
    # getting a dog
    dog = factory.GetPet("dog")
    dog.speak()

    # getting a cat
    cat = factory.GetPet("cat")
    cat.speak()