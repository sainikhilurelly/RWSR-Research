## Why I created this document
This document explains how I achieved a stabilized 2D simulation of my robot, the problems I faced, and how I solved them.

## Simulation code error
This was the first problem I faced. To be honest, I am not very familiar with Python.
Initially, whatever values I used, I kept getting incorrect (negative) results. After carefully checking the simulation code, I found a small mistake: a missing “-” sign in the torque formula.
Because of this, the system behaved incorrectly. After fixing it, the simulation started giving expected outputs.

## Successful stabilization
After fixing the error, I tested with random values, but the robot was not stable as expected.
Then I tried to understand PID tuning better and experimented with different values.
Finally, with:
θ = 0.05
Kp = 15.0
Ki = 0.0
Kd = 2.0
RPM = 300
I achieved a stable simulation.
I also tested other values, but this combination gave the best result. This version significantly reduced the shaking of the robot.

## Failures
Before understanding PID properly, I made several mistakes.
For example, when I tried to make the robot stand up by itself, it started shaking violently back and forth. This happened because I had not included the derivative term (Kd).
After adding Kd, the system became much more stable.

## What I learned
I learned how to tune a PID controller for stabilizing an underactuated robot.
I used a trial-and-error approach, changing one parameter at a time. This helped me understand:
how each parameter affects the system
what kind of behavior each term introduces

## Important mathematical formulas
PID control equation:-
u(t) = Kpe(t)+ Ki∫e(t)dt+ Kd dt/de(t)

Simple explanation:
P (Proportional): reacts to current error
I (Integral): accumulates past error and removes steady offset
D (Derivative): reacts to rate of change and reduces oscillation

Error definition:

 e(t) = θtarget − θactual
	​

 

