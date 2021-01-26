#프로세스이름으로 프로그램을 찾아 종료시킨다.
#프로그램은 4K stogram
import sys
import win32gui
import win32con
hwnd = win32gui.FindWindow(None, "4K Stogram – 프로페셔널 라이선스") #핸들찾기->spyxx로찾음
win32gui.PostMessage(hwnd, win32con.WM_CLOSE,0,0) #해당 핸들에 종료 메세지전송 

sys.exit()