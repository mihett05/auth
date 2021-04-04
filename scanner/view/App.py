import pygame
import qrcode
from threading import Thread

from ws.ws import Client


class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.token = "No token"
        self.img = None
        self.update_image()
        self.ws = Client(self.update_token)

    def update_image(self):
        qr = qrcode.QRCode(version=1)
        qr.add_data(self.token)
        qr.make()
        img = qr.make_image(back_color="transparent")
        self.img = pygame.image.fromstring(img.tobytes(), img.size, "RGBA")

    def update_token(self, token: str):
        self.token = token
        self.update_image()

    def draw(self):
        self.screen.fill((255, 255, 255))
        rect = self.img.get_rect()
        size = self.screen.get_size()
        self.screen.blit(self.img, (
            int(size[0] / 2 - rect.size[0] / 2),
            int(size[1] / 2 - rect.size[1] / 2),
            rect.size[0],
            rect.size[1]
        ))
        pygame.display.flip()

    def run(self):
        run = True
        Thread(target=self.ws.run_sync, args=()).start()
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.draw()
