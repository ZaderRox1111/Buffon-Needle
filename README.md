# Buffon-Needle
Approximating pi with the Buffon Needle algorithm.


Kyle Elison kje237@nau.edu
Zach Derrick zcd22@nau.edu
# The showMontePi Function
# Understanding the Problem
The goal of this lab is to implement the Monte Carlo simulation for finding an
approximation of pi. Then we will use a program simulating Buffon’s Needle
Algorithm to approximate pi.
## Constraints:
- Randomly drop the needles
- Needles can’t go higher than a unit above/below the lines
- Needles have to be in the simulation space
- Two lines parallel to each other, one unit apart
- Needles are one unit in length
- Needle needs to be colored if it hits, a different color if it misses
# Plan a Solution
Using the example page and after researching the buffon needle algorithm, we
found that if the distance from the center of the needle and the line is less than
or equal to half the sin of the angle of the needle, then it comes into contact with
the line.
- d = distance from line to center of the needle
- theta = angle of the needle’s turn from ‘east’
- d <= (½)math.sin(theta)
- We’re going to have to randomly create an x and y point within the boundary
constraints, as well as a theta, and determine if it crosses a line before we draw it.
If it does cross the line we will make it green, and if it misses it will be red. To draw
it, we need to move the turtle half a unit in the direction of theta, then one unit in
the direction of 180+theta. Then pick up the pen and move it to the next random
spot, put it down, and repeat the process.
# Implementing and Testing
To start out we began by looking at the variables we need to create, like the
counter and the turtle and the ‘unit’. Then we started building the for loop,
making the randomized x, y, and angle variables. We then started thinking
through and implementing the if/else statement to increase the counter and
check if the distance is less than ½ the sin of the angle.
After the if statements and checking the distance between the lines, we needed to
draw the turtle. We placed him at x and y, turned him towards the angle, moved
forward half a unit, then backwards a full unit, and pick him up again.
Rinse and repeat until you run out of darts, then take the total drops multiplied
by 2 and divide it by the amount of needles that hit the line.
We ran into a few errors along the way, such as we needed to make the angle in
radians so that the sine function would take it. We also forgot to bring the turtle
up when we drew the needles, so it was a bunch of lines. The lines were also not
counting when they crossed the bottom line, and they also counted when they
were much higher than the top line. We fixed the issue with the top line by adding
an absolute value to the distance, and dividing the whole distance equation by a
unit. To fix the not counting the bottom part we created an if statement to check
which line it was closer to, and take the distance from the closest line.
# Reflect and Refactor
Our solution ended up working nicely, however there are a few things we could
do to make it smoother and faster. We could have commented our code a little
bit better to make it easier to go over afterward. We also could have found a way
to display the estimate of pi on the turtle screen so that we don’t have to close it
to see the estimate, and we could have even found a way to have the estimate
update with every needle that drops. We also could have tried to add a way to
drop in extra needles from the turtle box or been able to change the amount of
needles dropped using something like a raw input without going in and editing
the code.
The largest problem we came across was finding how to check what line the
needle was closest to, and solving that took some extra thinking and going over
Nakai’s tips and guidance section, alongside bouncing ideas off of each other. To
better solve them in the future, we could make sure to read and comprehend the
tips and the full lab description.
