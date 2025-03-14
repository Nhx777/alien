import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
class AlienInvasion:#管理游戏资源和行为的类
    def __init__(self):
        pygame.init()
        self.settings=Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height)
        )
        self.ship=Ship(self)
        self.bullets=pygame.sprite.Group()
    def run_game(self):
        while True:#开始游戏的主循环
            self._check_events()
            self.ship.update()
            self._update_screen()
            self._update_bullets()

    def _check_events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:#按x退出游戏
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type==pygame.KEYUP:
                self._check_keyup_events(event)
    def _check_keydown_events(self,event):
        print("keydownevent")
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    def _fire_bullet(self):
        if len(self.bullets)<self.settings.bullets_allowed:
            new_bullet=Bullet(self)
            self.bullets.add(new_bullet)
    def _update_screen(self):
            self.screen.fill(self.settings.bg_color)#每次循环时重新绘制屏幕
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            pygame.display.flip()
    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
if __name__ == '__main__':
    ai=AlienInvasion()
    ai.run_game()

