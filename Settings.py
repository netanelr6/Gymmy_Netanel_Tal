import os

project_folder = "netanel&tal_2026A_" # fulder name in dats
output_path = ""    # bild in main
save_outputs = True  # Set to False to disable folder creation, Excel saving, and logging


# adaptation_model_name = "default_model" 

show_reboot_button = True
reboot_flag = False
s.exercise_completed = False

req_exercise = ""
str_to_say = ""
finish_workout = False
experiment_started = False

one_hand = False
experiment_started = False
WORKFLOW_MODE = 1        # 1=Normal, 2=Hardware, 3=Interactio

performance_class = {}

# RUN_MODE = 'SIM'          # 'SIM' OR 'ROBOT'
RUN_MODE = os.getenv('GYMMY_MODE', 'SIM')
"""
    GYMMY RUN_MODE CONFIGURATION:
    -----------------------------
    This variable determines if the system runs in Simulation ('SIM') or on the Physical Robot ('ROBOT').
    To avoid manual code changes when moving between PC and Robot, we use an Environment Variable.
    
    HOW TO CONFIGURE ON A NEW ROBOT:
    1. Open 'Edit the system environment variables' in Windows.
    2. Click 'Environment Variables'.
    3. Under 'User variables', click 'New'.
    4. Variable name: GYMMY_MODE
    5. Variable value: ROBOT
    6. Restart your IDE (PyCharm) or Terminal to apply changes.
    
    If NO environment variable is found, the system defaults to 'SIM'.
"""
    








def __init__():

    # classes pointers
    global training
    global camera
    global robot
    global screen

    #added globals
    global inter_aff
    global hardwere_aff
    global Team_Number

    # reboot button
    global show_reboot_button
    global reboot_flag
    reboot_flag = False


    global participant_code
    global excel_workbook
    global ex_list

    # training variables
    global exercise_amount
    global rep
    global req_exercise
    global finish_workout
    global waved
    global success_exercise
    global calibration
    global poppy_done
    global camera_done
    global robot_count
    global try_again # Adaptive scenario - successful performance
    global robot_rep # number of repetition of the robot

    # audio variables
    global audio_path

    # screen variables
    global picture_path

    global camera_num

    # adaptation
    global adaptation_model
    global adaptive
    global performance_class
    global corrective_feedback
    global one_hand


    # --- New Experiment Control Variables (Added below) ---
    global RUN_MODE
    global experiment_started
    global WORKFLOW_MODE
    global str_to_say



