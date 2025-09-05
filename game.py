import pygame
# Initialize required modules
pygame.init()

# Setup window geometry
screen = pygame.display.set_mode((400, 500))

# Create a loop to run till the game is quit by the user
done = False

# Initialize font, render text, and set text position
text = pygame.font.Font(None, 48).render(
    'Welcome to the Adventure!', True, pygame.Color('black')
)
text_rect = text.get_rect(center=(400 // 2, 300 // 2))

while not done:
    # Clear the event queue
    for event in pygame.event.get():
        # Check for QUIT event
        if event.type == pygame.QUIT:
            pygame.quit()
            done = True

    # Fill background
    screen.fill((200, 230, 255))

    # Draw text
    screen.blit(text, text_rect)

    # Make the changes visible
    pygame.display.flip()
