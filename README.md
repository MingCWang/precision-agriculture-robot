# precision-agriculture-robot

This research project focuses on the development of an autonomous Turtlebot platform equipped with a precision water-dispensing system.

## Usage
### onboard (rasberry pi)
```
bringup; relaysub
```
### real:mutant (local machine) 
```
roslaunch fiducial_nav fiducials_real.launch
python sprayer_publisher.py 
```
### start server /backend
```
python app.py
```

### web interface
navigate to http://172.20.111.126:6969/

## Demo


<div align="center">
  <video src="https://github.com/user-attachments/assets/0e36eb6e-2e52-41ca-af7e-78529c9f4e37" width="400" />
</div>
    
<p align="center">
  <img width="300" alt="demo3" src="https://github.com/user-attachments/assets/bd5a2794-b8d1-4892-9d10-2752df16b9b1">
</p>

## Links
FAQ: 
- [AI Detector](https://github.com/campusrover/labnotebook2/blob/main/docs/faq/ai/AI_Detector.md)
- [External Actuator Control With ROS Publisher](https://github.com/campusrover/labnotebook2/blob/main/docs/faq/hardware/external_actuator_control.md)

Video:
https://brandeis.zoom.us/rec/share/L7KHHXQx5YMipCGCVavkNSaTUPy47De38HoTem0eBAwPRykOmei3kHTvwU6wjcf-.MogkEBxoQQngRBTE?startTime=1734127778000

[Full Report](https://github.com/campusrover/labnotebook2/blob/main/docs/reports/2024/AgriculturalRobot.md)
