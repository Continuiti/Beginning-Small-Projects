#pragma config(Sensor, in1,    lineFollower,   sensorLineFollower)
#pragma config(Sensor, in2,    potentiometer,  sensorPotentiometer)
#pragma config(Sensor, in3,    lightSensor,    sensorReflection)
#pragma config(Sensor, dgtl1,  limitSwitch,    sensorTouch)
#pragma config(Sensor, dgtl2,  bumpSwitch,     sensorTouch)
#pragma config(Sensor, dgtl3,  quad,           sensorQuadEncoder)
#pragma config(Sensor, dgtl8,  sonar,               sensorSONAR_inch)
#pragma config(Sensor, dgtl12, green,          sensorLEDtoVCC)
#pragma config(Motor,  port1,           flashlight,    tmotorVexFlashlight, openLoop, reversed)
#pragma config(Motor,  port2,           rightMotor,    tmotorVex393_MC29, openLoop)
#pragma config(Motor,  port3,           leftMotor,     tmotorVex393_MC29, openLoop)
#pragma config(Motor,  port9,           servoMotor,    tmotorServoStandard, openLoop)
//*!!Code automatically generated by 'ROBOTC' configuration wizard               !!*//

/*
Project Title: VEX Robotic
Team Members: Thien Tran, Kobe Chauvin
Date: 4-3-17
Section: The Banana


Task Description:
Limit Switch turns on Light Sensor for as long as it's pressed. Turn on the flashlight when the Light Sensor "senses" the dark.


Pseudocode:

Check If Limit Switch On > If Condition Met, Check Value of Light Sensor > If Sensor Value Over 700, Turn On
*/

task main()
{
while (true)// Repeat Indefinitely
	{
while (SensorValue(limitswitch) == 1) //Repeat While LimitSwitch Pressed
{
	if (SensorValue(lightsensor) > 700) //Respond To Lightsensor
{turnFlashlightOn(flashlight, 127)}
	else{turnFlashLightOff(flashlight)}
}
}
}
