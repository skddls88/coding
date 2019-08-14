import pyautogui as m

try:
    while True:
        x, y = m.position()
        
        RGB = m.screenshot().getpixel((x, y))
        print('x : {}, y : {}, RGB = {}'. format(x, y, RGB), end='\r')
        
        
except KeyboardInterrupt:
    print('Ctrl + C를 눌러서 프로그램을 종료합니다.')