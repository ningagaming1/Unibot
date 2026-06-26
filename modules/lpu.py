import webbrowser

def handle(user_input, user_data):

    if "ums" in user_input:
        webbrowser.open("https://ums.lpu.in/lpuums/")

    elif "touch" in user_input:
        webbrowser.open("YOUR_LPU_TOUCH_URL")

    elif "dashboard" in user_input:
        webbrowser.open("https://admission.lpu.in")
    
    elif "class" in user_input:
        webbrowser.open("https://myclass.lpu.in/")

    else:
        print("Unknown LPU service")