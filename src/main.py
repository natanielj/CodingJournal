import psutil

def is_app_running(app_name):
    for process in psutil.process_iter(['name']):
        if process.info['name'] == app_name:
            return True
    return False

if is_app_running("code.exe"):
    print("vscode is currently running.")
else:
    print("vscode is not running.")

# if is_app_running("chrome.exe"):
#     print("Google Chrome is currently running.")
# else:
#     print("Google Chrome is not running.")