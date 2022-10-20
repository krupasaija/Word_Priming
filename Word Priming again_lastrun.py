#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.2),
    on October 20, 2022, at 17:35
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.2'
expName = 'Priming'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\HP\\OneDrive\\Desktop\\Word Priming again_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "Study" ---
Studytext = visual.TextStim(win=win, name='Studytext',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
studyslider = visual.Slider(win=win, name='studyslider',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.3), units=None,
    labels=["Familiar","Unfamiliar"], ticks=(1, 2, 3, 4, 5), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-1, readOnly=False)

# --- Initialize components for Routine "Test" ---
timer_text = visual.TextStim(win=win, name='timer_text',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
    color=[1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
testtext = visual.TextStim(win=win, name='testtext',
    text='',
    font='Open Sans',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
test_textbox = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(0, 0),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='test_textbox',
     autoLog=True,
)
submit_text = visual.TextStim(win=win, name='submit_text',
    text='Click to Submit',
    font='Open Sans',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
testmouse = event.Mouse(win=win)
x, y = [None, None]
testmouse.mouseClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Tutorial5 studylist.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Study" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    Studytext.setText(Study_word)
    studyslider.reset()
    # keep track of which components have finished
    StudyComponents = [Studytext, studyslider]
    for thisComponent in StudyComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Study" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Studytext* updates
        if Studytext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Studytext.frameNStart = frameN  # exact frame index
            Studytext.tStart = t  # local t and not account for scr refresh
            Studytext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Studytext, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Studytext.started')
            Studytext.setAutoDraw(True)
        if Studytext.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Studytext.tStartRefresh + 8.0-frameTolerance:
                # keep track of stop time/frame for later
                Studytext.tStop = t  # not accounting for scr refresh
                Studytext.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Studytext.stopped')
                Studytext.setAutoDraw(False)
        
        # *studyslider* updates
        if studyslider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            studyslider.frameNStart = frameN  # exact frame index
            studyslider.tStart = t  # local t and not account for scr refresh
            studyslider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(studyslider, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'studyslider.started')
            studyslider.setAutoDraw(True)
        
        # Check studyslider for response to end routine
        if studyslider.getRating() is not None and studyslider.status == STARTED:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in StudyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Study" ---
    for thisComponent in StudyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('studyslider.response', studyslider.getRating())
    trials.addData('studyslider.rt', studyslider.getRT())
    # the Routine "Study" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('tutorial5 testlistagain.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Test" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    timer_text.setPos((0.4,0.3))
    timer_text.setText(round(10 - t, ndigits = 1))
    testtext.setText(test_word)
    test_textbox.reset()
    # setup some python lists for storing info about the testmouse
    testmouse.x = []
    testmouse.y = []
    testmouse.leftButton = []
    testmouse.midButton = []
    testmouse.rightButton = []
    testmouse.time = []
    testmouse.clicked_name = []
    gotValidClick = False  # until a click is received
    # Run 'Begin Routine' code from TimerCode
    timer_text.text = ''
    # keep track of which components have finished
    TestComponents = [timer_text, testtext, test_textbox, submit_text, testmouse]
    for thisComponent in TestComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Test" ---
    while continueRoutine and routineTimer.getTime() < 10.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *timer_text* updates
        if timer_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            timer_text.frameNStart = frameN  # exact frame index
            timer_text.tStart = t  # local t and not account for scr refresh
            timer_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(timer_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'timer_text.started')
            timer_text.setAutoDraw(True)
        if timer_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > timer_text.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                timer_text.tStop = t  # not accounting for scr refresh
                timer_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'timer_text.stopped')
                timer_text.setAutoDraw(False)
        
        # *testtext* updates
        if testtext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            testtext.frameNStart = frameN  # exact frame index
            testtext.tStart = t  # local t and not account for scr refresh
            testtext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(testtext, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'testtext.started')
            testtext.setAutoDraw(True)
        if testtext.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > testtext.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                testtext.tStop = t  # not accounting for scr refresh
                testtext.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'testtext.stopped')
                testtext.setAutoDraw(False)
        
        # *test_textbox* updates
        if test_textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test_textbox.frameNStart = frameN  # exact frame index
            test_textbox.tStart = t  # local t and not account for scr refresh
            test_textbox.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test_textbox, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'test_textbox.started')
            test_textbox.setAutoDraw(True)
        if test_textbox.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test_textbox.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                test_textbox.tStop = t  # not accounting for scr refresh
                test_textbox.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'test_textbox.stopped')
                test_textbox.setAutoDraw(False)
        
        # *submit_text* updates
        if submit_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            submit_text.frameNStart = frameN  # exact frame index
            submit_text.tStart = t  # local t and not account for scr refresh
            submit_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(submit_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'submit_text.started')
            submit_text.setAutoDraw(True)
        if submit_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > submit_text.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                submit_text.tStop = t  # not accounting for scr refresh
                submit_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'submit_text.stopped')
                submit_text.setAutoDraw(False)
        # *testmouse* updates
        if testmouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            testmouse.frameNStart = frameN  # exact frame index
            testmouse.tStart = t  # local t and not account for scr refresh
            testmouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(testmouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('testmouse.started', t)
            testmouse.status = STARTED
            testmouse.mouseClock.reset()
            prevButtonState = testmouse.getPressed()  # if button is down already this ISN'T a new click
        if testmouse.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > testmouse.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                testmouse.tStop = t  # not accounting for scr refresh
                testmouse.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('testmouse.stopped', t)
                testmouse.status = FINISHED
        if testmouse.status == STARTED:  # only update if started and not finished!
            buttons = testmouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(submit_text)
                        clickableList = submit_text
                    except:
                        clickableList = [submit_text]
                    for obj in clickableList:
                        if obj.contains(testmouse):
                            gotValidClick = True
                            testmouse.clicked_name.append(obj.name)
                    x, y = testmouse.getPos()
                    testmouse.x.append(x)
                    testmouse.y.append(y)
                    buttons = testmouse.getPressed()
                    testmouse.leftButton.append(buttons[0])
                    testmouse.midButton.append(buttons[1])
                    testmouse.rightButton.append(buttons[2])
                    testmouse.time.append(testmouse.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # abort routine on response
        # Run 'Each Frame' code from TimerCode
        timer_text.text = str(round(10-routineTimer.getTime()))
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TestComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Test" ---
    for thisComponent in TestComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('test_textbox.text',test_textbox.text)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('testmouse.x', testmouse.x)
    trials_2.addData('testmouse.y', testmouse.y)
    trials_2.addData('testmouse.leftButton', testmouse.leftButton)
    trials_2.addData('testmouse.midButton', testmouse.midButton)
    trials_2.addData('testmouse.rightButton', testmouse.rightButton)
    trials_2.addData('testmouse.time', testmouse.time)
    trials_2.addData('testmouse.clicked_name', testmouse.clicked_name)
    # Run 'End Routine' code from TimerCode
    item_status= ''
    
    if(test_textbox.text == corrAns):
        corrAns= 0
        item_status = 'hit'
    else:
        item_status = 'miss'
    thisExp.addData ('item_status', item_status)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-10.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_2'


# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
