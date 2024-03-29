# Inheritance is a way of creating a new class for using details of an existing class without modifying it.

# The newly formed class is a derived class (or child class). Similarly, the existing class is a base class (or parent class).

# base class
class Animal:
    
    def eat(self):
        print( "I can eat!")
    
    def sleep(self):
        print("I can sleep!")

# derived class
class Dog(Animal):
    
    def bark(self):
        print("I can bark! Woof woof!!")

# Create object of the Dog class
dog1 = Dog()

# Calling members of the base class
dog1.eat()
dog1.sleep()

# Calling member of the derived class
dog1.bark();

# Here, dog1 (the object of derived class Dog) can access members of the base class Animal. It's because Dog is inherited from Animal.
print("")
# Calling members of the Animal class
dog1.eat()
dog1.sleep()