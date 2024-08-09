
import random


class Color:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RED = '\033[0;31m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'
    DARK_GRAY = '\033[1;30m'
    BOLD_RED = '\033[1;31m'
    DARK_RED = '\033[0;35m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'
    LIGHT_YELLOW = '\033[38;2;220;220;180m'  # Example of adding a custom RGB color




def print_inscription_logo():
    # Estimated RGB value for the light green/yellow color
    print("\033[38;2;220;220;180m")
    print("\033==============================================================================================================\033[0m")
    print("\033[38;2;220;220;180m" + r"""
    ███╗ ███╗  ███╗ ╔██████╗  ╔██████╗  ██████╗            ███████╗            ╔███  ╔██████╗   ██╗    ╔██
    ╚██║  ███╗  ██║ ██╔════╝ ╔██╔═══██║ ╚█╔══██║ ██╗   ██╗ ╚██╔══██╗ ████████╗ ║██╝ ╔██╔═══██╗  ████╗  ██║
     ██║  █╔██╗ ██║ ╔█████╗  ██║         █║ ██╔╝  ██║ ██╔╝  ██████╔╝ ╚══██╔══╝ ║██  ███║   ███║ ██╔██╗ ██║
    ╔██║  █║╚██╗██║ ╚════██║ ╚██╚═══██║  █║  ██║   ╚██╔╝    ██╔═══╝     ██║    ║██╗ ╚██║   ██║  ██║╚██╗██║
    ███║ ██║ ╚████║ ██████╔╝  ╚██████╔╝ ██║   ██║   ██║    ╔██║         ██║    ║███  ╚██████╔╝  ███║ ╚███║
    ╚══╝ ╚═╝  ╚═══╝ ╚═════╝    ╚═════╝  ╚═╝   ╚═╝   ██║   ╔█╔═╝        ╔██║    ╚══╝   ╚═════╝   ╚═╝   ╚══╝
                                ⌟⎽⌞    ⌟_=          ╚═╝   ╚╝  ⌟⎼==⎼_   ╚═╝   
                       _⌟    ⎽╔╝███╚╗⎻═███╚╗⎼╗  ⌟╔═╗⌞  .   ` ╔███⎺⌝╚═╝╗
                 ⎺⎻=═╝███╔╝═⎺╝ ⌝╚═╝⌜   ⌝╚═╝⌜⎺╚═██████║    .⌞ ⌜  ⌝      ╚= _  ⌟╔═╗⌞ 。
                                               ⌝╚═███╝                     ⎺=██╔╝
    """ + "\033[0m")
    print("\033[38;2;220;220;180m                                        press any button to start.\033[38;2;220;220;180m")
    print("\033\n==============================================================================================================\033[0m")

def game_start_banner():
    banner = f"""
    {Color.DARK_GRAY}
    Welcome to the world of {Color.BOLD_RED}Dark Asylum{Color.ENDC}{Color.DARK_GRAY},
    where your courage will be tested against the darkest creatures.
    {Color.ENDC}
    """
    print(banner)

def print_card_art(name):
    art = f"""
    {Color.RED}{name}{Color.ENDC}
    ------
   |      |
   |  /\  |
   | <  > |
   |  \/  |
   |      |
    ------
    """
    print(art)


class Card:
    def __init__(self, name, attack, health, cost, bone_cost=0, abilities=None, description=""):
        self.name = name
        self.attack = attack
        self.health = health
        self.cost = cost
        self.bone_cost = bone_cost
        self.abilities = abilities if abilities else []
        self.description = description

    def apply_abilities(self, target):
        if "Flying" in self.abilities:
            print("There is a BUG")

        if "Undying" in self.abilities and self.health <= 0:
            print("There is a BUG")

    # Logic for undying, e.g., return to hand instead of dying

    def __str__(self):
        card_icon = "🂠"
        abilities_desc = ', '.join(self.abilities) if self.abilities else "No special abilities"
        return (f"{card_icon} {Color.CYAN}{self.name}{Color.ENDC} | "
                f"{Color.GREEN}ATK: {self.attack}{Color.ENDC} | "
                f"{Color.RED}HP: {self.health}{Color.ENDC} | "
                f"{Color.MAGENTA}Cost: {self.cost}{Color.ENDC} | "
                f"{Color.YELLOW}Bones: {self.bone_cost}{Color.ENDC} | "  # Show bone cost
                f"{Color.YELLOW}Abilities: {abilities_desc}{Color.ENDC}")

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.board = []
        self.health = 10
        self.total_damage_dealt = 0
        self.blood = 0
        self.bones = 0
        self.energy = 3  # Example for energy

    def sacrifice_creature(self, card):
        self.blood += card.cost
        self.board.remove(card)
        print(f"{Color.RED}{card.name} was sacrificed. {self.blood} blood gained.{Color.ENDC}")

    def draw_card(self, card):
        self.hand.append(card)
        print(f"{Color.YELLOW}{self.name}{Color.ENDC} draws: {Color.CYAN}{card.name}{Color.ENDC} ⌼")

    def play_card(self, card_index):
        card = self.hand[card_index]


        # Check if the player has enough bones
        if card.bone_cost > self.bones:
            print(f"{Color.RED}Not enough bones to summon {card.name}! It requires {card.bone_cost} bones.{Color.ENDC}")
            return False

        # Check if the player has enough creatures to sacrifice
        if len(self.board) < card.cost:
            print(
                f"{Color.RED}Not enough creatures to sacrifice! {card.name} requires {card.cost} sacrifices.{Color.ENDC}")
            return False

        if len(self.board) < card.cost:
            print(f"{Color.RED}Not enough creatures to sacrifice! {card.name} requires {card.cost} sacrifices.{Color.ENDC}")
            return False

        sacrifices = []
        while len(sacrifices) < card.cost:
            self.show_board()
            sacrifice_index = int(safe_input(f"{Color.RED}Select a creature to sacrifice (index): {Color.ENDC}"))
            if 0 <= sacrifice_index < len(self.board):
                sacrifices.append(sacrifice_index)
            else:
                print(f"{Color.RED}Invalid selection!{Color.ENDC}")

        if hasattr(card, 'bone_cost') and self.bones < card.bone_cost:
            print(f"{Color.RED}Not enough bones! {card.name} requires {card.bone_cost} bones to play.{Color.ENDC}")
            return False

        if hasattr(card, 'bone_cost'):
            self.bones -= card.bone_cost
            print(f"{Color.YELLOW}You lost {card.bone_cost} bones!{Color.ENDC}")  #

        for index in sorted(sacrifices, reverse=True):
            sacrificed_card = self.board.pop(index)
            print(f"{Color.RED}Sacrificed {sacrificed_card.name}.{Color.ENDC} 🩸")
            self.bones += 1  # Award a bone
            print(f"{Color.YELLOW}Your bone +1{Color.ENDC}")  # Notify player

        self.hand.pop(card_index)
        self.board.append(card)
        self.bones -= card.bone_cost  # Deduct the bone cost when the card is played
        print(f"{Color.GREEN}{self.name} plays {card.name} on the board.{Color.ENDC} ⌼")

        # Automatically display the hand after summoning a card
        self.show_hand()
        return True

    def show_hand(self):
        print(f"{Color.MAGENTA}{self.name}'s Hand:{Color.ENDC}")
        for i, card in enumerate(self.hand):
            print(f"{i}: {card}")
        print(f"{Color.YELLOW}Bones: {self.bones}{Color.ENDC}")  # Display the number of bones the player has
        print("==============================================================================================================")

    def show_board(self):

        print(f"{Color.BLUE}{self.name}'s Board:{Color.ENDC}")

        for i, card in enumerate(self.board):
            print(f"{i}: {card}")
        print(f"{Color.YELLOW}Bones: {self.bones}{Color.ENDC}")  # Display the number of bones the player has
        print("==============================================================================================================")

    def remove_dead_creatures(self):
        self.board = [card for card in self.board if card.health > 0]

        # Automatically display the hand after summoning a card
        self.show_hand()
        return True

    def show_hand(self):
        print(f"{Color.MAGENTA}{self.name}'s Hand:{Color.ENDC}")
        for i, card in enumerate(self.hand):
            print(f"{i}: {card}")
        print("==============================================================================================================")

    def show_board(self):
        print(f"{Color.BLUE}{self.name}'s Board:{Color.ENDC}")
        for i, card in enumerate(self.board):
            print(f"{i}: {card}")
        print("==============================================================================================================")

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.opponent = player2
        self.deck = [
            Card("Wolf", 3, 2, 2),
            Card("Stinkbug", 1, 2, 1), Card("Mantis", 1, 1, 1, ["Double Strike"]),
            Card("Bear", 4, 6, 3),
            Card("Hawk", 2, 1, 4, ["Flying"]),
            Card("Squirrel", 0, 1, 0, description="Can be sacrificed for no cost."),
            Card("Stoat", 1, 3, 1),
            Card("Elk", 2, 4, 2),
            Card("Bone Hound", 2, 2, 0, bone_cost=2, abilities=["Guard"]),
            Card("skeleten", 1, 1, 0, bone_cost=1)

        ]
        random.shuffle(self.deck)

    def setup(self):
        print_inscription_logo()
        input("Press Enter to start the game...")
        # Draw two random creature cards and one Squirrel card for each player
        for _ in range(2):
            self.player1.draw_card(self.deck.pop())
            self.player2.draw_card(self.deck.pop())
        # Ensure each player gets a Squirrel card
        squirrel1 = next((card for card in self.deck if card.name == "Squirrel"), None)
        if not squirrel1:
            squirrel1 = Card("Squirrel", 0, 1, 0, description="Can be sacrificed for no cost.")
        self.player1.draw_card(squirrel1)

        squirrel2 = next((card for card in self.deck if card.name == "Squirrel"), None)
        if not squirrel2:
            squirrel2 = Card("Squirrel", 0, 1, 0, description="Can be sacrificed for no cost.")
        self.player2.draw_card(squirrel2)

    def draw_phase(self):
        print(f"{Color.BLUE}{self.current_player.name}'s Draw Phase:{Color.ENDC}")
        choice = safe_input(f"{Color.YELLOW}Choose '1' to draw a creature card, '2' to draw a Squirrel: {Color.ENDC}",
                            ['1', '2'])
        print(
            "--------------------------------------------------------------------------------------------------------------")
        if choice == '1':
            # Draw a random creature card
            creature_card = next((card for card in self.deck if card.name != "Squirrel"), None)
            if creature_card:
                self.current_player.draw_card(creature_card)
            else:
                print(f"{Color.RED}No creature cards left in the deck!{Color.ENDC}")
        elif choice == '2':
            # Ensure a Squirrel card is available or create a new one
            squirrel_card = next((card for card in self.deck if card.name == "Squirrel"), None)
            if not squirrel_card:
                print(f"{Color.YELLOW}No Squirrel cards left, creating a new Squirrel card.{Color.ENDC}")
                squirrel_card = Card("Squirrel", 0, 1, 0, description="Can be sacrificed for no cost.")
            self.current_player.draw_card(squirrel_card)
        print(
            "--------------------------------------------------------------------------------------------------------------")

    def play_turn(self):
        self.draw_phase()
        print(f"{Color.GREEN}{self.current_player.name}'s Turn:{Color.ENDC}")
        self.current_player.show_hand()
        while True:
            action = safe_input(f"{Color.YELLOW}Choose 'play', 'done', or 'show' to view hand/board: {Color.ENDC}",
                                ['play', 'done', 'show'])
            if action == 'play':
                card_index = int(safe_input("Enter the index of the card to play: "))
                if self.current_player.play_card(card_index):
                    continue
            elif action == 'show':
                self.current_player.show_hand()
                self.current_player.show_board()
            elif action == 'done':
                print(f"{self.current_player.name} ends their turn.")
                break
        print(
            "==============================================================================================================")

    def combat_phase(self):
        if not self.current_player.board or not self.opponent.board:
            print(f"{Color.RED}No creatures to engage in combat!{Color.ENDC}")
            return
        print(f"\n{Color.MAGENTA}Combat Phase!{Color.ENDC}")
        opponent_alive_cards = [card for card in self.opponent.board if card.health > 0]

        for player_card in self.current_player.board:
            if opponent_alive_cards:
                target = opponent_alive_cards[0]  # Simplified targeting: always hit the first live opponent card
                damage_dealt = min(player_card.attack, target.health)
                target.health -= damage_dealt
                print(
                    f"{Color.CYAN}{player_card.name}{Color.ENDC} attacks {Color.CYAN}{target.name}{Color.ENDC} and deals {damage_dealt} damage.")
                if target.health <= 0:
                    print(f"{Color.RED}{target.name} is destroyed!{Color.ENDC}")
                    opponent_alive_cards.remove(target)
                    self.opponent.bones += 1  # Gain a bone when a creature is destroyed
                    self.opponent.board.remove(target)  # Remove the destroyed card from the board
            else:
                break  # No opponent creatures to attack

        if not opponent_alive_cards:
            total_damage = sum(card.attack for card in self.current_player.board)
            self.opponent.health -= total_damage
            print(
                f"{Color.GREEN}{self.current_player.name} deals {total_damage} direct damage to {self.opponent.name}.{Color.ENDC}")
            print(f"{Color.RED}{self.opponent.name} has {self.opponent.health} health remaining.{Color.ENDC}")
        print(
            "--------------------------------------------------------------------------------------------------------------")


        if not self.opponent.board:
            # Opponent has no creatures on the board, direct damage to the opponent's health
            total_damage = sum(card.attack for card in self.current_player.board)
            self.opponent.health -= total_damage
            print(
                f"{Color.GREEN}{self.current_player.name} deals {total_damage} direct damage to {self.opponent.name}.{Color.ENDC}")
            print(f"{Color.RED}{self.opponent.name} has {self.opponent.health} health remaining.{Color.ENDC}")
        else:
            # Combat phase where creatures attack opposing creatures
            opponent_alive_cards = [card for card in self.opponent.board if card.health > 0]

            for player_card in self.current_player.board:
                if opponent_alive_cards:
                    target = opponent_alive_cards[0]  # Simplified targeting: always hit the first live opponent card
                    damage_dealt = min(player_card.attack, target.health)
                    target.health -= damage_dealt
                    print(
                        f"{Color.CYAN}{player_card.name}{Color.ENDC} attacks {Color.CYAN}{target.name}{Color.ENDC} and deals {damage_dealt} damage.")
                    if target.health <= 0:
                        print(f"{Color.RED}{target.name} is destroyed!{Color.ENDC}")
                        self.opponent.board.remove(target)  # Remove only the specific instance that was killed
                        opponent_alive_cards.remove(target)
                else:
                    break  # No opponent creatures to attack

            self.opponent.remove_dead_creatures()  # Clean up the opponent's board after combat

            # After attacking creatures, check if any damage can be dealt to the opponent's health
            if not opponent_alive_cards:
                total_damage = sum(card.attack for card in self.current_player.board)
                self.opponent.health -= total_damage
                print(
                    f"{Color.GREEN}{self.current_player.name} deals {total_damage} direct damage to {self.opponent.name}.{Color.ENDC}")
                print(f"{Color.RED}{self.opponent.name} has {self.opponent.health} health remaining.{Color.ENDC}")

        print(
            "--------------------------------------------------------------------------------------------------------------")

    def is_game_over(self):
        return self.player1.health <= 0 or self.player2.health <= 0

    def declare_winner(self):
        if self.player1.health <= 0:
            print(f"{Color.RED}{self.player2.name} wins!{Color.ENDC} 🎉")
        elif self.player2.health <= 0:
            print(f"{Color.RED}{self.player1.name} wins!{Color.ENDC} 🎉")
        else:
            print(f"{Color.YELLOW}It's a draw!{Color.ENDC} 🤝")
        print("==============================================================================================================")


    def setup(self):
        print_inscription_logo()
        input("Press Enter to start the game...")
        # Draw two random creature cards and one Squirrel card for each player
        for _ in range(2):
            self.player1.draw_card(self.deck.pop())
            self.player2.draw_card(self.deck.pop())
        # Ensure each player gets a Squirrel card
        squirrel1 = next((card for card in self.deck if card.name == "Squirrel"), None)
        if not squirrel1:
            squirrel1 = Card("Squirrel", 0, 1, 0, description="Can be sacrificed for no cost.")
        self.player1.draw_card(squirrel1)

        squirrel2 = next((card for card in self.deck if card.name == "Squirrel"), None)
        if not squirrel2:
            squirrel2 = Card("Squirrel", 0, 1, 0, description="Can be sacrificed for no cost.")
        self.player2.draw_card(squirrel2)

    def draw_phase(self):
        print(f"{Color.BLUE}{self.current_player.name}'s Draw Phase:{Color.ENDC}")
        choice = safe_input(f"{Color.YELLOW}Choose '1' to draw a creature card, '2' to draw a Squirrel: {Color.ENDC}",
                            ['1', '2'])
        print(
            "--------------------------------------------------------------------------------------------------------------")
        if choice == '1':
            # Draw a random creature card
            creature_card = next((card for card in self.deck if card.name != "Squirrel"), None)
            if creature_card:
                self.current_player.draw_card(creature_card)
            else:
                print(f"{Color.RED}No creature cards left in the deck!{Color.ENDC}")
        elif choice == '2':
            # Ensure a Squirrel card is available or create a new one
            squirrel_card = next((card for card in self.deck if card.name == "Squirrel"), None)
            if not squirrel_card:
                print(f"{Color.YELLOW}No Squirrel cards left, creating a new Squirrel card.{Color.ENDC}")
                squirrel_card = Card("Squirrel", 0, 1, 0, description="Can be sacrificed for no cost.")
            self.current_player.draw_card(squirrel_card)
        print(
            "--------------------------------------------------------------------------------------------------------------")

    def play_turn(self):
        self.draw_phase()
        print(f"{Color.GREEN}{self.current_player.name}'s Turn:{Color.ENDC}")
        self.current_player.show_hand()
        while True:
            action = safe_input(f"{Color.YELLOW}Choose 'play', 'done', or 'show' to view hand/board: {Color.ENDC}",
                                ['play', 'done', 'show'])
            if action == 'play':
                card_index = int(safe_input("Enter the index of the card to play: "))
                if self.current_player.play_card(card_index):
                    continue
            elif action == 'show':
                self.current_player.show_hand()
                self.current_player.show_board()
            elif action == 'done':
                print(f"{self.current_player.name} ends their turn.")
                break
        print(
            "==============================================================================================================")

    def combat_phase(self):
        if not self.current_player.board or not self.opponent.board:
            print(f"{Color.RED}No creatures to engage in combat!{Color.ENDC}")
            return

        print(f"\n{Color.MAGENTA}Combat Phase!{Color.ENDC}")
        opponent_alive_cards = [card for card in self.opponent.board if card.health > 0]

        for player_card in self.current_player.board:
            if opponent_alive_cards:
                target = opponent_alive_cards[0]  # Simplified targeting: always hit the first live opponent card
                damage_dealt = min(player_card.attack, target.health)
                target.health -= damage_dealt
                print(
                    f"{Color.CYAN}{player_card.name}{Color.ENDC} attacks {Color.CYAN}{target.name}{Color.ENDC} and deals {damage_dealt} damage.")
                if target.health <= 0:
                    print(f"{Color.RED}{target.name} is destroyed!{Color.ENDC}")
                    opponent_alive_cards.remove(target)
                    self.opponent.bones += 1  # Gain a bone when a creature is destroyed
                    print(f"{Color.YELLOW}Your bone +1{Color.ENDC}")  # Notify player
                    self.opponent.board.remove(target)  # Remove the destroyed card from the board
            else:
                break  # No opponent creatures to attack

        if not opponent_alive_cards:
            total_damage = sum(card.attack for card in self.current_player.board)
            self.opponent.health -= total_damage
            print(
                f"{Color.GREEN}{self.current_player.name} deals {total_damage} direct damage to {self.opponent.name}.{Color.ENDC}")
            print(f"{Color.RED}{self.opponent.name} has {self.opponent.health} health remaining.{Color.ENDC}")
        print(
            "--------------------------------------------------------------------------------------------------------------")




        if not self.opponent.board:
            # Opponent has no creatures on the board, direct damage to the opponent's health
            total_damage = sum(card.attack for card in self.current_player.board)
            self.opponent.health -= total_damage
            print(
                f"{Color.GREEN}{self.current_player.name} deals {total_damage} direct damage to {self.opponent.name}.{Color.ENDC}")
            print(f"{Color.RED}{self.opponent.name} has {self.opponent.health} health remaining.{Color.ENDC}")
        else:
            # Combat phase where creatures attack opposing creatures
            opponent_alive_cards = [card for card in self.opponent.board if card.health > 0]


            self.opponent.remove_dead_creatures()  # Clean up the opponent's board after combat


        print(
            "--------------------------------------------------------------------------------------------------------------")

    def is_game_over(self):
        return self.player1.health <= 0 or self.player2.health <= 0

    def declare_winner(self):
        if self.player1.health <= 0:
            print(f"{Color.RED}{self.player2.name} wins!{Color.ENDC} 🎉")
        elif self.player2.health <= 0:
            print(f"{Color.RED}{self.player1.name} wins!{Color.ENDC} 🎉")
        else:
            print(f"{Color.YELLOW}It's a draw!{Color.ENDC} 🤝")
        print("==============================================================================================================")


def safe_input(prompt, valid_responses=None):
    """
    Safely handles user input with optional validation against specific responses.

    Args:
    - prompt (str): The message displayed to the user.
    - valid_responses (list): Optional list of valid responses. If provided, the function will only accept these responses.

    Returns:
    - str: A valid response from the user.
    """
    while True:
        user_input = input(prompt)
        if valid_responses is None or user_input in valid_responses:
            return user_input
        else:
            print(f"Invalid input. Please enter one of the following: {', '.join(valid_responses)}")


def main():
    game = Game(Player("Player 1"), Player("Player 2"))
    game.setup()
    while not game.is_game_over():
        game.play_turn()
        game.combat_phase()
        if game.is_game_over():
            game.declare_winner()
            break
        game.current_player, game.opponent = game.opponent, game.current_player

if __name__ == "__main__":
    main()