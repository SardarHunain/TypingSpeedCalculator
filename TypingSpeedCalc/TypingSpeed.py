from time import *
import random as r

def mistake(paragraph,usertxt):
    error = 0
    for i in range(len(paragraph)):
        try:
            if(paragraph[i]!=usertxt):
                error = error+1
        except:
            error = error+1
    return error

def speed_time(time_s,time_e,userInput):
    time_delay = time_e - time_s
    time_round_off = round(time_delay,2)
    speed = len(userInput)/time_round_off
    return round(speed)


test = ["Stimulate your mind as you test your typing speed with this standard English paragraph typing test. Watch your typing speed and accuracy increase as you learn about a variety of new topics! Over 40 typing test selections available.","To find out how fast you type, just start typing in the blank textbox on the right of the test prompt. You will see your progress, including errors on the left side as you type.","You can fix errors as you go, or correct them at the end with the help of the spell checker. If you need to restart the test, delete the text in the text box. Interactive feedback shows you your current wpm and accuracy.","In order to complete the test and share your results, you need to get 100% accuracy. You can review your progress for this session with the feedback chart. Just hover over a dot to see what your average speed and accruacy are for that key.","Our typing tests are ranked on level of difficulty. The algorithm to calculate difficulty depends on the average word length and how many special characters like capitals, numbers and symbols are included in the text."]
test1 = r.choice(test)
print("*****TYPING SPEED TEST*****")
print(test1)
print()
print("--------------------------------------------------------------------------------------------")
print()        
time1 = time()
userInput = input("enter text here:-")   
time2 = time()
print("speed:-",speed_time(time1, time2, userInput),"w/s")
print("error:-",mistake(test1, userInput))
