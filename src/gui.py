"""
Author: Tsamouridis Anastasios Athanasios
"""
import tkinter as tk
from tkinter.font import Font
from tkinter import messagebox, ttk

# from my files
import fileHandler as fh
import autoRecord as ar

class Gui:
    """
    Class Gui

    Creates the User Interface of the App
    """
    def __init__(self):
        """
        Creates a new object of class Gui
        """
        self.autoRec = ar.autoRecord()
        self.root = tk.Tk()
        self.root.title("OZ Automatic Recorder")
        self.root.resizable(False, False)
        self.root.iconbitmap('images/icon.ico')
        myFont = Font(family="Calibri", size = 20)

        self.frame = tk.Frame(self.root, bg = 'gray60')
        
        self.b_runApp = tk.Button(self.frame,  text = 'Run', bg = 'gray20', fg = 'white', padx = 5, pady = 5, command = self.clickOn_b_runApp)
        self.b_runApp.grid(row = 0, column = 0, padx=20, pady=40)
        self.b_runApp.config(font = myFont)

        self.b_scheduleMeeting = tk.Button(self.frame,  text = 'Schedule a Recording', bg = 'white', fg = 'black', padx = 5, pady = 5, command = self.clickOn_b_scheduleMeeting)
        self.b_scheduleMeeting.grid(row = 0, column = 1, padx=20, pady=40)
        self.b_scheduleMeeting.config(font = myFont)

        self.b_show = tk.Button(self.frame,  text = 'Scheduled Recordings', bg = 'white', fg = 'black', padx = 5, pady = 5, command = self.show)
        self.b_show.grid(row = 1, column = 0, columnspan = 2, padx=20, pady=5)
        myFont = Font(family="Calibri", size = 15)
        self.b_show.config(font = myFont)

        self.b_configure = tk.Button(self.frame,  text = 'Path configuration', bg = 'white', fg = 'black', padx = 5, pady = 5, command = self.pathDialog)
        self.b_configure.grid(row = 2, column = 0, columnspan = 2, padx=20, pady=5)
        myFont = Font(family="Calibri", size = 15)
        self.b_configure.config(font = myFont)

        self.frame.grid()
        self.root.mainloop()

    def pathDialog(self):
        """
        pathDialog method

        Opens a new window for the user to edit the OBS' path
        """
        self.closeTopLevels()
        pathWindow = tk.Toplevel()
        pathWindow.resizable(False, False)
        pathWindow.iconbitmap('images/icon.ico')
        l_path = tk.Label(pathWindow, text = "Paste the OBS' path in your system: ")
        l_path.grid(row=0, column = 0, padx=7, pady = 7)
        e_path = tk.Entry(pathWindow, width = 30)
        e_path.event_add('<<Paste>>', '<Control-v>')
        e_path.event_add('<<Paste>>', '<Control-V>')
        e_path.grid(row = 0, column = 1, padx=7, pady = 7)

        def confirmAndSave():
            ans = messagebox.askquestion("Confirm path", "Do you want to save the path provided")
            if ans == 'yes':
                fh.savePath(e_path.get())
                pathWindow.destroy()
                pathWindow.update()
            else:
                pass

        b_path = tk.Button(pathWindow, text = "Confirm", command = confirmAndSave)
        b_path.grid(row = 0, column = 2, padx=7, pady = 7)

        def setDefault():
            """
            Sets the default OBS' path 
            """
            fh.savePath('C:/Program Files/obs-studio/bin/64bit')
            pathWindow.destroy()
            pathWindow.update()
        b_default = tk.Button(pathWindow, text = "Reset path to default", command = setDefault)
        b_default.config(bg = 'black', fg = 'white')
        b_default.grid(row = 1, columnspan = 3, padx=7, pady = 7)

    def show(self):
        """
        show method

        Opens a new window displaying Scheduled Recordings. 
        User can delete a schedule recording from here
        """
        myFont = Font(family="Calibri",size=20,weight="bold")
        allSchedules = fh.getSchedule()
        self.closeTopLevels()
        schedulewindow = tk.Toplevel()
        schedulewindow.resizable(False, False)
        schedulewindow.iconbitmap('images/icon.ico')
        intro = "You have scheduled the following recordings:\n"
        l_intro = tk.Label(schedulewindow, text = intro)
        l_intro.config(font = myFont)
        l_intro.grid(row = 0, column = 0, columnspan = 3)

        myFont = Font(family="Calibri",size=13)
        l_schedule = tk.Label(schedulewindow, text =  allSchedules)
        l_schedule.config(font = myFont)
        l_schedule.grid(row = 1, column = 0, columnspan = 3)

        l_delete = tk.Label(schedulewindow, text="Delete recording No: ")
        l_delete.grid(row=2, column = 0, sticky = 'ew', padx = 20, pady = 20)

        e_delete = tk.Entry(schedulewindow)
        e_delete.grid(row=2, column =1, sticky = 'ew', padx = 20, pady = 20)

        def updateSchedules():
            if e_delete.get() != '':
                mes = 'Do you want to delete recording #' + str(e_delete.get()) + '?'
                ans = messagebox.askquestion('Delete Recording', mes)
                if ans == 'yes':    
                    fh.deleteSchedule(e_delete.get())
                    allSchedules = fh.getSchedule()
                    l_schedule.config(text=allSchedules)
                    schedulewindow.attributes('-topmost', 'true')
                    schedulewindow.attributes('-topmost', 'false')
                else:
                    pass

        def deleteAll():
            mes = 'Do you want to delete ALL recordings? This action cannot be undone...'
            ans = messagebox.askquestion('Delete Recording', mes)
            if ans == 'yes':    
                fh.deleteAllSched()
                allSchedules = 'No Scheduled Recordings yet'
                l_schedule.config(text=allSchedules)
                schedulewindow.attributes('-topmost', 'true')
                schedulewindow.attributes('-topmost', 'false')

        myFont = Font(family="Calibri",size=15,weight="bold")
        b_delete = tk.Button(schedulewindow, text = 'Delete', bg = 'red', fg = 'white', command = updateSchedules)
        b_delete.config(font = myFont)
        b_delete.grid(row = 2, column=2, sticky = 'nsew')

        b_deleteAll = tk.Button(schedulewindow, text = 'Delete All Scheduled Recordings', bg = 'black', fg = 'white', command = deleteAll)
        b_deleteAll.grid(row = 3, columnspan=3, sticky = 'nsew')

    def closeTopLevels(self):
        """
        closeTopLevels method

        Closes all topLevel Windows user has opened
        """
        for widget in self.root.winfo_children():
                if isinstance(widget, tk.Toplevel):
                    widget.destroy()

    def callEverySec(self):
        """
        callEverySec method

        Implements the loop that checks when a recording should start and end
        """
        self.autoRec.start()
        self.autoRec.stop()
        if self.b_runApp.cget('text') != 'Run':
            self.root.after(1000, self.callEverySec)
        

    def clickOn_b_runApp(self):
        """
        clickOn_b_runApp method

        Implements the preferable actions when user pushes Run button
        """
        if self.b_runApp.cget('text') == 'Run':
            self.b_scheduleMeeting["state"] = tk.DISABLED
            self.b_show["state"] = tk.DISABLED
            self.b_configure["state"] = tk.DISABLED
            self.b_runApp.config(text = "Stop Running")
            self.closeTopLevels()
            self.callEverySec()

        else:
            self.b_scheduleMeeting["state"] = tk.NORMAL
            self.b_show["state"] = tk.NORMAL
            self.b_configure["state"] = tk.NORMAL
            self.b_runApp.config(text = "Run")
            self.autoRec.setStopVar(True)
            f = open('data_files/recCompleted.txt', 'w')
            f.write('')
            f.close()

    def clickOn_b_scheduleMeeting(self):
        """
        clickOn_b_scheduleMeeting method

        Implements the preferable actions when user pushes Schedule Meeting button
        """
        self.closeTopLevels()
        scheduleDialog = tk.Toplevel()
        scheduleDialog.resizable(False, False)
        scheduleDialog.iconbitmap('images/icon.ico')

        l_link = tk.Label(scheduleDialog, text = "Meeting's Link: ")
        l_link.grid(row=0, column=0,padx=20, pady=20)
        e_link = tk.Entry(scheduleDialog, bg = 'white', fg = 'black')
        e_link.grid(row=0, column=1,padx=20, pady=20)
        e_link.event_add('<<Paste>>', '<Control-V>')
        e_link.event_add('<<Paste>>', '<Control-v>')

        l_hour = tk.Label(scheduleDialog, text = "Recording start time(hour): \n [0-23]")
        l_hour.grid(row=1, column=0)
        e_hour = tk.Entry(scheduleDialog, bg = 'white', fg = 'black')
        e_hour.grid(row=1, column=1,padx=20, pady=20)
        e_link.event_add('<<Paste>>', '<Control-v>')
        e_hour.event_add('<<Paste>>', '<Control-V>')
        hour = e_hour.get()

        l_min = tk.Label(scheduleDialog, text = "Recording start time(min): \n[0-59]")
        l_min.grid(row=2, column=0,padx=20, pady=20)
        e_min = tk.Entry(scheduleDialog, bg = 'white', fg = 'black')
        e_min.grid(row=2, column=1,padx=20, pady=20)
        e_link.event_add('<<Paste>>', '<Control-v>')
        e_min.event_add('<<Paste>>', '<Control-V>')

        l_durH = tk.Label(scheduleDialog, text = "Duration(hours): \n[0-23]")
        l_durH.grid(row=3, column=0,padx=20, pady=20)
        e_durH = tk.Entry(scheduleDialog, bg = 'white', fg = 'black')
        e_durH.grid(row=3, column=1,padx=20, pady=20)
        e_link.event_add('<<Paste>>', '<Control-v>')
        e_durH.event_add('<<Paste>>', '<Control-V>')

        l_durMin = tk.Label(scheduleDialog, text = "Duration(Minutes): \n[0-59]")
        l_durMin.grid(row=4, column=0,padx=20, pady=20)
        e_durMin = tk.Entry(scheduleDialog, bg = 'white', fg = 'black')
        e_durMin.grid(row=4, column=1,padx=20, pady=20)
        e_link.event_add('<<Paste>>', '<Control-v>')
        e_durMin.event_add('<<Paste>>', '<Control-V>')

        n = tk.StringVar() 
        dayPicker = ttk.Combobox(scheduleDialog,state="readonly", width = 15, textvariable = n) 

        # Adding combobox drop down list 
        dayPicker['values'] = ('Monday',  
                                'Tuesday', 
                                'Wednesday', 
                                'Thursday', 
                                'Friday', 
                                'Saturday', 
                                'Sunday') 

        dayPicker.grid(row=5, column = 1)

        l_dayPicker = tk.Label(scheduleDialog, text="Select Day of Recording:")
        l_dayPicker.grid(row=5, column = 0, padx=20, pady=20)
        dayPicker.current(0)



        def emptyEntries():
            """
            Clears all Entries user has filled in
            """
            e_durH.delete(0,tk.END)
            e_durMin.delete(0,tk.END)
            e_hour.delete(0,tk.END)
            e_link.delete(0,tk.END)
            e_min.delete(0,tk.END)
            dayPicker.current(0)

        def saveAndInform():
            """
            Saves the schedule and informs user if this action was successful
            """
            success = fh.saveSchedule(e_link.get(), e_hour.get()[:2], e_min.get()[:2], e_durH.get()[:2], e_durMin.get()[:2], dayPicker.get())
            if success:
                ans = messagebox.askquestion(title='Successfully saved', message='Your Meeting is succesfully saved. Do you want to add another meeting?')
                if ans == 'no':
                    scheduleDialog.destroy()
                    scheduleDialog.update()
            else:
                scheduleDialog.attributes('-topmost', 'true')
                scheduleDialog.attributes('-topmost', 'false')
                messagebox.showinfo(title='Error', message='Error: Your Meeting is not saved. Please, check and try again...')
                
        button_font = Font(family="Calibri", size = 20)
        b_confirm = tk.Button(scheduleDialog, text = "Confirm", font = button_font, command=saveAndInform)
        b_confirm.grid(row=6, column=0,padx=20, pady=20)
        b_discard = tk.Button(scheduleDialog, text = "Clear", font = button_font, command = emptyEntries)
        b_discard.grid(row=6, column=1,padx=20, pady=20)
        
Gui()
