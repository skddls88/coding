import pyautogui as m
import random
#0,27 65,88 범위 내에 크롬이 있다.

def rand(chrome_button):
    x = random.uniform(chrome_button['top_left']['x'], chrome_button['bottom_right']['x'])
    y = random.uniform(chrome_button['top_left']['y'], chrome_button['bottom_right']['y'])
    #random.uniform(a, b)는 a와 b사이 수 중에 랜덤한 값을 반환한다.

    return x, y
def main():
    chrome_button = {
        'top_left' : {'x': 0, 'y' : 27},
        'bottom_right' : {'x' : 64, 'y' : 89}
    }

    x, y = rand(chrome_button)
    #rand()함수에 chrome의 사각형 좌표를 넣고 이 중에서 x와 y를 반환받는다.
    m.moveTo(x, y, duration = 1)

if __name__ == '__main__':
    main()
