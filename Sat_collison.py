import pygame

class App:
    def __init__(self) -> None:          
        self.WIDTH,self.HEIGHT=800,600
        self.FPS=30
        self.CLOCK=pygame.time.Clock()
        self.WINDOW=pygame.display.set_mode((self.WIDTH,self.HEIGHT))
    def run(self):
        while True:  
            pygame.display.set_caption(f"SAT collison {self.CLOCK.get_fps()}")
            self.WINDOW.fill((0,0,0))
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit()

            pygame.display.flip()
            self.CLOCK.tick(self.FPS)	
    ...


if __name__=="__main__":
    app=App()
    app.run()