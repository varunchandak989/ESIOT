import RPi.GPIO as GPIO 
import time

BUTTON_ZERO = 29
BUTTON_ONE = 31
BUTTON_TWO = 32
BUTTON_THREE = 33

PRESS_ZERO = 35
PRESS_ONE = 36
PRESS_TWO = 37
PRESS_THREE = 38

#GPIO setup for the LEDs
LED_ZERO = 10
LED_ONE = 11
LED_TWO = 12
LED_THREE= 13

#GPIO setup for the Seven Segment Display
a=15
b=16
c=18
d=19
e=21
f=22
g=23


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


GPIO.setup(BUTTON_ZERO, GPIO.IN)
GPIO.setup(BUTTON_ONE, GPIO.IN)
GPIO.setup(BUTTON_TWO, GPIO.IN)
GPIO.setup(BUTTON_THREE, GPIO.IN)

GPIO.setup(PRESS_ZERO, GPIO.IN)
GPIO.setup(PRESS_ONE, GPIO.IN)
GPIO.setup(PRESS_TWO, GPIO.IN)
GPIO.setup(PRESS_THREE, GPIO.IN)



GPIO.setup(LED_ZERO, GPIO.OUT) #Floor 1
GPIO.setup(LED_ONE, GPIO.OUT) #Floor 2
GPIO.setup(LED_TWO, GPIO.OUT) #Floor 3
GPIO.setup(LED_THREE, GPIO.OUT) #Floor 4



GPIO.setup(a, GPIO.OUT) 
GPIO.setup(b, GPIO.OUT) 
GPIO.setup(c, GPIO.OUT) 
GPIO.setup(d, GPIO.OUT) 
GPIO.setup(e, GPIO.OUT) 
GPIO.setup(f, GPIO.OUT) 
GPIO.setup(g, GPIO.OUT) 

digitclr=[0,0,0,0,0,0,0]
digit0=[1,1,1,1,1,1,0]
digit1=[0,1,1,0,0,0,0]
digit2=[1,1,0,1,1,0,1]
digit3=[1,1,1,1,0,0,1]


gpin=[15,16,18,19,21,22,23]
#routine to clear and then write to display
def digdisp(digit):
    for x in range (0,7):
        GPIO.output(gpin[x], digitclr[x])

    for x in range (0,7):
        GPIO.output(gpin[x], digit[x])

        
while True:
    
        
    if (GPIO.input(BUTTON_ZERO)== True) :
        GPIO.output(LED_ZERO,1)
            
        print"0"
            
        digdisp(digit0)
        time.sleep(1)   
        GPIO.output(LED_ZERO,0)
        time.sleep(3)
        
        while True:
            if(GPIO.input(PRESS_ONE)== True):
                print'floor ONE'
                digdisp(digit0)
                time.sleep(1)
                digdisp(digit1)
                time.sleep(2)
                break
                
                
            elif (GPIO.input(PRESS_TWO)== True):

                print'floor TWO'
                digdisp(digit0)
                time.sleep(1)
                digdisp(digit1)
                time.sleep(1)
                digdisp(digit2)
                time.sleep(2)
                break
               
                
            elif (GPIO.input(PRESS_THREE)== True):

                print'floor THREE'
                digdisp(digit0)
                time.sleep(1)
                digdisp(digit1)
                time.sleep(1)
                digdisp(digit2)
                time.sleep(1)
                digdisp(digit3)
                time.sleep(2)

                break
                
                

    elif (GPIO.input(BUTTON_ONE) == True):
        
            
        GPIO.output(LED_ONE, 1)
        print"1"

        digdisp(digit0)
        time.sleep(1)
        digdisp(digit1)
        time.sleep(1)
        time.sleep(4)

        GPIO.output(LED_ONE, 0)

        while True:
            if(GPIO.input(PRESS_ZERO)== True):
                print 'floor ZERO'
                digdisp(digit0)
                time.sleep(2)
                break
                
            elif (GPIO.input(PRESS_TWO)== True):
                print'floor TWO'
                digdisp(digit2)
                time.sleep(2)
                break

                    
            elif (GPIO.input(PRESS_THREE)== True):
                print'floor THREE'
                digdisp(digit2)
                time.sleep(1)
                digdisp(digit3)
                time.sleep(2)
                break
 
               


            
    elif (GPIO.input(BUTTON_TWO) == True):

        GPIO.output(LED_TWO, 1)
            
        print"2"

        digdisp(digit0)
        time.sleep(1)
        digdisp(digit1)
        time.sleep(1)
        digdisp(digit2)
        time.sleep(1)
        time.sleep(5)
        GPIO.output(LED_TWO, 0)
            
        while True:
            if(GPIO.input(PRESS_ZERO)== True):
                print 'floor ZERO'
                digdisp(digit1)
                time.sleep(1)
                digdisp(digit0)
                time.sleep(2)
                break
                
            elif (GPIO.input(PRESS_ONE)== True):
                print 'floor ONE'
                digdisp(digit1)
                time.sleep(2)
                break
                
            elif (GPIO.input(PRESS_THREE)== True):

                print'floor THREE'
                digdisp(digit3)
                time.sleep(2)
                break
                
            
    elif (GPIO.input(BUTTON_THREE) == True):

        GPIO.output(LED_THREE, 1)

        print"3"
        digdisp(digit0)
        time.sleep(1)
        digdisp(digit1)
        time.sleep(1)
        digdisp(digit2)
        time.sleep(1)
        digdisp(digit3)
        time.sleep(6)

        GPIO.output(LED_THREE, 0)

        while True:
            if (GPIO.input(PRESS_ZERO)== True):
                print 'floor ZERO'
                digdisp(digit2)
                time.sleep(1)
                digdisp(digit1)
                time.sleep(1)
                digdisp(digit0)
                time.sleep(2)
                break
                
            elif (GPIO.input(PRESS_ONE)== True):

                print 'Floor ONE'
                digdisp(digit2)
                time.sleep(1)
                digdisp(digit1)
                time.sleep(2)
                break
                
            elif (GPIO.input(PRESS_TWO)== True):

                print'floor TWO'                
                digdisp(digit2)
                time.sleep(2)
                break
                
                

    else:
####        time.sleep(3)
       # digdisp(digit0)
        GPIO.output(LED_ZERO, 0)
        GPIO.output(LED_ONE, 0) 
        GPIO.output(LED_TWO, 0)
        GPIO.output(LED_THREE, 0)



    
            
