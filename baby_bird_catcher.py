import pygame,sys,random

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.init()

text_font = pygame.font.SysFont("Arial", 100)

def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))

class Basket(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Basket, self).__init__()
        basket_img = pygame.image.load("Basket2.jpg").convert_alpha()
        self.image = pygame.transform.scale(basket_img, (160, 80))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 15
        self.direction = 0

    def move(self):
        self.rect.x += self.direction * self.speed
        self.rect.x = max(0, min(self.rect.x, 1200 - self.rect.width))


    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.direction = -1
            elif event.key == pygame.K_RIGHT:
                self.direction = 1
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                self.direction = 0

class BabyBird(pygame.sprite.Sprite):
    def __init__(self, x, y, point_value):
        super(BabyBird, self).__init__()
        egg_img = pygame.image.load("Egg.png").convert_alpha()
        self.image = pygame.transform.scale(egg_img, (40, 50))
        self.rect = self.image.get_rect(center=(x, y))
        self.point_value = 5 #point_value


    def move(self):
        self.rect.y += 5


def main():
    pygame.init()


    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Baby Bird Catcher")


    clock = pygame.time.Clock()


    basket = Basket(screen_width // 2, screen_height - 50)
    all_sprites = pygame.sprite.Group()
    baby_birds = pygame.sprite.Group()


    all_sprites.add(basket)


    score = 0
    score_font = pygame.font.Font(None, 36)


    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            basket.handle_event(event)

        screen.fill((255, 255, 255))

        basket.move()


        if random.randint(0, 100) < 5:
            baby_bird = BabyBird(random.randint(30, screen_width - 30), 0, random.randint(1, 10))
            all_sprites.add(baby_bird)
            baby_birds.add(baby_bird)


        for baby_bird in baby_birds:
            baby_bird.move()
            if baby_bird.rect.colliderect(basket.rect):
                score += baby_bird.point_value
                baby_bird.kill()
            elif baby_bird.rect.bottom > screen_height:
                score -= 5
                baby_bird.kill()


        all_sprites.draw(screen)


        score_text = score_font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        if score>=100:
            screen.fill((173,217,137))
            draw_text("You Won!", text_font, (0,0,0), 250, 200)
            score+=1000
        elif score<0:
            screen.fill((0,0,0))
            draw_text("You Lost", text_font, (200,0,0), 250, 200)
            score-=1000
            
        else:
            pass
        
        

        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()


if __name__ == "__main__":
    main()
