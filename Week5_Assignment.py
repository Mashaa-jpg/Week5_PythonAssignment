# --- Assignment 1: Design Your Own Class! ---

# Let's design a Smartphone class.
# This is the parent class.
class Smartphone:
    """A class representing a generic smartphone."""

    # This is the constructor (__init__). It's used to initialize
    # the object with unique values for its attributes.
    def __init__(self, brand, model, os, storage_gb):
        self.brand = brand
        self.model = model
        self.os = os
        self.storage_gb = storage_gb
        # A simple attribute to represent installed apps
        self.apps = []

    # A method to display the smartphone's information.
    def display_info(self):
        """Prints the main information about the smartphone."""
        print(f"--- {self.brand} {self.model} ---")
        print(f"OS: {self.os}")
        print(f"Storage: {self.storage_gb} GB")
        print(f"Installed Apps: {', '.join(self.apps) or 'None'}")

    # A method to add an app to the smartphone.
    def install_app(self, app_name):
        """Adds a new app to the list of installed apps."""
        print(f"Installing {app_name} on {self.model}...")
        self.apps.append(app_name)
        print("Installation complete!")


# Now, let's create a child class using inheritance.
# This is a subclass of Smartphone, inheriting all its attributes and methods.
class GamingSmartphone(Smartphone):
    """A specialized smartphone designed for gaming."""

    # The constructor for the child class. We use super() to call
    # the parent's constructor first, then add new attributes.
    def __init__(self, brand, model, os, storage_gb, refresh_rate_hz):
        # Call the constructor of the parent class (Smartphone)
        super().__init__(brand, model, os, storage_gb)
        # Add a new attribute specific to GamingSmartphone
        self.refresh_rate_hz = refresh_rate_hz

    # This is an example of polymorphism and method overriding.
    # We define a new version of display_info() that's specific to this class.
    def display_info(self):
        """Overrides the parent's method to include gaming specs."""
        print(f"--- High-Performance Gaming Phone: {self.brand} {self.model} ---")
        print(f"OS: {self.os}")
        print(f"Storage: {self.storage_gb} GB")
        print(f"Display Refresh Rate: {self.refresh_rate_hz} Hz")
        print(f"Installed Apps: {', '.join(self.apps) or 'None'}")


# Let's create and use some objects to see it in action!
print("--- Assignment 1: Smartphone Class in Action ---")
standard_phone = Smartphone("Samsung", "Galaxy S21", "Android", 128)
standard_phone.install_app("Social Media")
standard_phone.display_info()
print("-" * 20)

gaming_phone = GamingSmartphone("ASUS", "ROG Phone 5", "Android", 256, 144)
gaming_phone.install_app("Mobile Legends")
gaming_phone.display_app("Genshin Impact")
gaming_phone.display_info()
print("\n" + "="*50 + "\n")


# --- Activity 2: Polymorphism Challenge! ---

# This is the base class for all vehicles.
class Vehicle:
    """A generic vehicle with a default move action."""

    def move(self):
        """A generic move method for any vehicle."""
        print("The vehicle is moving.")


# These are the subclasses that will inherit from Vehicle.
class Car(Vehicle):
    """A car that drives."""

    # This method overrides the parent's move() method.
    def move(self):
        print("The car is driving. 🚗")


class Plane(Vehicle):
    """A plane that flies."""

    def move(self):
        print("The plane is flying. ✈️")


class Boat(Vehicle):
    """A boat that sails."""

    def move(self):
        print("The boat is sailing. 🚤")


# Now, let's demonstrate polymorphism!
# We create a list containing different types of objects,
# but they all belong to a shared parent class (Vehicle).
vehicles = [Car(), Plane(), Boat(), Vehicle()]

print("--- Activity 2: Polymorphism in Action ---")
# We can loop through the list and call the same method (move()) on each object.
# Python automatically knows which version of move() to call based on the object's type.
# This is the power of polymorphism!
for vehicle in vehicles:
    vehicle.move()
