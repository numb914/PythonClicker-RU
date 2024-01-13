import mouse
import time
import keyboard
key = input('Какую клавишу использовать для активации временного кликера?').lstrip()
key1 = input('Какую клавишу использовать для АКТИВАЦИИ безостановочного кликера?').lstrip()
key2 = input('Какую клавишу использовать для ОСТАНОВКИ безостановочного кликера?').capitalize().lstrip()
delay = input('Введите задержку в секундах для безостановочного кликера').lstrip()
print('Скрипт активирован')
if ',' in delay:
    delay = float(delay.replace(',', '.'))
while True:
    while keyboard.is_pressed(key):
        mouse.click('left')
        time.sleep(0.01)
    if keyboard.is_pressed(key1):
        while True:
            mouse.click('left')
            time.sleep(delay - 0.01)
            if keyboard.is_pressed(key2):
                break
            if keyboard.is_pressed(key1):
                continue
            time.sleep(0.01)
    time.sleep(0.01)