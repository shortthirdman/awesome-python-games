import pygame
import random

pygame.init()

WIDTH, HEIGHT = 640, 480
WHITE = (255, 255, 255)
BLACK = (10, 10, 20)
PADDLE_SPEED = 6
BALL_SPEED = 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Pong")
clock = pygame.time.Clock()
font = pygame.font.SysFont("consolas", 32)

paddle_width, paddle_height = 12, 90

player = pygame.Rect(30, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
opponent = pygame.Rect(WIDTH - 42, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
ball = pygame.Rect(WIDTH // 2 - 8, HEIGHT // 2 - 8, 16, 16)

ball_dx = BALL_SPEED * random.choice([-1, 1])
ball_dy = BALL_SPEED * random.choice([-1, 1])

player_score = 0
opponent_score = 0
running = True

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and player.top > 0:
        player.y -= PADDLE_SPEED

    if keys[pygame.K_DOWN] and player.bottom < HEIGHT:
        player.y += PADDLE_SPEED

    if opponent.centery < ball.centery and opponent.bottom < HEIGHT:
        opponent.y += PADDLE_SPEED - 1

    if opponent.centery > ball.centery and opponent.top > 0:
        opponent.y -= PADDLE_SPEED - 1

    ball.x += ball_dx
    ball.y += ball_dy

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy *= -1

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_dx *= -1

    if ball.left <= 0:
        opponent_score += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_dx = BALL_SPEED * random.choice([-1, 1])

    if ball.right >= WIDTH:
        player_score += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_dx = BALL_SPEED * random.choice([-1, 1])

    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player)
    pygame.draw.rect(screen, WHITE, opponent)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
    score_text = font.render(f"{player_score}   {opponent_score}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))
    pygame.display.flip()
pygame.quit()