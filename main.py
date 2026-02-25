import time
import Settings as s
import Excel
# Note: We keep the imports here, but we will initialize them carefully
from Camera import Camera
from Poppy import Poppy
from Audio import Audio
from Training import Training
from Screen import Screen, FullScreenApp
from PIL import Image, ImageTk
import pickle
import datetime

if __name__ == '__main__':
    # --- 1. המשתנים המקוריים שלך (חייבים לרוץ ראשונים) ---
    s.camera_num = 0
    language = 'Hebrew'
    gender = 'Male'
    s.audio_path = 'audio files/' + language + '/' + gender + '/'
    s.picture_path = 'audio files/' + language + '/' + gender + '/'
    
    current_time = datetime.datetime.now()
    s.participant_code = str(current_time.day) + "." + str(current_time.month) + " " + \
                         str(current_time.hour) + "." + str(current_time.minute) + "." + \
                         str(current_time.second)

    # אתחול כל המשתנים הגלובאליים בדיוק כמו בגרסה המקורית
    s.exercise_amount = 6
    s.rep = 3 
    s.req_exercise = ""
    s.finish_workout = False
    s.waved = False
    s.success_exercise = False
    s.calibration = False
    s.training_done = False
    s.poppy_done = False
    s.camera_done = False
    s.robot_count = True
    s.try_again = False
    s.inter_aff = False
    s.hardwere_aff = False
    s.Team_Number = 0
    s.ex_list = []
    s.adaptive = False
    s.corrective_feedback = False
    s.one_hand = False
    s.experiment_started = False # המשתנה החדש שלנו

    # --- 2. הפעלת המסך לבחירת המצב (A, B, C) ---
    s.screen = Screen()
    # כאן המערכת עוצרת ומחכה שתבחר מצב ותלחץ START
    print("Waiting for protocol selection on screen...")
    while not s.experiment_started:
        s.screen.update_idletasks()
        s.screen.update()
        time.sleep(0.01)

    # --- 3. עדכון רשימת התרגילים לפי מה שנבחר (בדיוק כמו שרצית) ---
    # כאן אתה יכול להוסיף לוגיקה ספציפית למצבים A/B/C
    s.ex_list = ["hello_waving", "raise_arms", "bend_elbows"] 

    # --- 4. יצירת הרכיבים (בדיוק בסדר המקורי) ---
    Excel.create_workbook()
    s.camera = Camera()
    s.training = Training()
    s.robot = Poppy()
    # s.audio = Audio() # אם יש לך מחלקת Audio, בצע לה initialization כאן

    # --- 5. הפעלת ה-Threads (בדיוק בסדר המקורי) ---
    s.camera.start()
    s.training.start()
    s.robot.start()

    # הגדרות תצוגה סופיות
    image1 = Image.open('Pictures//icon.jpg')
    s.screen.tk.call('wm', 'iconphoto', s.screen._w, ImageTk.PhotoImage(image1))
    
    # הפעלת הלופ של העיניים
    print("SYSTEM ACTIVE. Running experiment...")
    s.screen.mainloop()