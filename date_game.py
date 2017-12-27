import pygame
from datetime import date, timedelta, datetime
from time import sleep
from color import colors
from dateFormat import date_formats
from utils import random_date
from configuration import GameConfig
import pyttsx3
import locale

WIDTH = 640
HEIGHT = 480

class DateGame(object):

    def __init__(self):
        pygame.display.init()
        pygame.font.init()
        pygame.display.set_caption("Guess the day game")
        self.end = False
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.font = pygame.font.SysFont("opensans", 72)

        self.answer = None
        self.hits = 0
        self.fails = 0
        self.questions = 0

        self.config = GameConfig()

        self.engine = pyttsx3.init()
        self.engine.setProperty('voice', self.config.language)
        self.engine.setProperty('rate',self.config.words_per_minute)
        self.engine.setProperty('volume',self.config.volume)

        if self.config.language == 'es':
            locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

    def start(self):
        self.main_menu()

    def update_menu(self, title, menu, option_selected):
        font_title = pygame.font.SysFont("opensans", 65)
        title_text = font_title.render(title, True, self.config.font_color)
        title_height = (HEIGHT / 7)

        self.screen.fill(self.config.background_color)
        self.screen.blit(title_text,
            ((WIDTH / 2) - title_text.get_width() // 2, title_height  - title_text.get_height() // 2))

        options_height = (1-1/7)*HEIGHT
        num_options = len(menu)
        font_option = pygame.font.SysFont("opensans", 48)
        for i, option in enumerate(menu):
            option_name = option['name']
            if option_selected == i:
                option_name = option_name + '*'
            option_text = font_option.render(option_name, True, self.config.font_color)
            self.screen.blit(option_text,
                ((WIDTH / 5) , title_height+i*((options_height / num_options))+option_text.get_height()))
        pygame.display.flip()


    def main_menu(self):
        title = 'Main menu'
        menu = [{'name': 'Play', 'func': self.run},
                {'name': 'Configuration', 'func': self.config_menu}]

        self.menu(title, menu)

    def menu(self, title, menu):
        option = 0
        end = False
        while not end:
            self.update_menu(title, menu, option)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    end = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    menu[option]['func']()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    option = (option + 1) % len(menu)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    option = (option - 1) % len(menu)

    def toggle_voice(self):
        self.config.voice = not self.config.voice

    def config_menu(self):
        title = 'Configuration'
        menu = [{'name':'Voice', 'func': self.toggle_voice}]
        self.menu(title, menu)

    def update_screen(self):
        hud_font = pygame.font.SysFont("opensans", 32)
        self.date_text = self.font.render(self.date.strftime(self.config.date_format), True, self.config.font_color)

        self.screen.fill(self.config.background_color)
        self.screen.blit(self.date_text,
            ((WIDTH / 2) - self.date_text.get_width() // 2, (HEIGHT / 2)  - self.date_text.get_height() // 2))
        hits_text = hud_font.render('Hits: {}'.format(self.hits), True, self.config.font_color)
        fails_text = hud_font.render('Fails: {}'.format(self.fails), True, self.config.font_color)

        if self.config.hud:
            self.screen.blit(hits_text, (0, 0))
            self.screen.blit(fails_text, (WIDTH-fails_text.get_width(), 0))
        pygame.display.flip()

    def run(self):
        self.date = random_date(self.config.min_date, self.config.max_date)
        self.weekday = self.date.weekday()
        self.end_session = False
        self.question = 0
        self.hits = 0
        self.fails = 0
        self.update_screen()

        if self.config.voice:
            self.engine.say(self.date.strftime(self.config.voice_date_format))
            self.engine.runAndWait()
        while self.question < self.config.num_questions and not self.end_session:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.end_session = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.end_session = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
                    self.answer = 6 # Sunday python
                if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                    self.answer = 0 # Monday python
                if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                    self.answer = 1 # Tuesday python
                if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                    self.answer = 2 # Wednesday python
                if event.type == pygame.KEYDOWN and event.key == pygame.K_4:
                    self.answer = 3 # Thursday python
                if event.type == pygame.KEYDOWN and event.key == pygame.K_5:
                    self.answer = 4 # Friday python
                if event.type == pygame.KEYDOWN and event.key == pygame.K_6:
                    self.answer = 5 # Saturday python

            if self.answer is not None:
                self.question += 1
                if self.answer == self.weekday:
                    self.hits += 1
                else:
                    self.fails += 1
                self.answer = None
                self.date = random_date(self.config.min_date, self.config.max_date)
                self.weekday = self.date.weekday()

                self.update_screen()
                if self.config.voice:
                    self.engine.say(self.date.strftime(self.config.voice_date_format))
                    self.engine.runAndWait()


if __name__ == "__main__":
    game = DateGame()
    game.start()

