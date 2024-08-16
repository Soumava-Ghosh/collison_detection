import pygame

class App:
    def __init__(self) -> None:          
        self.WIDTH,self.HEIGHT=800,600
        self.FPS=120
        self.CLOCK=pygame.time.Clock()
        self.WINDOW=pygame.display.set_mode((self.WIDTH,self.HEIGHT))
    def run(self):
        fix_circle=Circle(50,(self.WIDTH/2,self.HEIGHT/2),(200, 100, 23))
        moving_circle=Circle(20,(self.WIDTH/2,self.HEIGHT/2),(163, 254, 35))
        pygame.mouse.set_visible(0)
        while True:  
            pygame.display.set_caption(f"Circle Collison {self.CLOCK.get_fps()}")
            self.WINDOW.fill((0,0,0))
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit()
            pos=pygame.mouse.get_pos()
            moving_circle.centre=pos
            if self.check_collison(moving_circle,fix_circle):
                moving_circle.color='red'
            else:
                moving_circle.color=(163, 254, 35)
            fix_circle.draw(self.WINDOW)
            moving_circle.draw(self.WINDOW)
            pygame.display.flip()
            self.CLOCK.tick(self.FPS)	
    ...
    def check_collison(self,body1,body2):
        x1,y1=body1.centre
        x2,y2=body2.centre
        dist=(x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)
        dist=float(dist**0.5)
        return body1.radius+body2.radius>dist
class Circle:
    def __init__(self,r,pos,colour) -> None:
        self.radius=r
        self.centre=pos
        self.color=colour
        pass
    def draw(self,surface):
        pygame.draw.circle(surface,self.color,self.centre,self.radius)

if __name__=="__main__":
    app=App()
    app.run()