import pygame
from pygame.locals import *
import sys
import random

class Typing():
    def __init__(self):
        pygame.init()
        screen_size = (600, 400)
        self.screen = pygame.display.set_mode(screen_size)
        self.Main = MainGame(self.screen)
        
    def main(self):
        self.Main.main_game()
        
class MainGame():
    def __init__(self, screen):
        self.screen = screen
        self.font_susi = pygame.font.SysFont(None, 70)
        self.font_score = pygame.font.SysFont(None, 30)
        self.font_time = pygame.font.SysFont(None, 50)
        self.score = 0
        self.clock = pygame.time.Clock()
        self.word_list = ['apple', 'banana', 'orange']
        self.word = random.choice(self.word_list)
        
    def main_game(self):
        while True:
            self.screen.fill((0, 0, 0))
            pygame.display.set_caption('Game Mode')
            self.word_check()
            susi_text = self.font_susi.render(self.word, True, (255, 255, 255))
            score_text = self.font_score.render(str(self.score), True, (255, 255, 255))
            time_text = self.font_time.render(str(self.get_time()//1000), True, (255, 255, 255))
            self.screen.blit(score_text, (0, 0))
            self.screen.blit(susi_text, (0, 120))
            self.screen.blit(time_text, (400, 0))
            pygame.display.update()
            self.time_check()
            for event in pygame.event.get():
                self.word_cut(event)
                if event.type == QUIT:
                    pygame.init()
                    sys.exit()

    def word_cut(self, event):
        if event.type == pygame.KEYDOWN:
            if self.word[0] == chr(event.key):
                self.word = self.word[1:]
    
    def word_check(self):
        if len(self.word) < 1:
                self.word = random.choice(self.word_list)
                self.get_score()
                
    def get_score(self):
        self.score += 100
    
    def get_time(self):
        elapsed_time = pygame.time.get_ticks()
        return elapsed_time
    
    def time_check(self):
        elapsed_time = pygame.time.get_ticks()
        if 10000 < elapsed_time:
            pygame.init()
            sys.exit()
    
if __name__ == '__main__':
    Typing = Typing()
    Typing.main()
