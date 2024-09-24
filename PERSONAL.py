import webbrowser
import subprocess
import os

blank = True

while blank == True :
    print (" Currently setup activities : pd, gb,fivem,FAA ")
    activity=input ("what are we doing today? : ").lower().strip()
    if activity == "pd" :
        webbrowser.open('https://sandyroleplaycad.hamz.pro/login.php')
        webbrowser.open('https://docs.google.com/spreadsheets/d/14Fw0il4OAdKhXylXCXhAWjtbMhLOv4uJHYRKDJtghG8/edit?gid=370252680') #penal codes
        webbrowser.open('https://docs.google.com/document/d/1h9sm736YgR164OR5N5WWOeicp4FhfPsDypidABkK_OY/edit') #SOP
        webbrowser.open('https://docs.google.com/document/d/1oohJewH1hD_UwVRC-UIGxFIoHSLPOtUoI52LwmQ3PuI/edit') # HEAT
        webbrowser.open('https://docs.google.com/document/d/1YYwZk9Xwx4nWT-miO7ephTsJ9Lx1ifmygIV4kbMp32o/edit') #SRT
        webbrowser.open ("https://docs.google.com/document/d/1iJOxmZEce6Py62JTe34h-GbUmoOi7hNmSudnbCmd0iI/edit#heading=h.6mxia2nhr1wb") #ASU
        webbrowser.open('http://spotify.com')
        blank = True
    if activity == "faa":
        webbrowser.open ("https://docs.google.com/document/d/1_w_fHEYub8SN91RHZthrvR56-2w3QkYz5xr4uAK5NZ8/edit")
        
    if activity == "fivem":
        subprocess.call("c:\\fivem.exe") #fivem
        subprocess.call("c:\\crosshairx.exe") #crosshair  X   
        
    
    #if activity== "gb"
        #close crosshair X subprocess.call(["taskkill","/F","/IM","crosshairX.exe"])
        #open Ground Branch subprocess.call('C:\\myprogram.exe')
        
    



    if activity == "end":
        blank = False 
