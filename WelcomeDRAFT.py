import pygame

class Welcome:
    def __init__(self, screen=None):
        if screen is None:
            screen = pygame.display.set_mode((1920, 1080))
        self.screen = screen
        self.font = pygame.font.SysFont('Arial', 50)
        self.text = self.font.render('Welcome to the Game!', True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.text, self.text_rect)

    def update(self):
        pass
pygame.init()

print("Welcome to the Game!")
print("Press any key to continue...")
welcome_screen = Welcome()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            running = False

    welcome_screen.draw()
    pygame.display.flip()
pygame.quit()
print("Starting the game...")
print("PLAY")
print("EXIT")
user_input = input("Enter your choice: ")
if user_input.lower() == "play":
    print("Game is starting...")
elif user_input.lower() == "exit":
    print("Exiting the game...")
else:    print("Invalid choice. Exiting the game...")
button_screen = pygame.display.set_mode((1920, 1080))
button_font = pygame.font.SysFont('Arial', 40)
play_button = button_font.render('PLAY', True, (255, 255, 255))
exit_button = button_font.render('EXIT', True, (255, 255, 255))     
Rrunning = True
play_button_rect = play_button.get_rect(center=(button_screen.get_width() // 2, button_screen.get_height() // 2 - 50))
exit_button_rect = exit_button.get_rect(center=(button_screen.get_width() // 2, button_screen.get_height() // 2 + 50))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if play_button_rect.collidepoint(mouse_pos):
                print("Game is starting...")
                running = False
            elif exit_button_rect.collidepoint(mouse_pos):
                print("Exiting the game...")
                running = False

    button_screen.fill((0, 0, 0))
    button_screen.blit(play_button, play_button_rect)
    button_screen.blit(exit_button, exit_button_rect)
    pygame.display.flip()
pygame.quit()