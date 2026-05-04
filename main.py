import time
import datetime
import Settings as s
import os
import sys

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

# Fallback configuration: assign default project folder if undefined in Settings.py
if not hasattr(s, 'project_folder'):
    s.project_folder = "OPS_folder_not_exsist"
if not hasattr(s, 'save_outputs'):
    s.save_outputs = True
    
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
    s.rep = 8 #8
    s.waved = False
    s.success_exercise = False
    s.calibration = False
    s.training_done = False
    s.poppy_done = False
    s.camera_done = False
    s.robot_count = False
    s.try_again = False
    s.adaptive =  False # True #
    s.corrective_feedback = False

if __name__ == '__main__':
    print("--- GYMMY SYSTEM STARTING ---")
    
    # 1. Run settings initialization
    initialize_experiment_settings()

    # ====================================================================================================
    #----Directory Management & Logging Configuration---------------------------------------------
    log_file = None
    if s.save_outputs:
        # Construct output directory only if saving is enabled
        s.output_path = os.path.join("DATS", s.project_folder, s.participant_code)
        os.makedirs(s.output_path, exist_ok=True)

        # Initialize logging
        log_file_path = os.path.join(s.output_path, "code_output.txt")
        log_file = open(log_file_path, "w", encoding="utf-8")

        class Logger(object):
            def __init__(self, terminal, logfile):
                self.terminal = terminal
                self.logfile = logfile

            def write(self, message):
                self.terminal.write(message)
                self.logfile.write(message)
                self.logfile.flush()

            def flush(self):
                pass

        sys.stdout = Logger(sys.stdout, log_file)
        sys.stderr = Logger(sys.stderr, log_file)
        print(f"--- Session Initialized. Saving to: {s.output_path} ---")
    else:
        print("--- Debug Mode: Outputs and Logging are DISABLED ---")
    #=======================================================================================================
    
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

    try:
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

    except Exception as e:
        print(f"!!! CRITICAL RUNTIME ERROR: {e}")
        
    finally:
        # Finalize and close resources only if they were initialized
        if s.save_outputs:
            Excel.close_workbook()
            if log_file:
                log_file.close()
            print("--- Data securely saved. ---")
        print("--- System shutdown complete. ---")
    # ==========================================================

