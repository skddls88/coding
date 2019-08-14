import pyautogui as m
import random
import time

def rand(chrome_button):
    x = random.uniform(chrome_button['top_left']['x'], chrome_button['bottom_right']['x'])
    y = random.uniform(chrome_button['top_left']['y'], chrome_button['bottom_right']['y'])
    # random.uniform(a, b)는 a와 b사이 수 중에 랜덤한 값을 반환한다.

    return x, y

def click():
    time.sleep(1)
    # 이동 후 1초 쉬고...
    m.click()
    # 파라미터가 없으면 현재 마우스좌표를 클릭
    print('chrome을 클릭하였습니다.')

    time.sleep(4)
    # chrome browser가 뜨는동안 대기
    m.typewrite('naver.com', interval=0.25)
    # 키보드로 입력, interval 옵션은 적지 않아도 무방
    # interval = 한 글자 입력 후 대기시간
    # 오토같지 않도록...
    print('주소에 "naver.com"을 입력하였습니다.')

    time.sleep(1)
    # 주소 입력 후 대기
    m.press('enter')
    # press는 특정 키를 입력할 때
    print('enter를 눌렀습니다.')

    return

def login():
    time.sleep(2)

    try:
        button = m.locateOnScreen('btn.png')
        # 버튼의 좌표는 왼쪽 위(x,y), 오른쪽 아래 (x,y)의 사각형 형태
        # 아래 라인에서 이 좌표의 중심 좌표를 구하고 클릭!

        center = m.center(button)
        # button은 사각형 좌표고 사각형의 중심좌표를 center변수에 저장
        print('button_center : ', center)

    except:
        print('해당이미지가 존재하지 않아 종료합니다.')
        exit(0)

    m.click(center) # 중심좌표 입력
    print('Login 버튼을 클릭하였습니다.')

def main():
    chrome_button ={
        'top_left' : {'x': 0, 'y' : 27},
        'bottom_right' : {'x' : 65, 'y' : 88}
    }

    x, y = rand(chrome_button)
    #rnad()함수에 chrome의 사각형 좌표를 넣고 이 중에서 x와 y를 반환받는다.
    m.moveTo(x, y, duration = 1)
    click()
    login()

if __name__ == '__main__':
    main()

