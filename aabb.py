import pygame

'''Conditions
'''


class App:
    def __init__(self) -> None:
        self.WIDTH, self.HEIGHT = 600, 600
        self.FPS = 120
        self.CLOCK = pygame.time.Clock()
        self.WINDOW = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.speed = 5

    def run(self):
        static_body = Body(300, 100, 'blue')
        moving_body = Body(200, 300, 'green')
        key = None
        while True:
            pygame.display.set_caption(f"Collison {self.CLOCK.get_fps()}")
            self.WINDOW.fill('black')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            key = pygame.key.get_pressed()
            pos = pygame.mouse.get_pos()
            self.keyboard_interraction(key, static_body)
            self.mouse_interaction(moving_body, pos)

            if (is_coliding(moving_body, static_body)):
                moving_body.color = 'red'
                static_body.color = 'red'
            else:
                moving_body.color = 'green'
                static_body.color = 'red'
            self.check_boundary(static_body)
            static_body.draw(self.WINDOW)
            moving_body.draw(self.WINDOW)
            pygame.display.flip()
            self.CLOCK.tick(self.FPS)

    def keyboard_interraction(self, key, body):
        # if bool:
        #     match key:
        #         case pygame.K_UP:
        #             body.y -= self.speed
        #         case pygame.K_DOWN:
        #             body.y += self.speed
        #         case pygame.K_RIGHT:
        #             body.x += self.speed
        #         case pygame.K_LEFT:
        #             body.x -= self.speed
        key_input = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:
            body.x -= self.speed
        if key[pygame.K_RIGHT]:
            body.x += self.speed
        if key[pygame.K_UP]:
            body.y -= self.speed
        if key[pygame.K_DOWN]:
            body.y += self.speed

    def check_boundary(self, body):
        if body.x > self.WIDTH:
            body.x = 0
        if body.x < 0:
            body.x = self.WIDTH
        if body.y > self.HEIGHT:
            body.y = 0
        if body.y < 0:
            body.y = self.HEIGHT

    def mouse_interaction(self, body, pos):
        x, y = pos[0], pos[1]
        body.x = x
        body.y = y
        ...


def is_coliding(body1, body2):
    condition_1 = body1.x < body2.x+body2.dimention
    condition_2 = body1.x+body1.dimention > body2.x
    condition_3 = body1.y < body2.y+body2.dimention
    condition_4 = body1.dimention+body1.y > body2.y
    if condition_1 and condition_2 and condition_3 and condition_4:
        return True
    ...


class Body:
    def __init__(self, x, y, color) -> None:
        self.x = x
        self.y = y
        self.color = color
        self.dimention = 50
        pass

    def draw(self, surface):
        rectangle = pygame.Rect(self.x, self.y, self.dimention, self.dimention)
        pygame.draw.rect(surface, self.color, rectangle)


if __name__ == "__main__":
    app = App()
    app.run()
