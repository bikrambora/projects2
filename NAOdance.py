'''
DO NOT REMOVE THIS HEADER


CODE AUTHOR: BIKRAM KAUSHIK BORA



'''

'''
THIS FILE CONTAINS PYTHON CODE FOR A DANCE FOR THE NAO ROBOT

MANUFACTURED BY ALDEBARAN ROBOTICS

https://www.aldebaran.com/en/humanoid-robot/nao-robot
______________________________________________________________________________________________________
This project uses the following basic syntax 


motionProxy  :  This object is used to call movement related functions

postureProxy :  This object is used to call whole body posture related functions

ttsProxy     :  This object is used to call speech related functions

_______________________________________________________________________________________________________
This project uses the following basic syntax for the moves

--->  list of MOTOR NAMES
--->  list of ANGLES
--->  list of TIMES

using these three lists the movements are performed.
_______________________________________________________________________________________________________
'''



#IMPORT ALL THE NECESSARY LIBRARIES
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages/naoqi')
from naoqi import ALProxy
import motion
import almath




#SET THE ROBOT IP
robotIP="128.250.231.68"

#LIST WHICH STORES THE BATTERY VALUES
battery_list=[]





#BEFORE STARTING WE INITIALISE THE 'MOTIONPROXY','POSTUREPROXY'
#AND 'TEXT TO SPEECH PROXY' OBJECTS
motionProxy  = ALProxy("ALMotion", robotIP, 9559)
postureProxy = ALProxy("ALRobotPosture", robotIP, 9559)
ttsProxy     = ALProxy("ALTextToSpeech", robotIP, 9559)

#isAbsolute variable is used wherever functions require a boolean argument
isAbsolute   = True






#WE USE CARTESIAN CONTROL ALSO
#We define the space and axis mask required for cartesian control of NAO
space      = motion.FRAME_ROBOT
axisMask   = almath.AXIS_MASK_ALL

#isAbsolute variable is used wherever functions require a boolean argument
isAbsolute = False





#THIS FUNCTION CHECKS THE BATTERY, PRINTS WARNING IF BATTERY IS LOW
#AND APPENDS BATTERY LEVEL TO A LIST
def battery_check():
    memory = ALProxy("ALMemory", robotIP, 9559)
    key = "Device/SubDeviceList/Battery/Charge/Sensor/Value"
    battery =memory.getData(key)
    battery_list.append(battery)
    print(battery)
    if battery < 0.1:
        print ("WARNING! BATTERY LOW")





#THIS FUNCTION CALCULATES THE AVERAGE BATTERY USED PER MOVE
def battery_avg():

    battery_sum=0
    battery_avg=0

    for i in range(0,len(battery_list)-1):
        battery_sum=battery_list[i]-battery_list[i+1]

    battery_avg=float(battery_sum)/(len(battery_list)-1)

    print "Average battery used per move : "+str(battery_avg)





#DANCE MOVE 1 FUNCTION DEFINITION
def move1():

    names      = ["RHipRoll","LHipRoll", "LKneePitch"
                  , "LAnklePitch", "LHipPitch"]
    angleLists = [[0.2] ,[0.2]  ,[1]   ,[-0.5],[-0.5]]
    times      = [[1.0] ,[ 1.0] ,[1.0] ,[1.0] , [1.0]]
    isAbsolute = True
    motionProxy.angleInterpolation(names, angleLists, times, isAbsolute)

    names      = ["RShoulderRoll" ,"RHand","HeadYaw","LWristYaw"]
    angleLists = [[-1.5],[1,0,1,0]        ,[1.5] ,[-1.0]]
    times      = [[2.0] ,[0.5,1.0,1.5,2.0],[2.0] ,[1.0] ]
    isAbsolute = True
    motionProxy.angleInterpolation(names, angleLists, times, isAbsolute)






#DANCE MOVE 2 FUNCTION DEFINITION
def move2():    

    names      = ["RHipRoll","LHipRoll" ,"LKneePitch"
                  ,"LAnklePitch" ,"LHipPitch"]
    angleLists = [[0],[0],[0],[0],[0]]
    times      = [[1.0],[ 1.0],[1.0],[1.0],[1.0]]
    isAbsolute = True
    motionProxy.angleInterpolation(names, angleLists, times, isAbsolute)


    motors  = ["RElbowRoll" ,"LElbowRoll","LShoulderRoll" ,"RShoulderPitch"
               ,"RHand", "LHand", "HeadYaw" ]
    angles  = [[0.5],[-0.5] ,[0.8],[-1] ,[1.0]  ,[1.0] , [0.7,0.7] ]
    times   = [[0.5],[0.5]  ,[0.5],[0.5],[0.5]  ,[0.5] , [0.5,1.0] ]
    motionProxy.angleInterpolation(motors, angles, times,isAbsolute)


    motors  = ["RElbowRoll","LElbowRoll","RShoulderRoll" ,"LShoulderPitch"
               ,"RHand", "LHand", "HeadYaw"   ]
    angles  = [[-0.5],[0.5] ,[-0.8] ,[1]    ,[1.0]  ,[1.0] , [-0.7,-0.7] ]
    times   = [[0.5] ,[0.5] ,[0.5]  ,[0.5]  ,[0.5]  ,[0.5] , [0.5,1]     ]
    motionProxy.angleInterpolation(motors, angles, times,isAbsolute)


    motors  = ["RElbowRoll","LElbowRoll","RShoulderPitch","LShoulderPitch"
               ,"RHand" ,"LHand" , "HeadYaw" ]
    angles  = [[0]  ,[0]    ,[-1]   ,[-1]   ,[-1.0]  ,[-1.0]  , [0] ]
    times   = [[0.3],[0.3]  ,[0.3]  ,[0.3]  ,[0.3]   ,[0.3]   , [0.3]]
    motionProxy.angleInterpolation(motors, angles, times,isAbsolute)







#DANCE MOVE 3 FUNCTION DEFINITION
def move3():

    
    Head_motors       = ["HeadPitch","HeadYaw"    ]
    Head_angles       = [[0.5,-0.5,0.5,-0.5,0.5,-0.5,0.5,-0.5,0.5,-0.5]
                         ,[1.0, -1.0]  ]
    Head_times        = [[0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0 ]
                         ,[ 2.5, 5.0]  ]
 
    UpperBody_motors  = ["RElbowRoll" ,"LElbowRoll"
                         ,"LShoulderPitch"  ,"RShoulderPitch"   ]
    UpperBody_angles  = [[0.5],[-0.5],[0.8, -0.8, 0.0, -0.8, 0.8]
                         ,[-0.8, 0.8, 0.0, 0.8, -0.8] ]
    UpperBody_times   = [[1.0],[1.0] ,[1.0,  2.0, 3.0,  4.0, 5.0]
                         ,[ 1.0, 2.0, 3.0, 4.0,  5.0] ]

        
    LowerBody_motors  = ["LKneePitch","RKneePitch","RAnklePitch","LAnklePitch"
                         ,"RHipPitch","LHipPitch"]
    LowerBody_angles  = [[1,0]  ,[1,0]  ,[-0.5,0] ,[-0.5,0]
                         ,[-0.5,0]   ,[-0.5,0]]
    LowerBody_times   = [[3,5]  ,[3,5]  ,[3,5]    ,[3,5]
                         ,[3,5]      ,[3,5]  ]

    #The motornames_names list has the various MOTOR_NAMES which are used
    #The angles list has the respective MOTOR_ANGLES which are used
    #The times list has the recpective TIMEs at which
    #the motor holds a particular angle value

    motor_names       = Head_motors + UpperBody_motors + LowerBody_motors
    times             = Head_times  + UpperBody_times  + LowerBody_times
    angles            = Head_angles + UpperBody_angles + LowerBody_angles
    isAbsolute = True

     
    motionProxy.angleInterpolation(motor_names, angles, times, isAbsolute)

    names =      ["RHand","RShoulderPitch"]
    angleLists = [[1.0],[-1.0]]
    times      = [[0.5],[0.5]] 
    motionProxy.angleInterpolation(names, angleLists, times, isAbsolute)



    #SET NAO TO INITIAL POSE
    postureProxy.goToPosture("StandInit", 0.5)





#DANCE MOVE 4 FUNCTION DEFINITION
def move4():    

    #LOWER THE TORSO AND MOVE FROM SIDE TO SIDE
    effector   = "Torso"
    path       = [0.0, -0.07, -0.03, 0.0, 0.0, 0.0]
    time       = 1.5                
    motionProxy.positionInterpolation(effector, space, path,axisMask
                                      , time, isAbsolute)

    effector   = "Torso"
    path       = [0.0, 0.07, 0.03, 0.0, 0.0, 0.0]
    time       = 1.5                
    motionProxy.positionInterpolation(effector, space, path,axisMask
                                      , time, isAbsolute)

    effector   = "Torso"
    path       = [0.0, 0.07, -0.03, 0.0, 0.0, 0.0]
    time       = 1.5                
    motionProxy.positionInterpolation(effector, space, path,axisMask
                                      , time, isAbsolute)


#DANCE MOVE 5 FUNCTION DEFINITION
def move5():
        
    Head_motors       = ["HeadPitch" ,"HeadYaw"    ]
    Head_angles       = [[0.5 ]      ,[1.0, -1.0]  ]
    Head_times        = [[0.5 ]      ,[ 2.5, 5.0]  ]

    UpperBody_motors  = ["RElbowRoll"   ,"LElbowRoll"
                         ,"LShoulderPitch"  ,"RShoulderPitch"]
    UpperBody_angles  = [[0.5]  ,[-0.5] ,[0.8,  0.8, 0.8,  0.8, 0]
                         ,[-0.8, -0.8, -0.8, -0.8,  0 ] ]
    UpperBody_times   = [[1.0]  ,[1.0]  ,[1.0,  2.0, 3.0,  4.0, 5.0]
                         ,[ 1.0, 2.0, 3.0, 4.0,  5.0] ]
  
    #The motornames_names list has the various MOTOR_NAMES which are used
    #The angles list has the respective MOTOR_ANGLES which are used
    #The times list has the recpective TIMEs at which
    #the motor holds a particular angle value

    motor_names       = UpperBody_motors + Head_motors
    times             = UpperBody_times  + Head_times
    angles            = UpperBody_angles + Head_angles

    isAbsolute = True
    motionProxy.angleInterpolation(motor_names, angles, times, isAbsolute)





#THIS IS THE DEFINITION OF THE MAIN FUNCTION
def main(robotIP):    
    
    #BATTERY CHECK BEFORE STARTING
    battery_check()

    #ROBOT SPEAKS OUT MESSAGE
    ttsProxy.say("I LIKE TO MOVE IT MOVE IT!")

    #WE SET THE MOTOR STIFFNESS TO 1 AND BRING NAO
    #TO INITIAL POSTURE BEFORE START OF DANCE
    motionProxy.setStiffnesses("Body", 1.0)
    postureProxy.goToPosture("StandZero", 0.5)


    #ALL THE DANCE MOVE FUNCTIONS ARE CALLED ONE BY ONE
    move1()
    battery_check()
    
    move2()
    battery_check()

    move3()    
    battery_check()

    move4()
    battery_check()

    move5()
    battery_check()

    #BATTERY AVERAGE FUNCTION IS CALLED
    battery_avg()


    #SET NAO TO INITIAL POSE
    postureProxy.goToPosture("StandInit", 0.5)

    #ROBOT SPEAKS OUT MESSAGE
    ttsProxy.say("THANK YOU!")

    #WE SET THE MOTOR STIFFNESS TO 0 AT THE END OF DANCE
    motionProxy.setStiffnesses("Body", 0.0)
    



#CALL TO THE MAIN FUNCTION WHICH BEGINS THE DANCE
#BY CALLING ALL THE OTHER FUNCTIONS    
main(robotIP)


​