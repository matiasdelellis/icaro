#define __USB__
#include <stdlib.h>
#include <string.h>
#ifdef __USB__
#include "../tmp/usb.h"
#include <usb.c>
#endif
#ifndef __USB__
void epap_in() { return; }
void epap_out() { return; }
void epapin_init() { return; }
void epapout_init() { return; }
#endif
uchar caracter;

void servos()
{
int val=0;
caracter=usbread();
	switch(caracter) 
	{
	case '1':  
		val=10;
		break;
	case '2':
		val=11;  
		break;
	case '3':
		val=12;  
		break;
	case '4':
		val=8;  
		break;
	case '5': 
		val=9; 
		break;
	default:
		usbsend("error", 5);
		break;

	}
Delayms(10);	
caracter=' ';
caracter=usbread();
ServoWrite(val,caracter);
return;
}


void setup()
{
    TRISB=0;
    pinmode(15,INPUT);
    pinmode(21,INPUT);
    pinmode(22,INPUT);
    pinmode(23,INPUT);
    pinmode(24,INPUT);
    pinmode(25,OUTPUT);
    pinmode(26,OUTPUT);
    pinmode(27,OUTPUT);
    pinmode(28,OUTPUT);
    ServoAttach(10);
    ServoAttach(11);
    ServoAttach(12);
    ServoAttach(8);
    ServoAttach(9);
}
void loop()
{

if (usbavailable())
{
caracter=usbread();
	switch(caracter) 
	{
	case 'b':  
		usbsend("icaro", 5);
		break;
	case 'm':  
		servos();
		break;
	default:
		usbsend("error", 5);
		break;

	}
  Delayms(10);	
caracter=' ';
}

}
