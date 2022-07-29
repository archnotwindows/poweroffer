#Libraries for create a window
import tkinter as tk
#Libraries for execute command
import subprocess
#Libraries for read web browser history
from browser_history.browsers import Firefox

#Print all browser history on txt
with open('history.txt', 'w') as f:
    fi = Firefox()
    outputs = fi.fetch_history()
    his = outputs.histories
    for line in his:
        f.write(str(line))
        f.write('\n')

window = tk.Tk() 
#Resolution program
window.geometry("800x500")
#Title program
window.title("Poweroffer")
#Background program
window.configure(background="blue")
window.grid_columnconfigure(0, weight=1) 

scritta = tk.Label(window, text="Welcome!", font=("Helvetica",15)) 
scritta.grid(row=0, column=0,  sticky="N", padx=20, pady=10)      

sito = tk.StringVar
text_input= tk.Entry(textvariable=sito)
text_input.grid(row=3, column=0, sticky="WE", padx=10, pady=10)

#Shutdown pc
def spegni():
    subprocess.run('shutdown now', shell=True)
    subprocess.run('shutdown -s -t O', shell=True)

#If i visit youtube, shutdown pc
def smetti():
    sito = text_input.get() 
    print(sito)

    f = open ("siti.dat","w")
    f.write(sito)
    f.close()

    a = open("executable.py","w")
    a.write("#!/usr/bin/env python3 \n")
    a.write("import os,json,lz4.block,time \n")
    a.write("f = open(\"siti.dat\",\"r\") \n")
    a.write("sito = f.read()\n")
    a.write("d = open(\"/home/usr/snap/firefox/common/.mozilla/firefox/8gnxd9f4.default/sessionstore-backups/recovery.jsonlz4\", \"rb\") \n")
    a.write("magic = d.read(8)\n")
    a.write("data = json.loads(lz4.block.decompress(d.read()).decode(\"utf-8\"))\n")
    a.write("d.close()\n")
    a.write("current_window = \"\"\n")
    a.write("for win in data.get(\"windows\"):\n")
    a.write("   for tab in win.get(\"tabs\"):\n")
    a.write("       i = int(tab.get(\"index\")) - 1 \n")
    a.write("       current_window = tab.get(\"entries\")[i].get(\"url\")\n")
    a.write("print(current_window)\n")
    a.write("if sito in str(current_window):\n")
    a.write("   print(\"Yes\")\n")
    a.write("   os.system(\"shutdown now\")")
    a.close()

    
    b = open("executable.sh", "w")
    b.write("#!/bin/bash\n")
    b.write("/home/lorenzo/Scrivania/poweroffer/executable.py")
    b.close()

    

#Button stop procrastinating
second_button= tk.Button(text="Stop procrastinating", command=smetti)
second_button.grid(row=5, column=0, sticky="WE", padx=15, pady=8)

#Button for shutdown pc
first_button = tk.Button(text="have a break from the pc", command=spegni) 
first_button.grid(row=1, column=0, sticky="W", padx=50, pady=50) 

#Always open window
if __name__ == "__main__":
    window.mainloop()