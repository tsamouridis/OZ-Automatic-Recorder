"""
autoRecord.py

Contains the class autoRecord, which implements the main purpose of the App
"""
import datetime, webbrowser, os
import fileHandler as fh

class autoRecord:
    """
    Class autoRecord

    This class denotes the main functionalities of the App.
    Its methods check for starting and stopping a recording
    """
    def __init__(self):
        """
        Creates a new object of class autoRecord
        """
        self.stopVar = False
        self.RecondingOn = False

    def setStopVar(self, boolean):
        """
        setStopVar method

        Setter of StopVar
        """
        self.StopVar = boolean

    def dayToInt(self, text):
        """
        dayToInt method

        returns an integer from 1 to 6 representing a day of the weak
        -1 is returned, when variable text is not a day
        """
        intDay = -1
        if text == "Monday":
            intDay = 0
        elif text == "Tuesday":
            intDay = 1
        elif text == "Wednesday":
            intDay = 2
        elif text == "Thursday":
            intDay = 3    
        elif text == "Friday":
            intDay = 4    
        elif text == "Saturday":
            intDay = 5
        else:
            intDay = 6
        return intDay

    def setEnd(self, day, startH, startMin, durH, durMin):
        """
        setEnd method

        Sets the time the Recording schould be stopped
        """
        endH = 0
        endMin = 0
        borrow = 0
        if startMin + durMin >= 60:
            borrow +=1
            endMin = (startMin+durMin)-60
        else:
            endMin = startMin+durMin
        endH = startH + durH + borrow
        if endH == 24:
            endH = 0
        elif endH >= 25:
            endH = endH-24
        if endH<startH:
            day+=1
        return [day,endH, endMin]

    def start(self):
        """
        start method

        Checks if the recording schould be stαρτεδ.
        If yes, it starts OBS recording and Zoom Meeting 
        """
        allSchedules = fh.getRecs()
        if allSchedules == "No Scheduled Recordings yet":
            pass
        else:
            schedulesSplitedLines = allSchedules.splitlines()
            for recording in schedulesSplitedLines:
                info = recording.split()
                day = self.dayToInt(info[0])
                startH = int(info[1])
                startMin = int(info[2])
                link = info[5]
                if datetime.datetime.today().weekday()==day and datetime.datetime.now().time().hour == startH and datetime.datetime.now().time().minute == startMin and self.RecondingOn == False:
                    webbrowser.open(link)
                    bashCommand = 'start /d "'
                    f = open("path.txt", "r")
                    path = f.read()
                    bashCommand += path
                    bashCommand += '" obs64.exe --startrecording'
                    os.system(bashCommand)
                    self.RecondingOn = True

    def stop(self):
        """
        stop method

        Checks if the recording schould be stopped.
        If yes it kills OBS recording and Zoom Meeting 
        """
        allSchedules = fh.getRecs()
        f = open("recCompleted.txt", 'r')
        fileLink = f.read()
        f.close()
        if allSchedules == "No Scheduled Recordings yet":
            return False
        else:
            schedulesSplitedLines = allSchedules.splitlines()
            for recording in schedulesSplitedLines:
                info = recording.split()
                day = self.dayToInt(info[0])
                startH = int(info[1])
                startMin = int(info[2])
                durH = int(info[3])
                durMin = int(info[4])
                link = info[5]
                [newDay, endH, endMin] = self.setEnd(day, startH, startMin, durH, durMin)
                day = newDay
                stopRec = True
                if fileLink == link:
                    stopRec = False
                if datetime.datetime.today().weekday()==day and datetime.datetime.now().time().hour == endH and datetime.datetime.now().time().minute == endMin and stopRec==True:
                    try:
                        os.system("taskkill /F /IM obs64.exe")
                        os.system("taskkill /F /IM zoom.exe") 
                        self.RecordingOn = False
                        fh.saveRecordingCompleted(link)
                    except:
                        pass
