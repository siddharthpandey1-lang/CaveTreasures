import pygame

pygame.init()

class Welcome:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont('Arial', 50)
        self.text = self.font.render('Welcome to the Game!', True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.text, self.text_rect)

# --- Setup ---
screen = pygame.display.set_mode((800, 600))  # smaller window for testing
pygame.display.set_caption("Game Menu")

# --- Welcome Screen ---
welcome_screen = Welcome(screen)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            running = False

    welcome_screen.draw()
    pygame.display.flip()

# --- Button Menu ---
font = pygame.font.SysFont('Arial', 40)
play_button = font.render('PLAY', True, (255, 255, 255))
exit_button = font.render('EXIT', True, (255, 255, 255))
play_button_rect = play_button.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 50))
exit_button_rect = exit_button.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 50))
running = True
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

    screen.fill((0, 0, 0))
    screen.blit(play_button, play_button_rect)
    screen.blit(exit_button, exit_button_rect)
    pygame.display.flip()
pygame.quit()