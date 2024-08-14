import pygame

'''Conditions
'''


class App:
    def __init__(self) -> None:          
        self.WIDTH,self.HEIGHT=600,600
        self.FPS=120
        self.CLOCK=pygame.time.Clock()
        self.WINDOW=pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        self.speed=100
    def run(self):
        static_body=Body(300,100)
        while True:  
            pygame.display.set_caption(f"Collison {self.CLOCK.get_fps()}")
            self.WINDOW.fill('white')
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit()
                if event.type==pygame.KEYDOWN:
                    key=event.key
                    self.keyboard_interraction(key,static_body)
            static_body.draw(self.WINDOW)
            pygame.display.flip()
            self.CLOCK.tick(self.FPS)	
    def keyboard_interraction(self,key,body):
        print(body.x,body.y)
        match key:
            case pygame.K_UP:
                body.y-=self.speed
            case pygame.K_DOWN:
                body.y+=self.speed
            case pygame.K_RIGHT:
                body.x+=self.speed
            case pygame.K_LEFT:
                body.x-=self.speed
        if body.x>self.WIDTH:
            body.x=0
        if body.x<0:
            body.x=self.WIDTH
        if body.y>self.HEIGHT:
            body.y=0
        if body.y<0:
            body.y=self.HEIGHT



class Body:
    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y
        pass
    def draw(self,surface):
        rectangle=pygame.Rect(self.x,self.y,100,100)
        pygame.draw.rect(surface,'green',rectangle)



if __name__=="__main__":
    app=App()
    app.run()