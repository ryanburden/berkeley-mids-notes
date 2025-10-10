Classes

- Why create new classes?
    - hold a specific format of data
    - create new functionality
    - build object-oriented software

- Bound method
    - d.ascend(100)
    - d is bound to the method by the period
    - Inside the method, self represents the object (d)

- Class / Instance Attributes

- Getter / Setter Methods
    - it can be good to have a get or set method regarding attributes. 
    - but, attributes can always be changed with instance.attribute = 10

- Hidden Attributes
    - dunder before the attribute name makes it hidden
    - ex: self.altitude -> self.__altitude
    - Trying to access this attribute will result in an AttributeError

- Accessing Hidden Attributes
    - add a dunder and the name of the class
    - ex: d1.__altitude -> d1.__Drone__altitude
    - This is called "Name Mangling"

- __repr__ and __str__ methods
    - without either of these magic commands, printing or entering the object
    - ie: d1 = Drone(), print(d1) will print the memory address
    - in repr and str methods, you can return whatever representation you want