class Pokemon: 
    def __init__(self, name, type) -> None:
        self.__name = name
        self.__type = type
        
    def __str__(self) -> str:
        return self.__name
    
    def __eq__(self, __value: object) -> bool:
        return __value == self.__name
    
    def eat(self, berry) -> str:
        return f"{self.__name} eats {berry}"
    
    def attack(self, enemy) -> str:
        return f"{self.__name} attacks {enemy}"
    
    @property
    def type(self) -> str:
        return self.__type
    
    @property
    def name(self) -> str:
        return self.__name

class Badges:
    def __init__(self, name, gym) -> None:
        self.__name = name
        self.__gym = gym
    
    def __str__(self):
        return self.__name
    
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def gym(self) -> str:
        return self.__gym
    
class Trainer:
    def __init__(self, name) -> None:
        self.__name = name
        self.__trainerBadges = []
        self.__pokemon = []
        
    def __str__(self) -> str:
        return self.__name
        
    def addBadges(self, badge) -> None:
        self.__trainerBadges.append(badge)
        
    def addPokemon(self, pokemon) -> None:
        self.__pokemon.append(pokemon)
        
    def __searchPokemon(self, pokemon) -> Pokemon:
        if pokemon in self.__pokemon:
            index = self.__pokemon.index(pokemon)
            return self.__pokemon[index]
        return None
        
    def feed(self, pokemon, berry) -> str:
        poke = self.__searchPokemon(pokemon)
        return f"{self.__name} feeds {poke}: {poke.eat(berry)}"
    
    def attack(self, pokemon, enemy) -> str:
        dialogue = f"{self.__name}'s pokemon attacks: "
        poke = self.__searchPokemon(pokemon)
        dialogue += poke.attack(enemy)
        return dialogue
    
    def showbadges(self) -> None:
        print(f"{self.__name}'s Badges: ")
        for i in self.__trainerBadges:
            print(i.name)
            
    @property
    def name(self):
        return self.__name
    
def main():
    
    trainer = Trainer("Ash")
    trainer.addPokemon(Pokemon("Pikachu", "Electric"))
    trainer.addPokemon(Pokemon("Greninja", "Water"))
    trainer.addBadges(Badges("Rock Badge", "Brock's Gym"))
    trainer.addBadges(Badges("Water Badge", "Misty's Gym"))
    
    print(trainer)
    print(trainer.attack("Greninja", "Zoobat"))
    print(trainer.feed("Pikachu", "Lala Berry"))
    
    trainer.showbadges()

main()