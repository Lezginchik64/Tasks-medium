from captcha.image import ImageCaptcha
from PIL import Image
import random
import string


def generate_captcha_text(length=10):
    return ''.join(
        random.choices(string.ascii_letters + string.digits, k=length)
    )

def generate_captcha_image(captcha_text, image_width=300):
    image = ImageCaptcha(image_width)
    image_file = f"{captcha_text}.png"
    image.write(captcha_text, image_file)
    return image_file

captcha_text = generate_captcha_text()
image_file = generate_captcha_image(captcha_text)
print("Generated CAPTCHA")
Image.open(image_file).show()

attempts = 3
for attempt in range(attempts):
    user_input = input(f"\nПопытка {attempt + 1}/{attempts}: Введите текст: ")

    if user_input.lower() == captcha_text.lower():
        print(f"✅ Верно! Код: {captcha_text.lower()}")
        break
    else:
        print(f"❌ Неверно. Осталось попыток: {attempts - attempt - 1}")
else:
    print(f"💀 Все попытки исчерпаны. Доступ заблокирован.")

