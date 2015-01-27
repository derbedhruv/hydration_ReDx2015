/* ###########################################################
  Extracting DC from a signal and then throwing the DC component out via PWM.
  The PWM is smoothed using an RC filter and then put through a difference amplifier with the original signal
  THis difference is then sent through analog A3 

  This exercise is one part of building a pulse oximeter, with the LED brightness once again being controlled
  by PWM (on pin 11, one more LED will need to be added later).
  
  Interrupt timer used to implement digital DC filter, taken from
  http://www.instructables.com/id/Arduino-Timer-Interrupts/
########################################################### */

#define redLED 11
#define irLED 5
#define DCout 3
#define DC_FILTER_ORDER 4

float filtered_value[DC_FILTER_BUFFER+1];
int value, last_value;
int value_buffer[DC_FILTER_BUFFER+1];
//value_buffer is implemented as a circular buffer of size = filter order + 1 (because we are using an IIR filter)
//filtered_value is also implemented as a circular buffer

void setup(){
  Serial.begin(115200);    // superfast serial communication
  
  double sampling_freq = 100;  // Fsampl in Hz
  int match_register = 16000000/(1024*sampling_freq) - 1; // match register to match that sampling frequency
  
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
  pinMode(redLED, OUTPUT);
  pinMode(irLED, OUTPUT);
  
  // set the voltages you want to output for the two LEDs (these will be RC-filtered eventually
  float voltage_red = 3.00;
  float voltage_ir = 2.5;
  
  // 
  analogWrite(redLED, int((voltage_red/5.0)*256) - 1);
  analogWrite(irLED, int((voltage_ir/5.0)*256) - 1);
}

ISR(TIMER1_COMPA_vect){   //  timer1 interrupt 100Hz
   // update variables...
   
   // will simply read A0 and then filter it
   value[0] = analogRead(A0); //present sample
   // Serial.println(value);
   
   // filter out PPG frequencies and only have the DC part
   // DSP LPF Cutoff = 
   filtered_value[0] = filtered_value[1] + 0.0002*(value[1] - filtered_value[1])+0.00007*(value[2]-filtered_value[2])+0.00002*(value[3]-filtered_value[3])+0.000005*(value[4]-filtered_value[4]);
   //filtered_value1[i] = filtered_value1[i-1] + 0.0002 * (data[i-1]- filtered_value1[i-1])+0.00007*(data[i-2] - filtered_value1[i-2])+0.00002*(data[i-3] - filtered_value1[i-3])+0.000005*(data[i-4] - filtered_value1[i-4])
   
   // the filtered value is now send out through PWM pin D3, which is also controlled by Timer2
   // filtered_value is in the range (0,1023) and the analogWrite value needs to be in the range (0, 255).
   // Hence we convert..
   analogWrite(DCout, int(256*(filtered_value[0] + 1)/1024) - 1);
   
   value[4]=value[3]; //last value in the input buffer is flushed out
   value[3]=value[2];
   value[2]=value[1];
   value[1]=value[0];
   
   filtered_value[4] = filtered_value[3]; //last value in the buffer is flushed out
   filtered_value[3] = last_filtered_value[2];
   filtered_value[2] = last_filtered_value[1];
   filtered_value[1] = filtered_value[0];

      
   // Then we read the value in again from an isolated analog pin and print it out..
   Serial.println(analogRead(A3));
}

void loop(){
  // nothign happens here
  // Serial.println(analogRead(A0));
}
