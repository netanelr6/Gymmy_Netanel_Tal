show_reboot_button = True

req_exercise = ""
str_to_say = ""
finish_workout = False
experiment_started = False

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


    one_hand = False
    RUN_MODE = 'SIM'          # 'SIM' OR 'ROBOT'
    experiment_started = False
    WORKFLOW_MODE = 1        # 1=Normal, 2=Hardware, 3=Interactio
    show_reboot_button = True 
