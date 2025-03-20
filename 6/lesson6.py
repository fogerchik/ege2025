# Работа с модулями/пакетами/библиотеками

# Импорт всех функций из модуля
import random
num = random.randint(1, 10)

# Импорт всех функций из модуля через псевдоним
import random as rnd
num2 = rnd.randint(1, 10)

# Импорт одной функции из модуля. К модулю по имени обращаться не надо
from random import randint
num3 = randint(1, 10)

# Импорт всех функций из модуля. К модулю по имени обращаться не надо
from random import *
num4 = randint(1, 10)
