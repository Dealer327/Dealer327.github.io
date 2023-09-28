from calendar import monthrange
from datetime import datetime

Lexicon_ru: dict[str, str] = {'/start': '<b>Привет, друг!</b>\n\nЭто бот,'
                                        'в котором ты сможешь узнать о предстоящих мероприятиях в твоем городе или'
                                        ' создать свои! Ты сможешь находить друзей и единомышленников в одном месте!',
                              'forward': '>>',
                              'backward': '<<',
                              'calendar': 'календарь событий',
                              'new_event': 'создать свое событие',
                              }
now_year = datetime.today().year
now_month = datetime.today().month
days = monthrange(now_year, now_month)[1]

Lexicon_days: list[str] = [str(i) for i in range(1, days + 1)]


Lexicon_month: dict[str, str] = {'1': 'Январь', '2': 'Февраль',
                                 '3': 'Март', '4': 'Апрель',
                                 '5': 'Май', '6': 'Июнь',
                                 '7': 'Июль', '8': 'Август',
                                 '9': 'Сентябрь', '10': ' Октябрь',
                                 '11': 'Ноябрь', '12': 'Декабрь',
                                 'forward_c': '>>',
                                 'backward_c': '<<',
                                 }
LEXICON_COMMANDS: dict[str, str] = {
    'help': 'Справочник по работе бота'}
