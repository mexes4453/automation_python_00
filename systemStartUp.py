import os, subprocess, time

programs = {
                "notes"   : r"C:\notes\notes.exe",
                "notepad" : r"C:\Program Files\Notepad++\notepad++.exe",
                "chrome"  : r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
                "sap"     : r"C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplgpad.exe",
                "oneNote" : "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\OneNote 2016.lnk"
            }


def launchPrograms(programs):
    #print(programs.keys())
    try:
        for app in programs.keys():
            subprocess.Popen([programs[app]])
            print(app, "\n")
            time.sleep(3)
        print("Apps launched successfully", "\n")
    except:
        print(app, "was not successful\n")



if __name__=="__main__":
    launchPrograms(programs)
    esc = input("press enter to exit: ")
    


"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\OneNote 2016.lnk"