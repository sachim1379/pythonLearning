#프로세스이름으로 프로그램을 찾아 종료시킨다.
#예시프로그램은 '계산기'

import win32gui
import win32con

hwnd = win32gui.FindWindow(None, "계산기") #핸들이용
win32gui.PostMessage(hwnd, win32con.WM_CLOSE,0,0) #해당 핸들에 종료 메세지전송 