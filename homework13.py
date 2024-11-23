import random

import enchant


class CaesarsCipher:
    def __init__(self):
        """Устанавливает атрибуты CaesarsCipher."""
        self.alphabet: str = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                              'abcdefghijklmnopqrstuvwxyz1234567890 !?.')
        self.key: int = -1
        self.random_key: int = random.randint(0, len(self.alphabet))
        self.result_1, self.result_2 = '', ''
        self.dictionary: enchant = enchant.Dict("en_US")

    def decrypt(self, message: str) -> str:
        """Расшифровывает сообщение из шифра Цезаря с методом подбора ключа.

        Args:
            message: Сообщение, которое необходимо расшифровать.

        Returns:
            Возвращает расшифрованное сообщение.

        """
        check_arg: bool = False
        # Переменная для записи результата проверки на орфографию.
        self.key = -1
        # self.key перезадается, чтобы при каждом вызове метода атрибут
        # откатывался в начальное значение.
        while self.key < len(self.alphabet):
            self.key += 1
            for i in range(len(message)):
                ind: int = self.alphabet.find(message[i])
                # ind - Переменная для записи индекса символа
                # зашифрованной строки в алфавите шифра.
                if ind - self.key >= 0:
                    self.result_1 += self.alphabet[ind - self.key]
                else:
                    self.result_1 += self.alphabet[-(self.key - ind)]
            self.result_1 = self.result_1.split(' ')
            # Строка переводится в список для проверки каждого слова
            # на орфографию.
            for el in self.result_1:
                try:
                    check_arg = self.dictionary.check(el)
                    if check_arg is False:
                        break
                except ValueError:
                    break
            if check_arg is True:
                return ' '.join(self.result_1)
            else:
                self.result_1 = ''
        if self.result_1 == '':
            return 'Ошибка. Сообщение невозможно расшифровать.'

    def encrypt(self, message: str) -> str:
        """Шифрует сообщение шифром Цезаря на случайное значение ключа.

        Args:
            message: Сообщение, которое необходимо зашифровать.

        Returns:
            Возвращает зашифрованное сообщение.

        """
        for i in range(len(message)):
            ind = self.alphabet.find(message[i])
            # ind - переменная для записи индекса символа шифруемой строки
            # в алфавите шифра.
            if ind + self.random_key < len(self.alphabet):
                self.result_2 += self.alphabet[ind + self.random_key]
            else:
                dif = ind + self.random_key - len(self.alphabet)
                self.result_2 += self.alphabet[dif]
        return self.result_2
