class SelfExplain:
    """
    A class to demonstrate how 'self' points to the object itself.
    """

    def __init__(self):
        """
        Called when a new SelfExplain object is created.
        Prints the memory address of 'self'.
        """
        print("[SelfExplain] Constructor called.")
        print("Inside constructor, 'self' memory address:", id(self))


class Class2:
    """
    Another class to show that 'self' always refers to the current object.
    """

    def __init__(self):
        """
        Called when a new Class2 object is created.
        Prints the memory address of 'self'.
        """
        print("[Class2] Constructor called.")
        print("Inside constructor, 'self' memory address:", id(self))


# Creating object of SelfExplain
obj1 = SelfExplain()
print("Outside constructor, obj1 memory address:", id(obj1))
print()

# Creating object of Class2
obj2 = Class2()
print("Outside constructor, obj2 memory address:", id(obj2))
