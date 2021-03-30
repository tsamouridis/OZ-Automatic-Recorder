# OZ-Automatic-Recorder
![logo](https://github.com/tsamourid/OZ-Automatic-Recorder/blob/master/images/logo.png)

## OBS-Zoom Automatic Recorder for Windows users
Zoom Meetings Automatic Recorder using OBS Studio

This App provides the ability to automatically open a zoom Meeting at a specific time and record it using the OBS Studio software. More information about the functionality and abilities of the App are given below.

<img src="https://github.com/tsamourid/OZ-Automatic-Recorder/blob/master/images/demo1.png" alt="demo1" width="300"/> 

## Disclaimer
This app is not tested thoroughly, so user may encounter some problems. Improvements may be added later on.

## How to use
As seen above, the App provides the following choices to the user:
* **Run:** When this button is pressed OZ checks the scheduled meetings and starts a meeting and records it at the date and time specified by the user.
* **Schedule a Recording:** Opens a dialog to the user and schedules a recording. User schould provide meeting's link,date and time of the meeting, and duration of it.
* **Scheduled Recordings:** Opens a catalog with all the scheduled meetings. At this window user can also delete one or all the recordings.
* **Path configuration:** Here user can edit the OBS path in his/her system. He/She can also set the path to default, provided that the OBS is stored at:
  **C:/Program Files/obs-studio/bin/64bit**

### Run
If user wants to record a meeting he/she schould have pressed *Run* button. The interface will look like the following image. 
**Warning:** App schould not be terminated. It scould at least, run minimized.
To stop app from running press Stop Running button

<img src="https://github.com/tsamourid/OZ-Automatic-Recorder/blob/master/images/demo2.png" alt="demo2" width="300"/> 

### Schedule a Meeting
User schould enter the necessary information. Here is an image of the dialog that opens:

<img src="https://github.com/tsamourid/OZ-Automatic-Recorder/blob/master/images/demo3.png" alt="demo3" width="300"/> 

### Scheduled Recordings:
Here, user can inspect all the saved recordings and delete them.

<img src="https://github.com/tsamourid/OZ-Automatic-Recorder/blob/master/images/demo4.png" alt="demo4" width="300"/> 

### Path configuration:
User schould provide the correct path of obs executable so that OBS starts automatically with no problem. Default path is also given as an option.

<img src="https://github.com/tsamourid/OZ-Automatic-Recorder/blob/master/images/demo5.png" alt="demo5" width="300"/> 

## OBS settings:
When using this app, OBS scould be installed in user's system. Moreover, OBS schould be set to record Zoom.exe or the whole screen

## Zoom settings:
Make sure you are signed into your Zoom account. Moreover, make sure you have the following Zoom settings on:
* General:
    * Enter full screen automatically when starting or joining a meeting
* Video:
    * Turn off my video when joining a meeting
* Audio:
    * Automatically join audio by computer when joining a meeting
    * Mute my microphone when joining a meeting

## Browser settings:
Make sure your default browser opens automatically Zoom meetings and does not ask for your permission.
