import os
import shutil
import time 
import threading

current_dir = os.getcwd()
inbox_path = os.path.join(current_dir, "data", "files_inbox")

def handle(user_input,user_data):
    pass

def scan():
    list_of_files = os.listdir(inbox_path)
    if len(list_of_files)==0:
        #print("None")
        pass
    else:
        for file_name in list_of_files:
            #print(file) 
            parts = file_name.split(".")
            #print(parts)
            if parts[-1] == "pdf":
                #print(dir(os))
                #print(dir(shutil))
                os.makedirs(os.path.join(current_dir,"data","files_sorted","pdf"),exist_ok=True)
                shutil.copy(os.path.join(inbox_path,file_name),os.path.join(current_dir,"data","files_sorted","pdf"))
                #print("done")
            elif any(parts[-1] == extention for extention in ["txt","rft","md","docx","odt","doc"]):
                #print(dir(os))
                #print(dir(shutil))
                os.makedirs(os.path.join(current_dir,"data","files_sorted","documents"),exist_ok=True)
                shutil.copy(os.path.join(inbox_path,file_name),os.path.join(current_dir,"data","files_sorted","documents"))
                #print("done")
            elif any(parts[-1] == extention for extention in ["jpg","jpeg","png","svg","webp","bmp","tiff"]) :
                #print(dir(os))
                #print(dir(shutil))
                os.makedirs(os.path.join(current_dir,"data","files_sorted","images"),exist_ok=True)
                shutil.copy(os.path.join(inbox_path,file_name),os.path.join(current_dir,"data","files_sorted","images"))
                #print("done")
            elif any(parts[-1] == extention for extention in ["ppt","pptx","key"]) :
                #print(dir(os))
                #print(dir(shutil))
                os.makedirs(os.path.join(current_dir,"data","files_sorted","documents"),exist_ok=True)
                os.makedirs(os.path.join(current_dir,"data","files_sorted","documents","presentations"),exist_ok=True)
                shutil.copy(os.path.join(inbox_path,file_name),os.path.join(current_dir,"data","files_sorted","documents","presentations"))
                #print("done")
            else:
                os.makedirs(os.path.join(current_dir,"data","files_sorted","unidenified"),exist_ok=True)
                shutil.copy(os.path.join(inbox_path,file_name),os.path.join(current_dir,"data","files_sorted","unidenified"))

def run_scanner_forever():
    while True:
        scan()
        time.sleep(1)


scanner_thread = threading.Thread(target=run_scanner_forever, daemon=True)
scanner_thread.start()