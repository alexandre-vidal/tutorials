class Parrot:

    # class attribute
    name = ""
    age = 0

# create parrot1 object
parrot1 = Parrot()
parrot1.name = "Blu"
parrot1.age = 10

# create another object parrot2
parrot2 = Parrot()
parrot2.name = "Woo"
parrot2.age = 15

# access attributes
print(f"{parrot1.name} is {parrot1.age} years old")
print(f"{parrot2.name} is {parrot2.age} years old")

# In the above example, we created a class with the name Parrot with two attributes: name and age.

# Then, we create instances of the Parrot class. Here, parrot1 and parrot2 are references (value) to our new objects.

# We then accessed and assigned different values to the instance attributes using the objects name and the . notation.