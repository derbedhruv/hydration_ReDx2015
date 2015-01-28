/* ###########################################################
  Extracting DC from a signal and then throwing the DC component out via PWM.
  The PWM is smoothed using an RC filter and then put through a difference amplifier with the original signal
  THis difference is then sent through analog A3 

  This exercise is one part of building a pulse oximeter, with the LED brightness once again being controlled
  by PWM (on pin 11, one more LED will need to be added later).
  
  Interrupt timer used to implement digital DC filter, taken from
  http://www.instructables.com/id/Arduino-Timer-Interrupts/
########################################################### */

#define LED_850 11
#define LED_1300 5
#define DCout 3

#define timer_frequency 200 // the timer shall count at this speed.
#define sampling_freq 200    // Fsampl in Hz

// intensity of the LEDs
#define intensity_850 5
#define intensity_1300 1

boolean first = true;

int sampling_time = (double)timer_frequency/(double)sampling_freq;  // the time for which one sample (one wavelength) will be taken

int counter = 0;  // this counts incrementally to 200 at every 0.005s to keep track of things
float filtered_value_850 = 512, last_filtered_value_850;  // giving a better initialization value to the filter
float filtered_value_1300 = 512, last_filtered_value_1300;  // giving a better initialization value to the filter
int value, last_value;
String outdata;
float DC_gain = 1.05;  // the gain given to calibrate the DC in the output

// set the voltages you want to output for the two LEDs (these will be RC-filtered eventually)
// int intensity_850 = 50, intensity_1300 = 10;

void setup(){
  Serial.begin(115200);    // superfast serial communication
  
  int match_register = 16000000/(1024*timer_frequency) - 1; // match register to match that sampling frequency
  
  // STEP 1: we create an interrupt timer at the sampling frequency
  cli();//stop interrupts

  TCCR1A = 0;// set entire TCCR1A register to 0
  TCCR1B = 0;// same for TCCR1B
  TCNT1  = 0;//initialize counter value to 0
  // set compare match register for 1hz increments
  OCR1A = match_register; // HERE'S WHERE IT'S SET
  // turn on CTC mode
  TCCR1B |= (1 << WGM12);
  // Set CS10 and CS12 bits for 1024 prescaler
  TCCR1B |= (1 << CS12) | (1 << CS10);  
  // enable timer compare interrupt
  TIMSK1 |= (1 << OCIE1A);

  sei();//allow interrupts

  // STEP 2 : Set PWM frequency for pin 11 (which will control LED brightness via RC smoothing of the pwm signal) and pin 3 (which will control the DC output)
  // using pin 11 since it is controlled by Timer2 (we;re using Timer1 for the interrupt)
  // first we'll change the frequency of the PWM to suit our needs...
  // ref: http://playground.arduino.cc/Main/TimerPWMCheatsheet
  TCCR2B = TCCR2B & 0b11111000 | 0x01;  // 31372.55 Hz
 
  // We will also set the pwm frequency of pins 9 and 10 to the same frequency (to control the other LED)..
  // HOLY CRAP this is for timer1, which we're using for the timerinterrupt 
  // TCCR1B = TCCR1B & 0b11111000 | 0x01;  // 31372.55 Hz
  
  // Hence we'll use the remaining pins 5 and 6 which rely on Timer3
  TCCR0B = TCCR0B & 0b11111000 | 0x01;

  // STEP 3 : Give the output pwm value in the range (0, 255) mapped to (0, 5)V
  pinMode(LED_850, OUTPUT);
  pinMode(LED_1300, OUTPUT);
  
  // int voltage_ir = 736;
  
  // pin 8 is the common "anode" for the LEDs, it will be permanently set to high
  pinMode(8, OUTPUT);
  digitalWrite(8, HIGH);
  
  // Set the PWM frequencies of the LED pins
  // analogWrite(redLED, 256*(1 - (voltage_red + 1)/1024));
  // analogWrite(redLED, intensity_850);
  // analogWrite(irLED, intensity_1300);
  
  counter = 0;
}

ISR(TIMER1_COMPA_vect){   //  timer1 interrupt 1kHz
   // increment the counter
   counter++;
   // Using the timer interrupt, we shall be making this work...
  
}

void loop(){
  
  // First we handle the 850nm..
   if (first == true) {
     
     // update variables...
     last_filtered_value_850 = filtered_value_850;
  
     // will simply read A0 and then filter it
     value = analogRead(A0);
     // Serial.println(value);
     analogWrite(LED_1300, intensity_1300);
     analogWrite(LED_850, 255);
     
     // filter out PPG frequencies and only have the DC part
     filtered_value_850 = last_filtered_value_850 + 0.004*(value - last_filtered_value_850);
        
     // the filtered value is now send out through PWM pin D3, which is also controlled by Timer2
     // filtered_value is in the range (0,1023) and the analogWrite value needs to be in the range (0, 255).
     // Hence we convert..
     analogWrite(DCout, int(DC_gain*256*(filtered_value_850 + 1)/1024) - 1);
     
     // Then we read the value in again from an isolated analog pin and print it out..
     outdata = String(analogRead(A3)) + "," + String(int((filtered_value_850))) + ",";
     Serial.print(outdata);
     
     first = false;
     delay(20);
     
  } else{
     
     // update variables...
     last_filtered_value_1300 = filtered_value_1300;
  
     // will simply read A0 and then filter it
     value = analogRead(A0);
     // Serial.println(value);
     analogWrite(LED_850, intensity_850);
     
     // filter out PPG frequencies and only have the DC part
     filtered_value_1300 = last_filtered_value_1300 + 0.004*(value - last_filtered_value_1300);
     analogWrite(LED_1300, 255);
             
     // the filtered value is now send out through PWM pin D3, which is also controlled by Timer2
     // filtered_value is in the range (0,1023) and the analogWrite value needs to be in the range (0, 255).
     // Hence we convert..
     analogWrite(DCout, int(DC_gain*256*(filtered_value_1300 + 1)/1024) - 1);
     
     // Then we read the value in again from an isolated analog pin and print it out..
     outdata = String(analogRead(A3)) + "," + String(int((filtered_value_1300)));
     Serial.println(outdata);
     
     // reset the counter
     counter = 0;
     
     first = true;
     
     delay(20);
  }
  
  /*
  // Using the timer interrupt, we shall be making this work...
  // First we handle the 850nm..
   if (counter < sampling_time) {
     analogWrite(LED_850, intensity_850);
     // update variables...
     last_filtered_value = filtered_value;
  
     // will simply read A0 and then filter it
     value = analogRead(A0);
     // Serial.println(value);
     analogWrite(LED_850, 255);
     
     // filter out PPG frequencies and only have the DC part
     filtered_value = last_filtered_value + 0.004*(value - last_filtered_value);
        
     // the filtered value is now send out through PWM pin D3, which is also controlled by Timer2
     // filtered_value is in the range (0,1023) and the analogWrite value needs to be in the range (0, 255).
     // Hence we convert..
     analogWrite(DCout, int(DC_gain*256*(filtered_value + 1)/1024) - 1);
     
     // Then we read the value in again from an isolated analog pin and print it out..
     outdata = String(analogRead(A3)) + "," + String(int((filtered_value)));
     Serial.print(outdata);
     
  } else if (counter > sampling_time) {
     analogWrite(LED_1300, intensity_1300);
     // update variables...
     last_filtered_value = filtered_value;
  
     // will simply read A0 and then filter it
     value = analogRead(A0);
     // Serial.println(value);
     
     // filter out PPG frequencies and only have the DC part
     filtered_value = last_filtered_value + 0.004*(value - last_filtered_value);
     analogWrite(LED_1300, 255);
        
     // the filtered value is now send out through PWM pin D3, which is also controlled by Timer2
     // filtered_value is in the range (0,1023) and the analogWrite value needs to be in the range (0, 255).
     // Hence we convert..
     analogWrite(DCout, int(DC_gain*256*(filtered_value + 1)/1024) - 1);
     
     // Then we read the value in again from an isolated analog pin and print it out..
     outdata = String(analogRead(A3)) + "," + String(int((filtered_value)));
     Serial.println(outdata);
     
     // reset the counter
     counter = 0;
  }
  */
}
