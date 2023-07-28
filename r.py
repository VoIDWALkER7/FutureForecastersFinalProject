import tkinter as tk
from tkinter import messagebox
import threading
import cv2
import os
import time
import uuid
import speech_recognition as sr

# Hand Tracking Function
def hand():
    import cv2
    import os
    import time
    import uuid
    from cvzone.HandTrackingModule import HandDetector
    Handmodel = HandDetector(maxHands=1)
    cap = cv2.VideoCapture(0)
    
    def ec2():
        os.system("aws ec2 run-instances --image-id ami-057752b3f1d6c4d6c --instance-type t2.micro")
        os.system("firefox https://ap-south-1.console.aws.amazon.com/ec2/home?region=ap-south-1#Instances:")
        time.sleep(3)
    
    def s3(UUID):
        x = str(UUID)
        os.system(f"aws s3 mb s3://mybucket123{x} --region ap-south-1")
        os.system("firefox https://s3.console.aws.amazon.com/s3/home?region=ap-south-1#")
        time.sleep(3)

    while True:
        UUID  = uuid.uuid1().int
        status, photo = cap.read()
        hand,image = Handmodel.findHands(photo)
        cv2.imshow("myphoto", image)
        if hand:
            fingers = Handmodel.fingersUp(hand[0])
            if fingers == [1,0,0,0,0]:
                ec2()
            if fingers == [0,1,0,0,0]:
                s3(UUID)
            if fingers == [1,1,0,0,1]:
                os.system("firefox https://chat.openai.com/")
                time.sleep(3)
            if fingers == [0,1,1,0,0]:
                os.system("firfefox www.google.com")
                time.sleep(3)
            if fingers == [0,0,0,0,1]:
                break
        if cv2.waitKey(1) == 13:
            break
    cv2.destroyAllWindows()
    cap.release()

# Chatbot Function
def bot():
    os.system("firefox http://65.1.111.174/")

# Filter Function
def filter(text):
   
    import os
    import numpy as np
    import cv2
    cap=cv2.VideoCapture(0)
    status,photo=cap.read()
    print(text)
    text = text.lower()
    if 'distance' in text:
        faceModel=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        myCoordinates=faceModel.detectMultiScale(photo)
        x1=myCoordinates[0][0]
        y1=myCoordinates[0][1]
        x2=myCoordinates[0][2]+x1
        y2=myCoordinates[0][3]+y1
        width=myCoordinates[0][3]
        object_width=20
        focal_length=500
        object_width_pixels = photo[y1:y2,x1:x2].shape[1]
        distance= (object_width * focal_length) /object_width_pixels
        print(f" Distance of Object from camera is {distance} cm")
        
    if 'remove' in text and 'background' in text:
        faceModel=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        myCoordinates=faceModel.detectMultiScale(photo)
        x1=myCoordinates[0][0]
        y1=myCoordinates[0][1]
        x2=x1+myCoordinates[0][2]
        y2=y1+myCoordinates[0][3]
        newphoto=photo.copy()
        cv2.rectangle(newphoto,(x1,y1),(x2,y2),[0,255,0],5)
        blurred_image=newphoto.copy()
        blurred_image = cv2.GaussianBlur(blurred_image, (15, 15), 20)
        final_image=blurred_image.copy()
        final_image[y1:y2, x1:x2] = newphoto[y1:y2, x1:x2]
        cv2.imshow("myphoto",final_image)
        cv2.waitKey()
        cv2.destroyAllWindows()
        
    if 'remove' in text and 'face' in text:
        faceModel=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        myCoordinates=faceModel.detectMultiScale(photo)
        x1=myCoordinates[0][0]
        y1=myCoordinates[0][1]
        x2=x1+myCoordinates[0][2]
        y2=y1+myCoordinates[0][3]
        newphoto=photo.copy()
        cv2.rectangle(newphoto,(x1,y1),(x2,y2),[0,255,0],5)
        blurred_image=newphoto.copy()
        blurred_image = cv2.GaussianBlur(blurred_image, (15, 15), 20)
        final_image=newphoto.copy()
        final_image[y1:y2, x1:x2]=blurred_image[y1:y2,x1:x2]
        cv2.imshow("myphoto",final_image)
        cv2.waitKey()
        cv2.destroyAllWindows()
        
    if 'funny' in text:
        img = photo

        # 1) Edges
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

        # 2) Color
        color = cv2.bilateralFilter(img, 9, 300, 300)

        # 3) Cartoon
        cartoon = cv2.bitwise_and(color, color, mask=edges)

        cv2.imshow("Cartoon", cartoon)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Docker Function
def docker(text):
    f = os.popen("sudo pacman -Q docker").read()
    if f == " ":
        os.system("sudo pacman -S docker -y")
        os.system("sudo systemctl start docker")
        os.system("sudo systemctl enable docker")
    if "new" and "container" in text:
        if "detached" in text:
            if "name" in text:
                if "centos" in text:
                    y=os.popen("sudo docker run -dit --name os{} centos:7").read()
                    print(y)
                elif "ubuntu" in text:
                    y=os.popen("sudo docker run -dit --name os{} ubuntu14.04").read()
                    print(y)
                else:
                    y = "void and avoided"
                    print(y)
            else:
                if "centos" in text:
                    y = os.popen("sudo docker run -dit centos:7").read()
                    print(y)
                elif "ubuntu" in text:
                    y = os.popen("sudo docker run -dit ubuntu14.04").read()
                    print(y)
                else:
                    y = "void and avoided"
                    print(y)
        else:
            if "name" in text:
                if "centos" in text:
                    y = os.popen("sudo docker run -dit --name os{} centos:7").read()
                    print(y)
                elif "ubuntu" in text:
                    y = os.popen("sudo docker run -dit --name os{} ubuntu:14.04").read()
                    print(y)
                else:
                    y = os.popen("sudo docker run -dit --name os{} centos:7").read()
                    print(y)
            else:
                if "centos" in text:
                    y = os.popen("sudo docker run -dit centos:7").read()
                    print(y)
                elif "ubuntu" in text:
                    y = os.popen("sudo docker run -dit ubuntu14.04").read()
                    print(y)
                else:
                    y = "void and avoided"
                    print(y)

    if "show" and "containers" in text:
        if  "active" in text:
            y = os.popen("sudo docker ps").read()
            print(y)
        else:
            y = os.popen("sudo docker ps -a").read()
            print(y)

    if "remove"  and "containers" in text:
        if "all" in text:
            y = os.popen("sudo docker rm -f $(docker ps -a -q)").read()
            print(y)
        else:
            for i in text.split():
                if(i.startswith("os")):
                    y = os.popen("sudo docker rm {}".format(i)).read()
                    print(y)

    if "inside" and "container" in text:
        for i in text.split():
                if(i.startswith("os")):
                    os.system("sudo docker start {}".format(i))
                    y = os.popen("sudo docker attach {}".format(i)).read()
                    print(y)

# Linux Function
def linux(text):
    text = text.lower()
    if "neofetch" in text:
        y = os.popen("neofetch").read()
        print(y)
    elif "update" in text:
        if "system" in text:
            y = os.popen("sudo pacman -Syu -y").read()
            print(y)
        elif "docker" in text:
            y = os.popen("sudo pacman -Syu docker -y").read()
            print(y)
        elif "flutter" in text: 
            y = os.popen("sudo yay -Syu flutter -y").read()
            print(y)
        elif "gedit" in text: 
            y = os.popen("sudo pacman -Syu kwrite -y").read()
            print(y)
        else:
            y = "We are still working to set it up"
            print(y)
            
    elif "manual" in text: 
        if "vim" in text: 
            y = os.popen("man vim").read()
            print(y)
        elif "yum" in text: 
            y = os.popen("man yum").read()
            print(y)
        elif "neofetch" in text: 
            y = os.popen("man neofetch").read()
            print(y)
        elif "which" in text: 
            y = os.popen("man which").read()
            print(y)
        else: 
            y = "void and null"
            print(y)

    elif "where" in text: 
        if "kill all" in text: 
            y = os.popen("which killall").read()
            print(y)
        elif "cat" in text: 
            y = os.popen("which cat").read()
            print(y)
        elif "yum" in text: 
            y = os.popen("which yum").read()
            print(y)
        elif "neofetch" in text: 
            y = os.popen("which neofetch").read()
            print(y)
        elif "date" in text: 
            y = os.popen("which date").read()
            print(y)
        elif "cal" in text: 
            y = os.popen("which cal").read()
            print(y)
        else: 
            y = "we are still doing it~"
            print(y)
    elif "memory" in text: 
        y = os.popen("free").read()
        print(y)
    elif "variables" and "environment" in text: 
        y = os.popen("env").read()
        print(y)
    elif "japanese" and "browser" in text: 
        y = os.popen("browsh").read()
        print(y)
    elif "firefox" and "google" in text:
        y = os.popen("firefox google.com").read()
        print(y)
    elif "network" and "ports" in text:
        y = os.popen("sudo netstat -anp | grep tcp").read()
        print(y)
    elif "which" and "user" and "am" and "i" in text:
        y = os.popen("whoami").read()
        print(y)
    else:
        print("we are still adding the feature, thank you")

# Function to process the voice command and trigger actions
def process_voice_command():
    global text
    text = voice_command_entry.get()
    if 'hand' in text:
        threading.Thread(target=hand).start()
    elif 'chatbot' in text:
        threading.Thread(target=bot).start()
    elif 'filter' in text:
        threading.Thread(target=filter, args=(text,)).start()
    elif 'docker' in text:
        threading.Thread(target=docker, args=(text,)).start()
    elif 'linux' in text:
        threading.Thread(target=linux, args=(text,)).start()
    else:
        messagebox.showinfo("Not Supported", "This command is not supported yet.")

# Create the main Tkinter window
root = tk.Tk()
root.title("Voice Assistant")

# Create the input field for voice commands
voice_command_label = tk.Label(root, text="Enter your voice command:")
voice_command_label.pack()
voice_command_entry = tk.Entry(root, width=50)
voice_command_entry.pack()

# Create the button to trigger the actions
execute_button = tk.Button(root, text="Execute Command", command=process_voice_command)
execute_button.pack()

# Start the Tkinter main loop
root.mainloop()

