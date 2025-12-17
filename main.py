import os
import re
import zipfile
from io import StringIO
from collections import Counter
from contextlib import redirect_stdout
from typing import Callable, Optional, Iterable, Any


def run_tests(tests_path: Optional[str] = None) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Any:
            return func(*args, **kwargs)

        if tests_path is not None:
            tests_dir = os.path.join(
                os.path.dirname(tests_path),
                os.path.basename(tests_path).split('.')[0]
            )

            if tests_path.lower().endswith('.zip'):
                with zipfile.ZipFile(tests_path, 'r') as zip_ref:
                    zip_ref.extractall(tests_dir)

            test_pairs = sorted(f for f in os.listdir(tests_dir) if f.isdigit())

            for test_num in test_pairs:
                print(f'\n\033[1mRunning test {test_num}...\033[0m')

                with (
                    open(os.path.join(tests_dir, test_num), 'r', encoding='utf-8') as test_ref,
                    open(os.path.join(tests_dir, test_num + '.clue'), 'r', encoding='utf-8') as clue
                ):
                    test_code = test_ref.read()

                    with redirect_stdout(StringIO()) as f:
                        exec(
                            test_code.replace(func.__name__, 'func'),
                            {'func': func}
                        )

                    expected = clue.read().strip()
                    result = f.getvalue().strip()

                    if result == expected:
                        print('\033[34mТЕСТ ПРОЙДЕН\033[0m')
                    else:
                        print('\033[31mТЕСТ ПРОВАЛЕН\033[0m')
                        print(f'Код:\n{test_code}')
                        print(f'\nОжидалось:\n{expected}')
                        print(f'\nПолучено:\n{result}')
                        break

        return wrapper

    return decorator


@run_tests(
    tests_path=r'/Users/lezginchik/Работа/Поколение Python курс для профессионалов (2022) [Тимур Гуев, Артур Харисов] /[SW.BAND] 2. Повторяем основные конструкции языка Python/Часть 1/Задача 1.zip')
def hide_card(card_number: str) -> str:
    # удаляем все пробелы
    card_number = card_number.replace(' ', '')

    # заменяем первые 12 цифр на *
    return '*' * 12 + card_number[12:]
