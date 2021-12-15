# Automated Number Plate Recognnition System using ROS

Project Name: plate_recog.  

Team Members:
- Vishal Natarajan, vnataraj@buffalo.edu
---

## Project Description
This project aims to make a turtlebot3(burger) get around a simulated parking lot and recognize plates from vehicles present in the lot.

### Contributions
Using Tesseract, the project aims to use OpenCV in conjunction with ROS to help a robot detect plates inside a world

---

## Installation Instructions

List of Prerequisite Software:
- Tesseract
- Gazebo

All installation instructions require you to use the terminal in Ubuntu

1. Install PiP 
sudo apt install python3-pip

2. Install Tesseract
sudo pip install pytesseract=0.3.5

3. Get the plate recognition files
a.clone files from repo

cd ~/catkin_ws/src
catkin_create_pkg plate_recog
cd plate_recog
mkdir scripts
cd ~/catkin_ws/src
git clone https://github.com/vnataraj117/ANPR_using_ROS.git
cp -R ~/catkin_ws/src/ANPR_using_ROS/plate_recog/* ~/catkin_ws/src/plate_recog

b.build workspace
cd ~/catkin_ws/
rm -r build
rm -r devel
catkin build

c.source workspace
echo 'source ~/catkin_ws/devel/setup.bash' >> ~/.bashrc

---

## Running the Code
1. Launch the robot in gazebo and RViz

source ~/catkin_ws/devel/setup.bash
roslaunch plate_recog turtlebot3_parking.launch

2. Run Python Node for plate recognition

source ~/catkin_ws/devel/setup.bash
roscd plate_recog/src
chmod +x plate_recog.py
rosrun plate_recog ros_plate_recog.py

---

## Measures of Success

<TABLE>
<TR>
	<TH>Number plate recognition code work</TH>
	<TH>100%</TH>
</TR>
<TR>
	<TD>Robot moves with an xbox controller</TD>
	<TD>0%(could'nt get anything to work at all)</TD>
</TR>
<TR>
	<TD>The robot can move and recognise plates</TD>
	<TD>50%(it can recognise plates but the burger's camera feed doesnt seem to be clear enough for it to detect plates)</TD>
</TR>
<TR>
    <TD>World is generated<TD>
    <TD>50%(i could generate a world with some screenshots of cars with plates but could'nt actually get real cars with plates to be generated)
 </TR>
 <TR>
    <TD>Robot moves around world and recognises plates</TD>
    <TD>25%(we need to move the robot from point to point)</TD>
   </TR>    
</TABLE>

---

## What did you learn from this project?

Managed to learn some amount of OpenCV and how to use python libraries properly from doing this project 

First time programming anything really and was really exciting to see the code actually recognise plates from cars

Gained enough confidence to try my luck at programming 
---

## Future Work

The biggest challenge with the project was getting the robot to move around and detect plates in Gazebo which I couldn't get working nor could I generate a world with actual vehicles in them 
---

## References/Resources

A lot of YouTube videos on using OpenCV and Tesseract and general internet research on how ANPR is done 


