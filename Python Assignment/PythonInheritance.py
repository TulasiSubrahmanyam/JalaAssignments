class A:
    def __init__(self):
        self.a = 0

    def methodA1(self):
        print("Method A1")

    def methodA2(self):
        print("Method A2")

    def methodOverride(self):
        print("Method Override in A")


class B(A):
    def __init__(self):
        super().__init__()
        self.b = 0

    def methodB1(self):
        print("Method B1")

    def methodB2(self):
        print("Method B2")

    def methodOverride(self):
        print("Method Override in B")


class C(B):
    def __init__(self):
        super().__init__()
        self.c = 0

    def methodC1(self):
        print("Method C1")

    def methodC2(self):
        print("Method C2")

    def methodOverride(self):
        print("Method Override in C")


def main():
    aObj = A()
    aObj.methodA1()
    aObj.methodA2()
    aObj.methodOverride()

    bObj = B()
    bObj.methodA1()  # Inherited from A
    bObj.methodA2()  # Inherited from A
    bObj.methodB1()
    bObj.methodB2()
    bObj.methodOverride()  # Calls overridden method in B

    cObj = C()
    cObj.methodA1()  # Inherited from A
    cObj.methodA2()  # Inherited from A
    cObj.methodB1()  # Inherited from B
    cObj.methodB2()  # Inherited from B
    cObj.methodC1()
    cObj.methodC2()
    cObj.methodOverride()  # Calls overridden method in C

    # Runtime Polymorphism with Data Members/Instance variables
    aObj.a = 1
    print(aObj.a)

    bObj.a = 2  # Inherited from A
    bObj.b = 3
    print(bObj.a)
    print(bObj.b)

    cObj.a = 4  # Inherited from A
    cObj.b = 5  # Inherited from B
    cObj.c = 6
    print(cObj.a)
    print(cObj.b)
    print(cObj.c)


if __name__ == '__main__':
    main()


#another small easy understand inheritance
class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        print(f"{self.name} makes a sound.")
        

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        
    def speak(self):
        print(f"{self.name} barks.")
        
        
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        
    def speak(self):
        print(f"{self.name} meows.")
        

def main():
    animal = Animal("Generic Animal")
    animal.speak()  # Output: Generic Animal makes a sound.
    
    dog = Dog("Rufus")
    dog.speak()  # Output: Rufus barks.
    
    cat = Cat("Whiskers")
    cat.speak()  # Output: Whiskers meows.
    
    # Polymorphism
    animal = dog
    animal.speak()  # Output: Rufus barks.
    
    animal = cat
    animal.speak()  # Output: Whiskers meows.
    

if __name__ == '__main__':
    main()
