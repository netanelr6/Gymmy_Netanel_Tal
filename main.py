import time
import datetime
import Settings as s

# ==========================================================
# 1. CRITICAL: Initialize global variables before class imports
# This prevents AttributeErrors in Camera, Poppy, and Audio threads
# ==========================================================
s.req_exercise = ""
s.str_to_say = ""
s.finish_workout = False
s.experiment_started = False
s.ex_list = []
s.hardwere_aff = False
s.inter_aff = False

# ==========================================================
# 2. Import components after Settings initialization
# ==========================================================
import Excel
from Camera import Camera
from Poppy import Poppy
from Audio import Audio
from Training import Training
from Screen import Screen, FullScreenApp
from PIL import Image, ImageTk

def initialize_experiment_settings():
    """
    Setup basic experiment parameters and folder paths
    """
    
    s.camera_num = 0 if s.RUN_MODE.lower() == 'sim' else 1  # Default camera index for 'sim' | 1 for robot
    language = 'Hebrew'
    gender = 'Male'
    s.audio_path = f'audio files/{language}/{gender}/'
    s.picture_path = f'audio files/{language}/{gender}/'
    
    # Participant unique code generation (DD.MM_HH.MM.SS)
    current_time = datetime.datetime.now()
    s.participant_code = current_time.strftime("%d.%m_%H.%M.%S")

    # Original system variables4
    s.exercise_amount = 6
    s.rep = 3 
    s.waved = False
    s.success_exercise = False
    s.calibration = False
    s.training_done = False
    s.poppy_done = False
    s.camera_done = False
    s.robot_count = True
    s.try_again = False
    s.adaptive = False
    s.corrective_feedback = False

if __name__ == '__main__':
    print("--- GYMMY SYSTEM STARTING ---")
    
    # 1. Run settings initialization
    initialize_experiment_settings()
    
    # 2. Launch GUI Screen
    # Will open in fullscreen if RUN_MODE is set to 'ROBOT' in Settings.py
    s.screen = Screen()
    
    # 3. Smart wait loop for researcher selection
    # Keeps the window responsive in Windows environment
    print("Waiting for researcher selection on screen...")
    while not s.experiment_started:
        try:
            s.screen.update_idletasks()
            s.screen.update()
            time.sleep(0.01)
        except Exception as e:
            print(f"GUI Interaction Error: {e}")
            break

    # 4. Post-selection setup
    print(f"Protocol {s.WORKFLOW_MODE} selected. Initializing hardware...")
    
    # Configure exercise list based on study protocol
    s.ex_list = ["hello_waving", "raise_arms", "bend_elbows"]

    # 5. Initialize hardware and logic objects
    Excel.create_workbook()
    s.camera = Camera()
    s.training = Training()
    s.robot = Poppy()
    s.audio = Audio()

    # 6. Start background threads
    s.camera.start()
    s.training.start()
    s.robot.start()
    s.audio.start()
    
    print("ALL SYSTEMS GO. Workout session in progress.")
    
    # 7. Start main GUI loop (Eyes display)
    s.screen.mainloop()
