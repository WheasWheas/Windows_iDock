import pygame
import random

pygame.init()
WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

def main():
    running = True
    x, y = WIDTH // 2, HEIGHT // 2  # Initial position of the snake
    velocity = 15  # Speed of the snake
    dx, dy = 0, 0  # Direction of movement

    apple_x, apple_y = 100, 100
    
    apple_size = 20  # Size of the apple
    score = 0  # Initialize score

    def spawn_apple():
        return random.randint(0, WIDTH - apple_size), random.randint(0, HEIGHT - apple_size)


       
    # Initialize snake body
    snake_body = [(x, y)]
    snake_size = 20  # Size of each segment of the snake

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -velocity
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, velocity
                elif event.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -velocity, 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = velocity, 0

        # Update snake position
        x += dx
        y += dy

        # Extend the snake's body by 20 segments when it eats an apple
        if len(snake_body) < (score + 1) * 20:
            snake_body.extend([(x, y)] * 20)

        # Add new head to the snake body
        snake_body.append((x, y))
        if len(snake_body) > score + 1:
            snake_body.pop(0)

        # Check for collision with the apple
        if x < apple_x + apple_size and x + snake_size > apple_x and y < apple_y + apple_size and y + snake_size > apple_y:
            score += 1
            apple_x, apple_y = spawn_apple()

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw the snake's body
        for segment in snake_body:
            pygame.draw.rect(screen, (0, 255, 0), (*segment, snake_size, snake_size))

        # Draw the apple
        pygame.draw.rect(screen, (255, 0, 0), (apple_x, apple_y, apple_size, apple_size))

        # Update the display
        pygame.display.flip()
        clock.tick(FPS)

        # Clear the screen and draw the snake
        screen.fill((0, 0, 0))  # Clear the screen with black
        pygame.draw.rect(screen, (0, 255, 0), (x, y, 20, 20))  # Draw the snake as a green square
         # Check for collision with the apple
        if x < apple_x + apple_size and x + 20 > apple_x and y < apple_y + apple_size and y + 20 > apple_y:
            score += 1
            apple_x, apple_y = spawn_apple()

        # Draw the apple
        pygame.draw.rect(screen, (255, 0, 0), (apple_x, apple_y, apple_size, apple_size))
        pygame.display.flip()  # Update the display
        clock.tick(FPS)  # Control the frame rate


main()
pygame.quit()