import pygame

WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("First Game!")

COLOR = (255,255,255)
FPS = 60

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        draw_window()

    pygame.quit()

def draw_window():
    WIN.fill(COLOR)
    pygame.display.update()

def draw_grid():
    blockSize = 200
    for i in range(WIDTH):
        for j in range(HEIGHT):
            rect = pygame.RECT(i*blockSize,j*blockSize,blockSize,blockSize)
            pygame.draw.rect(WIN, (0,0,0), rect, 1)

if __name__ == "__main__":
    main()