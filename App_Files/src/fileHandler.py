"""
This file contains functions useful for storing data of the App in files
"""
import os

def saveSchedule(link, hour, minutes, durH, durMin, day):
    """
    Saves the information of the Meeting in 2 files:
    -schedules.txt stores the information to be accessed from the autoRecord's methods
    -prettySchedules.txt stores the infromation in a way to bew later presented to the user
    """
    integers_list = [hour, minutes, durH, durMin]
    areIntegers = True
    validity = False
    for i in range(len(integers_list)):
        if integers_list[i].isdigit() == False:
            areIntegers = False
            break
    if 0<=int(hour)<=23 and 0<=int(minutes)<=59 and 0<=int(durH)<=23 and 0<=int(durMin)<=59  and day != '':
        validity = True
    if areIntegers and validity:
        try:
            info = day + " " + hour + " " + minutes + " " + durH + " " +durMin + " " + link
            f = open("schedules.txt", "a")
            f.write(info)
            f.write('\n')
            f.close()

            f = open("prettySchedules.txt", "r")
            numOfInsert = len(f.readlines())+1
            f.close()
            f = open("prettySchedules.txt", "a")
            info = str(numOfInsert) + ". " + day + ": " + hour + ":" + minutes + ", Duration: " + durH + ":" + durMin + ", Link: " + link
            f.write(info)
            f.write('\n')
            f.close()
            return True
        except:
            return False
    return False
        
def getSchedule():
    """
    Reads the information from prettySchedules.txt
    """
    f = open("prettySchedules.txt", "r")
    toReturn = f.read()
    if(toReturn == ""):
        toReturn = "No Scheduled Recordings yet"
    f.close()
    return toReturn 

def getRecs():
    """
    Reads the information from schedules.txt
    """
    f = open("schedules.txt", "r")
    toReturn = f.read()
    if(toReturn == ""):
        toReturn = "No Scheduled Recordings yet"
    f.close()
    return toReturn

def deleteSchedule(num):
    """
    Deletes a schedule from prettySchedules.txt and schedules.txt
    """
    if num.isdigit():
        num = int(num)
    else:
        return
    f1 = open("schedules.txt", "r")
    f2 = open("prettySchedules.txt", "r")
    allLines = f1.readlines()
    allLines2 = f2.readlines()
    f1.close()
    f2.close()
    numOfLines = len(allLines)
    if 1<= num <=numOfLines:
        allLines.remove(allLines[num-1])
        allLines2.remove(allLines2[num-1])
        f1 = open("schedules.txt", "w")
        f2 = open("prettySchedules.txt", "w")
        allLines = ''.join([str(elem) for elem in allLines])
        for i in range(numOfLines-1):
            allLines2[i] = str(i+1) + allLines2[i][1:]
        allLines2 = ''.join([str(elem) for elem in allLines2])
        f1.write(allLines)
        f2.write(allLines2)
        f1.close()
        f2.close()
    else:
        return

def savePath(path):
    """
    Saves OBS' path in path.txt file
    """
    newpath = path.replace(os.sep, '/')
    f = open("path.txt", "w")
    f.write(newpath)
    f.close()


def saveRecordingCompleted(link):
    """
    saves the information that the meeting with Link 'link' has been recorded 
    """
    f = open("recCompleted.txt", "w")
    f.write(link)
    f.close()

def recordingDone(link):
    f = open("recCompleted.txt", "r")
    fileLink = f.read()
    f.close()
    if link == fileLink:
        return True
    else:
        return False

def deleteAllSched():
    f1 = open("schedules.txt", "w")
    f2 = open("prettySchedules.txt", "w")
    f1.write('')
    f2.write('')
    f1.close()
    f2.close()

