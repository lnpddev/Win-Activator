import os
import subprocess
import time
import tempfile
import sys
from clint.textui import colored
import smtplib
import webbrowser

class windows_activator:
    def __init__(self):
        print(colored.blue("mr beast windows activator"))       
        print(colored.blue("Yeah, this works."))    
    def locate(self):
        self.temp_folder=tempfile.gettempdir()
        os.chdir(self.temp_folder)
    def activate(self):
        with open("activated.bat","w",encoding="utf-8") as activated:
            activated.write("""
:: Q:\Test\2019\04\07\SU_1422368.cmd
@Echo off&SetLocal EnableExtensions EnableDelayedExpansion
Set "WinVerAct="
For /f "tokens=*" %%W in ('
    cscript /Nologo "C:\Windows\System32\slmgr.vbs" /xpr
') Do Set "WinVerAct=!WinVerAct! %%W"
if Not defined WinVerAct ( 
    Echo:No response from slmgr.vbs
    Exit /B 1
)
Echo Windows Version Activation Status:
Echo:"%WinVerAct:~1%"
""")
            
        os.system("activated.bat > activated.txt")
        with open ("activated.txt","r",encoding="utf-8") as file:
            file=file.read()
        if "will expire" in file:
            print(colored.green("[+]Windows is already activated!"))
            print(colored.green("\nPress any key to continue"))
            input("")
            sys.exit()
        else:
            print(colored.green("[+]Windows Activating.."))
            search=subprocess.check_output(["systeminfo"])
            search=str(search)
            if "Professional Education" in search:
                key="6TP4R-GNPTD-KYYHQ-7B7DP-J447Y"
            elif "Home" in search or "home" in search or "HOME" in search:
                key="TX9XD-98N7V-6WMQ6-BX7FG-H8Q99"
            elif "Education" in search:
                key="NW6C2-QMPVW-D7KKK-3GKT6-VCFB2"
            elif "Enterprise" in search:
                key="NPPR9-FWDCX-D2C8J-H872K-2YT43"
            elif "Core" in search:
                key="33QT6-RCNYF-DXB4F-DGP7B-7MHX9"
            elif "build" in search:
                key="VK7JG-NPHTM-C97JM-9MPGT-3V66T"
            elif "Pro" in search or "pro" in search or "PRO" and not "Professional" in search:
                if "Professional Workstations" in search:
                    key="NRG8B-VKK3Q-CXVCJ-9G2XF-6Q84J"
                key="W269N-WFGWX-YVC9B-4J6C9-T83GX"

            os.system("slmgr /ipk "+str(key))
            os.system("slmgr /skms kms8.msguides.com")
            os.system("slmgr /ato")
            print(colored.green("[+]This might take a while!"))
            time.sleep(60)
            with open("activated.bat","w",encoding="utf-8") as activated:
                activated.write("""
:: Q:\Test\2019\04\07\SU_1422368.cmd
@Echo off&SetLocal EnableExtensions EnableDelayedExpansion
Set "WinVerAct="
For /f "tokens=*" %%W in ('
    cscript /Nologo "C:\Windows\System32\slmgr.vbs" /xpr
') Do Set "WinVerAct=!WinVerAct! %%W"
if Not defined WinVerAct ( 
    Echo:No response from slmgr.vbs
    Exit /B 1
)
Echo Windows Activation Status:
Echo:"%WinVerAct:~1%"
""")
            os.system("activated.bat > activated.txt")
            with open ("activated.txt","r",encoding="utf-8") as file:
                file=file.read() 
            if "will expire" in file:
                print(colored.green("[+]Windows activated sucessfully! This will restart soon!"))
                os.system("shutdown /r /t 1")
                input("")
                sys.exit()
            else:
                print(colored.red("[+]Something went wrong! Check your antivirus!"))
                print(colored.green("\nPress any key to continue"))
                input("")
                sys.exit()

w_a=windows_activator()
w_a.locate()
w_a.activate()
