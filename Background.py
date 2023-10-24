import ctypes,win32con
from os import listdir
from random import choice

FOLDER = ""

def get_wallpaper():
    ubuf = ctypes.create_unicode_buffer(512)
    ctypes.windll.user32.SystemParametersInfoW(win32con.SPI_GETDESKWALLPAPER,len(ubuf),ubuf,0)
    return ubuf.value

def set_wallpaper(path):
    changed = win32con.SPIF_UPDATEINIFILE | win32con.SPIF_SENDCHANGE
    ctypes.windll.user32.SystemParametersInfoW(win32con.SPI_SETDESKWALLPAPER,0,path,changed)
    
def change_bg():
    try:
        stock = listdir(FOLDER)
        bg = choice(stock)
        print(bg)
    except:
        print("Folder doesn't exist.")
        
    if get_wallpaper() ==f"{FOLDER}/{bg}" and len(stock)>1:
        change_bg()
    else:
        set_wallpaper(f"{FOLDER}/{bg}")

change_bg()
