show_reboot_button = True

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

