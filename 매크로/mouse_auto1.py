import pyautogui as m
import random

chrome_button = {
    'top_left' : {'x': 0, 'y' : 27},
    'bottom_right' : {'x' : 64, 'y' : 89}
}

#random.uniform(src, dst) = src < (float)random_value < dst
x = random.uniform(chrome_button['top_left']['x'], chrome_button['bottom_right']['x'])
y = random.uniform(chrome_button['top_left']['y'], chrome_button['bottom_right']['y'])

m.moveTo(x, y, duration = 2) # ~동안에 = 2초간 x와 y의 좌표로 이동