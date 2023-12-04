# Генерирует сообщение после прохождения теста с подходящими спортами.
from .result_sport import test_na_sport


def generate_result_test(answers):
    sports = test_na_sport(answers[0], answers[1], answers[2:-1], answers[-1])
    return f'''
🏁Тест закончен! Мы предлагаем тебе такие виды спорта:
1⃣{sports[0]}
2⃣{sports[1]}
3⃣{sports[2]}
✅Найти информацию про секции по этим видам спорта ты можешь в разделе "Секции"
'''
