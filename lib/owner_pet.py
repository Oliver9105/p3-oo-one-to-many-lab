class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Must be one of {Pet.PET_TYPES}")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Returns a list of the owner's pets."""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Assigns an owner to a pet if it's an instance of the Pet class."""
        if not isinstance(pet, Pet):
            raise Exception("Invalid pet: Must be an instance of the Pet class")
        pet.owner = self

    def get_sorted_pets(self):
        """Returns the owner's pets sorted alphabetically by name."""
        return sorted(self.pets(), key=lambda pet: pet.name)
