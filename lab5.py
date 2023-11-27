"""
Fill your aquarium with fish you\'ve created
"""
class Fish:
    """
    Creates a Fish object
    """
    def __init__(self, name = '', age = 1, is_agressive = False, needed_space = 0.1):
        """
        Initialization
        """
        self.__name = name
        self.__age = age
        self.__species = []
        self.__size = 1
        self.__preffered_food = []
        self.__is_agressive = is_agressive
        self.__needed_space = needed_space
    def __del__(self):
        """
        Destructor
        """
        #print(f"destroyed {self.__name}")
    def __str__(self):
        """
        Returns a string that contains a describtion of a fish
        """
        return f'Рибка {self.__name}: вага {self.__size}кг, агресивна: {self.__is_agressive}'
    def __repr__(self):
        """
        Returns a string that contains Fish object constructor
        """
        return f'Fish(\'{self.__name}\', {self.__age}, {self.__is_agressive}, \
{self.__needed_space})'

    def __eq__(self, fish) -> bool:
        return (self.__name == fish.get_name()) and (self.__age == fish.get_age()) and \
            (self.__needed_space == fish.get_needed_space())

    def set_name(self, name: str):
        """
        Set name
        """
        self.__name = name

    def set_age(self, age):
        """
        Set age
        """
        self.__age = age

    def set_needed_space(self, needed_space):
        """
        Set needed space
        """
        self.__needed_space = needed_space

    def set_size(self, size):
        """
        Set size
        """
        self.__size = size

    def get_name(self):
        """
        Returns a Fis\'s name
        """
        return self.__name

    def get_age(self):
        """
        Returns the age of a Fish
        """
        return self.__age

    def get_species(self):
        """
        Returns a list of species of the Fish
        """
        return self.__species

    def get_size(self):
        """
        Returns the size of Fish
        """
        return self.__size

    def get_preffered_food(self):
        """
        Returns the list of preffered food of the Fish
        """
        return self.__preffered_food

    def get_agressive_status(self):
        """
        Returns True if the Fish is agressive
        """
        return self.__is_agressive

    def get_needed_space(self):
        """
        Returns needed space of the Fish
        """
        return self.__needed_space

class Aquarium:
    """
    Create an Aquarium object
    """
    def __init__(self, total_volume = 3.6, is_agressive = None):
        """
        initialization
        """
        self.__total_volume = total_volume
        self.__free_space = self.__total_volume
        self.__fishes = []
        self.__is_agressive = is_agressive

    def __del__(self):
        """
        destructor
        """
        print("aquarium was broken")

    def __str__(self):
        """
        string
        """
        return f"Рибки {', '.join([fish.get_name() for fish in self.__fishes])} в акваріумі на \
{self.__total_volume} займають {self.__total_volume - self.__free_space}"

    def __repr__(self):
        """
        repr
        """
        return f'Aquarium({self.__total_volume})'

    def add_fish(self, *args: Fish):
        """
        Adds a fish in an aquarium
        """
        for fish in args:
            if fish.get_needed_space() <= self.__free_space:
                if self.__is_agressive is None:
                    self.__is_agressive = fish.get_agressive_status()
                    self.__fishes.append(fish)
                    self.__free_space -= fish.get_needed_space()
                    print(f"Рибку {fish.get_name()} закинуто в акваріум. Вільно: \
{round(self.__free_space, 3)}")
                elif fish.get_agressive_status() == self.__is_agressive:
                    self.__fishes.append(fish)
                    self.__free_space -= fish.get_needed_space()
                    print(f"Рибку {fish.get_name()} закинуто в акваріум. Вільно: \
{round(self.__free_space, 3)}")
                else:
                    if self.__is_agressive:
                        print(f"[!] в акваріум не можна закинути рибку {fish.get_name()}: \
акваріум агресивний, рибка мирна")
                    else:
                        print(f"[!] в акваріум не можна закинути рибку {fish.get_name()}: \
акваріум мирний, рибка агресивна")
            else:
                print(f"[!] Рибка {fish.get_name()}({round(fish.get_needed_space(), 3)}) \
не влізе в акваріум! (вільно: {round(self.__free_space, 3)})")

    def get_fishes(self):
        """
        Returns a tuple of fishes that are in current aquarium
        """
        return self.__fishes

    def could_place_fish(self, fish: Fish) -> bool:
        """
        Returns True if u can place fish in the aquarium
        """
        return fish.get_needed_space() <= self.__free_space

    def top_three_by_size(self):
        """
        Returns a tuple that contains TOP-3 by size fish
        """
        fishes = self.__fishes.copy()
        fishes.sort(key = lambda x: x.get_size(), reverse = True)
        result = []
        for index, item in enumerate(fishes):
            if index == 3:
                break
            result.append(item)
        return tuple(result)
