from configparser import ConfigParser
from color import colors
from datetime import date, datetime
from dateFormat import get_date_format, month_formats, year_formats, day_formats, delimiters


class GameConfig(object):

    """Docstring for GameConfig. """

    def __init__(self):
        self.cfg = ConfigParser()
        self.cfg.read('user_cfg.ini')

        self.background_color = colors[self.cfg['DEFAULT']['background_color']]
        self.font_color = colors[self.cfg['DEFAULT']['font_color']]
        self.min_date = datetime.strptime(self.cfg['DEFAULT']['min_date'], '%Y%m%d').date()
        self.max_date = datetime.strptime(self.cfg['DEFAULT']['max_date'], '%Y%m%d').date()
        self.hud = self.cfg['DEFAULT'].getboolean('hud')
        self.timer = self.cfg['DEFAULT'].getboolean('timer')
        self.num_questions = self.cfg['DEFAULT'].getint('num_questions')

        self.month_format = month_formats[self.cfg['DATE FORMAT']['month_format']]
        self.day_format = day_formats[self.cfg['DATE FORMAT']['day_format']]
        self.year_format = year_formats[self.cfg['DATE FORMAT']['year_format']]
        self.delimiter = delimiters[self.cfg['DATE FORMAT']['delimiter']]
        self.date_format = get_date_format(month_format=self.month_format,
                                           day_format=self.day_format,
                                           year_format=self.year_format,
                                           delimiter=self.delimiter)


        self.voice = self.cfg['VOICE'].getboolean('voice')
        self.language = self.cfg['VOICE']['language']

        self.words_per_minute = self.cfg['VOICE'].getint('words_per_minute')
        self.volume = self.cfg['VOICE'].getint('volume')

        self.voice_month_format = month_formats[self.cfg['VOICE']['month_format']]
        self.voice_day_format = day_formats[self.cfg['VOICE']['day_format']]
        self.voice_year_format = year_formats[self.cfg['VOICE']['year_format']]
        if self.cfg['VOICE']['delimiter'] == 'preposition':
            self.voice_delimiter = delimiters[self.cfg['VOICE']['delimiter']][self.language]
        else:
            self.voice_delimiter = delimiters[self.cfg['VOICE']['delimiter']]
        self.voice_date_format = get_date_format(month_format=self.voice_month_format,
                                           day_format=self.voice_day_format,
                                           year_format=self.voice_year_format,
                                           delimiter=self.voice_delimiter)

