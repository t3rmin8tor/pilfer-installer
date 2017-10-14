#!/usr/bin/env python
import tkinter.ttk
from tkinter import *
import  os
import datetime 
import getpass
record_path=os.path.expanduser ('~\\Desktop\\')
now = datetime.datetime.now().strftime("%H-%M-%S") 
user=getpass.getuser() 
root = tkinter.Tk(className ="pilfer v 1.3")

note = tkinter.ttk.Notebook(root)

tab1 = Frame(note)
#tab2 = Frame(note)
tab3 = Frame(note)
#tab4 = Frame(note)
tab5 = Frame(note)
#Pilfer
Label(tab1, text="Chan to record").grid(row=0)
Label(tab1, text="Duration").grid(row=1)
#Pilfer-TS
#Label(tab2, text="enter url.m3U-M3U8").grid(row=1)
#Checkbutton(tab2, text="combine Ts Files").grid(row=2) 
#schedule

Label(tab3, text="Chan to record").grid(row=1) 
Label(tab3, text="Date").grid(row=2)  
Label(tab3, text="Start Time").grid(row=3)  
Label(tab3, text="Duration").grid(row=4)



#Rip-Record
chan = Entry(tab1) 
duration = Entry(tab1) 
#Pilfer-ts 
#tsfile = Entry(tab2) 

#schedule
schedchan = Entry(tab3)
scheddate = Entry(tab3) 
schedtime = Entry(tab3)
scheddur = Entry(tab3)

#rip-Record

chan.grid(row=0, column=1) 
duration.grid(row=1, column=1)


def config():
	os.system('pip3 install --user git+https://github.com/NapoleonWils0n/pilfer.git')
Button(tab5, text='configure pilfer', command=config).grid(row=2, column=0, sticky=W, pady=4)

def update():
	os.system('pip3 install --upgrade --user git+https://github.com/NapoleonWils0n/pilfer.git')
Button(tab5, text='Check for update', command=update).grid(row=2, column=3, sticky=W, pady=4)

def checkdur():
	if duration.get() == '':
		record()
	else:
		record_dur()
	
def record_dur():
	os.system('C:\Windows\System32\cmd.exe /c pilfer.exe ' + '-i ' + str(record_path) + chan.get() + ' -t ' + duration.get())

def record():
	os.system('C:\Windows\System32\cmd.exe /c pilfer.exe ' + '-i ' + str(record_path) + chan.get())
Button(tab1, text='record', command=checkdur).grid(row=4, column=0, sticky=W, pady=4)
Button(tab1, text='cancel', command=exit).grid(row=4,column=1, sticky=W, pady=4)


#rip-TS 
#tsfile.grid(row=1, column=1)
#schedule 

schedchan.grid(row=1, column=1)
scheddate.grid(row=2, column=1)
schedtime.grid(row=3, column=1)
scheddur.grid(row=4, column=1)

def create_url():
	os.system('schtasks /create /sc ONCE /tn "' + scheddate.get() + str(now) + '" /tr "C:\Windows\System32\cmd.exe /c pilfer.exe -i ' + schedchan.get()  +  ' -t ' + scheddur.get() +'"  /sd '+ scheddate.get() + ' /st ' + schedtime.get())


def create_file():
	os.system('schtasks /create /sc ONCE /tn "' + schedchan.get() + scheddate.get() + str(now) + '" /tr "C:\Windows\System32\cmd.exe /c pilfer.exe -i ' +str(record_path) + schedchan.get()  +  ' -t ' + scheddur.get() +'"  /sd '+ scheddate.get() + ' /st ' + schedtime.get())
Button(tab3, text='create_from_file', command=create_file).grid(row=9, column=2, sticky=W, pady=4)
Button(tab3, text='create_from_url',command=create_url).grid(row=9, column=1, sticky=W, pady=4)



note.add(tab1, text = "Pilfer")
# note.add(tab2, text = "Pilfer-TS")
note.add(tab3, text = "Schedule")
# note.add(tab4, text ="delete schedules")
note.add(tab5, text ="config")
note.pack()
print ('Pilfer initialising')
root.mainloop()
