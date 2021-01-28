#이름으로 메모장 프로그램을 찾은다음, HI 라고 타이핑한다.
import win32gui
import win32con
import win32api

hwnd = win32gui.FindWindow(None, "제목 없음 - Windows 메모장")
edit = win32gui.GetDlgItem(hwnd, 0xF)

win32api.SendMessage(edit, win32con.WM_CHAR, ord('H'), 0)
win32api.Sleep(100)

win32api.SendMessage(edit, win32con.WM_CHAR, ord('i'), 0)
win32api.Sleep(100)