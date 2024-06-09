class Player_One:
    def __init__(self):
        self.lat = int(input("Player 1: Enter a latitude between 1 and 100: "))
        self.long = int(input("Player 1: Enter a longitudinal starting point between 1 and 85: "))
        self.size = int(input("Player 1: Enter a size between 1 and 15: "))
        self.coordinates = []

    def create_coordinates(self):
        lat = [self.lat for i in range(self.size)]
        long = list(range(self.long, (self.long + self.size)))
        self.coordinates += zip(lat, long)
        return self.coordinates
    
    def attack(self, lat, long):
        if (lat, long) in battleship_two.coordinates:
            battleship_two.coordinates.pop(battleship_two.coordinates.index((lat, long)))
            if len(battleship_two.coordinates) == 0:
                print("You sunk my battleship!")
                print("                              ")
            else:
                print("You hit my battleship!")
                print("                                 ")
        else:
            print("miss")
            print("                  ")
    
class Player_Two:
    def __init__(self):
        self.lat = int(input("Player 2: Enter a latitude between 1 and 100: "))
        self.long = int(input("Player 2: Enter a longitudinal starting point between 1 and 85: "))
        self.size = int(input("Player 2: Enter a size between 1 and 15: "))
        self.coordinates = []

    def create_coordinates(self):
        lat = [self.lat for i in range(self.size)]
        long = list(range(self.long, (self.long + self.size)))
        self.coordinates += zip(lat, long)
        return self.coordinates
    
    def attack(self, lat, long):
        if (lat, long) in battleship_one.coordinates:
            battleship_one.coordinates.pop(battleship_one.coordinates.index((lat, long)))
            if len(battleship_one.coordinates) == 0:
                print("You sunk my battleship!")
                print("                                 ")
            else:
                print("You hit my battleship!")
                print("                           ")
        else:
            print("miss")
            print("                            ")

battleship_one = Player_One()
print("---------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("------------------------------------------------------NEXT PLAYER----------------------------------------------------------------------------------------------")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("---------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("------------------------------------------------------NEXT PLAYER----------------------------------------------------------------------------------------------")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                               N   N  EEEEE  X   X  TTTTT      PPPP   L        A    Y   Y  EEEEE  RRRR ")
print("                               NN  N  E      X   X    T        P   P  L       A A    Y Y   E      R   R")
print("                               N N N  E       X X     T        P   P  L      A   A    Y    E      R   R")
print("                               N  NN  EEE      X      T        PPPP   L      AAAAA    Y    EEE    RRRR ")
print("                               N   N  E       X X     T        P      L      A   A    Y    E      R R  ")
print("                               N   N  E      X   X    T        P      L      A   A    Y    E      R  R ")
print("                               N   N  EEEEE  X   X    T        P      LLLLL  A   A    Y    EEEEE  R   R")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("---------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("------------------------------------------------------NEXT PLAYER----------------------------------------------------------------------------------------------")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("---------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("------------------------------------------------------NEXT PLAYER----------------------------------------------------------------------------------------------")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")

battleship_two = Player_Two()
print("---------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------ATTACK------------------------------------------------------------------------------------------------")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("---------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------ATTACK------------------------------------------------------------------------------------------------")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                              A    TTTTT  TTTTT    A     CCC   K   K")
print("                                             A A     T      T     A A   C   C  K  K ")
print("                                            A   A    T      T    A   A  C      K K  ")
print("                                            AAAAA    T      T    AAAAA  C      KK   ")
print("                                            A   A    T      T    A   A  C      K K  ")
print("                                            A   A    T      T    A   A  C   C  K  K ")
print("                                            A   A    T      T    A   A   CCC   K   K")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("---------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------ATTACK------------------------------------------------------------------------------------------------")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("---------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------ATTACK------------------------------------------------------------------------------------------------")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")
print("                                                                                                                                                               ")

battleship_one.create_coordinates()
battleship_two.create_coordinates()

def attack_prompt(player):
    if player == 1:
        return battleship_one.attack(lat = int(input("Choose a latitude to attack: ")), long = int(input("Choose a longitude to attack: ")))
    elif player == 2:
        return battleship_two.attack(lat = int(input("Choose a latitude to attack: ")), long = int(input("Choose a longitude to attack: ")))
    
while len(battleship_one.coordinates) > 0 and len(battleship_two.coordinates) > 0:
    attack_prompt(player = int(input("Enter player number: ")))
else:
    print("Game Over")

#battleship_one.attack(lat = int(input("Choose a latitude: ")), long = int(input("Choose a longitude: ")))