from gpiozero import LED, Button
from time import sleep
import csv


led_green = LED(2)
led_red = LED(4)
button_left = Button(14)
button_right = Button(15)
csvcode = 0000



def toggle_led_green(channel):#Function to startup alarm
    global toggle, on
    blink1 = int(blink_in_csv()[0])
    if on == 0:
    	led_green.on()
    	sleep(2)
    	led_green.blink(1,1, blink1)
    	sleep(blink1)
    	led_green.on()
    	toggle = 1
    	on = 1

    elif on == 1:
        print('try')
        led_green.off()
        toggle = 0
        on = 0

def alarm_trigger(channel):#Function to simulate anti-theft
    global trigger, toggle
    blink2 = int(blink_in_csv()[1])
    if trigger == 0:
        csvcode = input('Voer code in: ')
        led_red.blink(1,1,blink2)
        sleep(blink2)
        code = code_in_csv()
        check = check_code(code, csvcode)
        if check == 1:
            led_red.off()
            toggle = 0
            trigger = 0
        else:
            led_red.on()
            toggle = 1
            trigger = 1
    else:
        print('nope')
        trigger = 0
    
def check_code(inputcode, csvcode):#Function to check if code is filled in .csv file
        new = int(code_in_csv()[0][0])
        if new == csvcode:
                return 1
        else:
                return 0

def code_in_csv():#Function to read pin code from pincode.csv
    lst = []
    with(open('pincode.csv','r')) as file:
        read = csv.reader(file)
        for word in read:
            lst.append(word)
        return lst
    
def blink_in_csv():#Function to read blink timer from blink.csv
    blinklst = []
    with(open('blink.csv','r')) as file:
        with(open('blink2.csv','r')) as file2:
            for word in file:
                blinklst.append(word)
            for word in file2:
                blinklst.append(word)
        return blinklst

on = 0    
toggle = 0
trigger = 1
def alarm_loop():#Function to loop alarm
    while 1:
        button_left.when_pressed = toggle_led_green
        if toggle == 1:
            button_right.when_pressed = alarm_trigger

alarm_loop()

