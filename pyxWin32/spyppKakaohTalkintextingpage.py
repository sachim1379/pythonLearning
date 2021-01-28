import time, win32con, win32api, win32gui ##pypiwin32 모듈 필요
#열려있는 대화창의 대화항목을 선택해서 입력한 메세지를 자동전송
#채팅방지정
kakao_opentalk_name = '재호'

def kakao_sendtext(text):
    win32api.SendMessage(hwndEdit, win32con.WM_SETTEXT, 0, text)
    SendReturn(hwndEdit)

## 엔터
def SendReturn(hwnd):
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    time.sleep(0.01)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

#핸들
hwndMain = win32gui.FindWindow( None, kakao_opentalk_name)
hwndEdit = win32gui.FindWindowEx( hwndMain, None, "RICHEDIT50W", None) ##RichEdit20W는 카톡안 대화텍스트박스의 클래스명
hwndListControl = win32gui.FindWindowEx( hwndMain, None, "EVA_VH_ListControl_Dblclk", None)

##텍스트전송
text = "SETTEXT_test"
kakao_sendtext(text)