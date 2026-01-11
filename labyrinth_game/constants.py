


# Константа с описанием комнат
ROOMS = {
    'entrance': {
        'description': 'Вы в темном входе лабиринта. На полу лежит старый факел.', 
        'exits': {'north': 'hall', 'east': 'trap_room', 'south': 'storeroom'},
        'items': ['torch'],
        'puzzle': None
    },
    'hall': {
        'description': 'Большой зал, где стоит пьедестал с запечатанным сундуком.', 
        'exits': {'south': 'entrance', 'west': 'library', 'north': 'treasure_room'}, 
        'items': [],
        'puzzle': ('На пьедестале надпись: "Назовите число, которое идет после девяти".'
                   'Введите ответ цифрой или словом.', '10') 
    },
    'trap_room': {
          'description': ('Комната с хитрой плиточной поломкой. На стене видна надпись:'
            '"Осторожно — ловушка".'), 
          'exits': {'west': 'entrance', 'north': 'storeroom'},
          'items': ['rusty_key'],
          'puzzle': ('Система плит активна. Чтобы пройти, назовите слово "шаг"' 
                     ' три раза подряд (введите "шаг шаг шаг")', 'шаг шаг шаг') 
    },
    'library': {
          'description': 'Пыльная библиотека. На полках старые свитки. Где ключ?', 
          'exits': {'east': 'hall', 'north': 'armory'},
          'items': ['ancient_book'],
          'puzzle': ('В одном свитке загадка: "Что растет, когда его съедают?" '
                     '(ответ одно слово)', 'резонанс') 
    },
        'armory': {
          'description': ('Старая оружейная комната. На стене висит меч,'
            'рядом стоит шкатулка.'), 
          'exits': {'south': 'library'},
          'items': ['sword', 'bronze_box'],
          'puzzle': None
    },
    'treasure_room': {
          'description': 'Комната, на столе стоит сундук. Дверь заперта, нужен ключ.', 
          'exits': {'south': 'hall'},
          'items': ['treasure_chest'],
          'puzzle': ('Дверь защищена кодом. Введите код: 2*5= ? )', '10') 
    },
    # Мои комнаты:
    'storeroom': {
        'description': 'Кладовая забита ящиками, почти ничего нельзя достать', 
        'exits': {'north': 'hall', 'south': 'trap_room', 'east': 'tomb'},
        'items': ['old_armor'],
        'puzzle': None
    },
    'tomb': {
        'description': 'Темный пустой склеп, неосвещенный, холодный, покинутый', 
        'exits': {'west': 'storeroom'},
        'items': ['old_note'],
        'puzzle': None
    }
}


NUMBERS = {
    '0': 'ноль',
    '1': 'один',
    '2': 'два',
    '3': 'три',
    '4': 'четыре',
    '5': 'пять',
    '6': 'шесть',
    '7': 'семь',
    '8': 'восемь',
    '9': 'девять',
    '10': 'десять',
}

# Константа с описанием команд
COMMANDS = {
    'go <direction>': 'перейти в направлении (north/south/east/west)',
    '<direction>': 'перейти в направлении (north/south/east/west)',
    'look': 'осмотреть текущую комнату',
    'take <item>': 'поднять предмет',
    'use <item>': 'использовать предмет из инвентаря',
    'inventory': 'показать инвентарь',
    'solve': 'попытаться решить загадку в комнате',
    'quit/exit': 'выйти из игры',
    'help': 'показать это сообщение'
}

# Константы с параметрами для случайных событий
EVENT_PROBABILITY = 10
EVENT_COUNT = 2
EVENT_INTENSIVITY = 4
TRAP_DMG_PROBABILITY = 9
BEAST_DMG_PROBABILITY = 8
EVENT1_DEATH_DMG = 3
EVENT2_DEATH_DMG = 2
