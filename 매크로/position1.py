import pyautogui as m

try:
    while True:
        x, y = m.position()
        print('x : {0}, y : {1}'. format(x, y), end='\r')
        #position = 'x : {}, y : {}'.format(x,y)
        #print(position, end='')
        #print('\b'* len(position), end='')
        
except:
#keyboardInterrupt:
    print('Ctrl + C를 눌러서 프로그램을 종료합니다.')