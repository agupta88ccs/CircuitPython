# Engineering Notebook

## LCD Button
### Description
The goal of this assignment was to use a MetroExpress board to wire up a LCD screen. The wire up a button to that. The code would display how many times the button was pressed on both the LCD screen and the Serial Monitor.    
### Wiring Diagram 
<img src="https://raw.githubusercontent.com/tweissm35/CircuitPython/master/media/lcdcount.jpg" width="400">

[Images Credit: Tim Weissman](https://github.com/tweissm35/CircuitPython)

### Lesson Learned 
Always check the wiring and LCD screen because sometimes the code isn't what is wrong it is something with the physical LCD screen. 


## Servo Touch 
### Description 
Coding a servo to turn back and forth when two wires connected to the breadboard are touched. When one is touched it turns 180 degrees in one direction and when the other is touched it turns 180 degrees back. In order to do this the code required having things such as "touchio" and "pulsio".    

### Wiring Diagram
<img src="https://raw.githubusercontent.com/tweissm35/CircuitPython/master/media/servo.jpg" width="400">

[Images Credit: Tim Weissman](https://github.com/tweissm35/CircuitPython)

### Lesson Learned
Figuring out how to do touchio was slightlty complicated other than that I was able to figuer out this pretty easily. All the wiring I already mainly knew how to do so that was helpful. 


## LED Fade
### Description
The goal of this assignment was to wire an LED to a metroExpress using a resistor. The code the LED to fade in and out (changing the brightness).  
### Wiring Diagram
<img src="https://github.com/tweissm35/CircuitPython/blob/master/media/fade.jpg" width="400">

[Images Credit: Tim Weissman](https://github.com/tweissm35/CircuitPython)

### Lesson Learned
This is the first CircuitPython assignment we did so learning the new coding language was the main difficulty when doing this. Having to write different statements to get the same thing was complicated. FOr example chaning "if" statements to "while true" statements was slightly confising at first. 

## Distance Sensor
### Description
The goal of this assignment was to code a distance sensor to determine the distance an object was from it and turn that into colors of the MetroExpress. The closer the object was to the sensor the closer the color got to red then as the object got farther it would change through the colors of the rainbow fading into eachother. 
### Wiring Diagram
<img src="https://github.com/tweissm35/CircuitPython/blob/master/media/ultrasonicsensor.jpg" width="400">

[Images Credit: Tim Weissman](https://github.com/tweissm35/CircuitPython)

### Lesson Learned
To me this code was really confusing to figure out. One of the main things was just trying to understand the code and all the values that controlled the colors. Since I was working off of someone elses code my main goal was just going through each step in the code to figure out what it was controlling and how the colors were working. 


## RBG Class
### Description
The goal of this assignment was to make a class to allow the preexisting code on canvas to work. This would allow for less code to be in the actual set run. This code allowed for two RBG LEDs to fade through all the colors of the rainbow. 
### Wiring Diagram 
<img src="https://github.com/tweissm35/CircuitPython/blob/master/media/rgb.jpg" width="400">

[Images Credit: Tim Weissman](https://github.com/tweissm35/CircuitPython)

### Lesson Learned
This assignment I did with Piper so between the two of us we were able to figure out the code. We had many spelling errors so figuring that out was complicated to figure out. Another thing was making sure that def_int_ was true and once we figured that out it went smoothly. The code we have is on her computer which is why I don't have this.


## Fancy LED
### Description
This assignment used the classes in the RBG assignment to create a new pattern with 6 LEDs. The four patterns they had to perform were alternate, chase, blink and sparkle. Using an already made class in canvas we used the VS code to help us code the actions the LEDs were to perform. 
### Wiring Diagram 
<img src="https://github.com/tweissm35/CircuitPython/blob/master/media/fancyLED.jpg" width="400">

[Images Credit: Tim Weissman](https://github.com/tweissm35/CircuitPython)

### Lesson Learned
I was able to understand the code and I was pretty sure it was working when a couple of my LEDs wouldn't light up. I realized that when rewiring my LEDs the pins weren't in the correct spot so two of the LEDS couldn't light up. After figuring that out it worked really smoothly. 


## Gearbox
### Description
The goal of this assignment was to make four gears that were configurations of eachother that then were put into a box form. They were all connected so that one was turned they all turned in sync.  
### Images
<img src="https://github.com/agupta88ccs/CircuitPython/blob/master/gearbox%20image.PNG" width="400">

### Lesson Learned
In this assignment I learned how to create a gear and how to use configurtions to change up the gear so you don't have to keep remaking the gear. At one point though my configurations were off and I realized that the number of teeth in the gear was all messed up. ALso making the walls of the box was complicated because when I first started I didn't realize how much easier it was to use relations. After that putting together the box was pretty simple. 

[Code Help](https://learn.adafruit.com/welcome-to-circuitpython/creating-and-editing-code)
