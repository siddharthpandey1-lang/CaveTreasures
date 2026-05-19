import pygame 
class Welcome:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont('Arial', 50)
        self.text = self.font.render('Welcome to the Game!', True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

    def draw(self):
        self.screen.fill((0, 0, 0))  # Clear the screen with black
        self.screen.blit(self.text, self.text_rect)  # Draw the welcome text
    def update(self):
        pass  # No updates needed for the welcome screen

    print("Loading welcome screen")
print("CAVE TREASURES")
print("PLAY")
print("EXIT")

user_input = input("Enter your choice: ")
if user_input == "PLAY":
    print("Starting the game...")
elif user_input == "EXIT":
    print("Exiting the game...")
else:
    print("Invalid choice. Please enter 'PLAY' or 'EXIT'.")

class Welcome:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont('Arial', 50)
        self.text = self.font.render('Welcome to the Game!', True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

    def draw(self):
        self.screen.fill((0, 0, 0))  # Clear the screen with black
        self.screen.blit(self.text, self.text_rect)  # Draw the welcome text

    def update(self):
        pass  # No updates needed for the welcome screen