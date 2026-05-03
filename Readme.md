 ## Project Overview
 This project explores behaviour of Reaction wheel stabilization robot(RWSR), its an underactuated system that maintains stability using internal angular momentum.
 The goal of the project is not only to achieve balance but also to understanding the limitations when actuator reaches its physical limit.

 ## MOtivation of my research
 The goal of my research is to study how stability can be maintained in underactuated RWSR underactuator constraints with particular focus on actuator saturation 

 Actuator saturation occurs when the wheel reaches its maximum rotational speed limiting its ability to generate additional corrective torque.This creates a boundary beyond which robot can no longer recover from disturbances.

 ## System Description
 The system consists of:-
 1.A rigid body 
 2.An internal reaction wheel 
 3.A rotational joint connecting the system
 # How this works:
 By accelearting the reaction wheel an equal and opposite torque is applied to the robot body and corrects its tilt theta and mintain its balance.

 ## Control system
  A PID controller is used to maintain the tilt of the robot
     Propotional(P): reacts to current tilt error  
     Integral(I): remembers the past errors 
     Derivative(D): predicts motion and reduces oscillation 
  This controller generates torque commands that drive the reaction wheel

 ## Saturation Behaviour
 The system has two distinct operating regions:
 Stable Region:
  For small tilt angles the controller successfully stabilizes the robot 

 Saturation Region:
  When tilt exceeds a cretain threshold the reaction wheel reaches its maximum speed(MAX_RPM).
  At this point the actuators cannot provide additional torque and the system looses stability.
 This shows a fundamental limitation imposed by actuator constraints in underactuated systems

 ## Simulations Results
 Simulations were conducted to analyze the behaviour of the RWSR under different initial conditions using a Python-based dynamic model 
 
 The results show that:
  The system stabilizes for small initial tilt angles 
  The controller reduces oscillations over time 
  In cretain conditions the actuator approaches its speed limit indicating potential saturation behaviour
 These simulations provide insight into how actuator limits affect system stability

 (Note: This study is currently limited to simulation and doesnt include hardware validation)

 ## Repository Structure
 /scripts includes  original simultion code
 /Data includes failure and successfull simulation images "Scientific proofs"
 /Docs includes documentation and error simulation code and About_docs.md

 ## Future Work
 Further improvements will focus on state-space control system to better model system dynamics

 By considering the full system stae-space control system  may help manage actuator limits more effectively and delay or prevent saturations

 ## Conclusion
 This project highlights that achieving balance is only part of the problem in control systems.
 Understanding actuator limits and their impact on system stability is essential for designing reliable robotic systems.