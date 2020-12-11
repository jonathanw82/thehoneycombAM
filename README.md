# thehoneycombe
Apiary Management for beekeeping 

## The users goals of this aplication are:
# Create Apirary with contact details.
# Add Bee hives
# Add inspection documents to each hive
# Add medical documents to each hive
# Add purchased medicine to a specific section that warns if the medicine is out of date
# A facility to download the history of a specific hive and its medical documants
# A facility to download the medical history.


# Weather Api.
The Weather app was added to help the beekeeper to judge the weather before they set off to there out apiary. Using the postcode added to the apiary on its creation, the wether app uses OpenCage API to get the longitude and latitude of the postcode provided. These details are then sent to the OpenWeatherMap API within with the URL request to give the most accurate location weather report possible. Regardless of the apiary that is selected, the weather will change to that relevant postcode.

The reason two API requests are relevant is that OpenWeatherMap API uses the longitude and latitude as its point of origin, postcodes or area names can not be used, also OpenCage API will accept postcodes in non-uppercase and with or without a space in the middle allowing for more flexibility and less code to tidy up the postcode depending on how the user inputs it.

The Weather app displays the area relevant to the postcode, current temperature, description of the current conditions, image of the current condition and a temperature feels like. Followed by a 5-day forecast displaying an image of the predicted condition of that day with the chance of rain as a percentage and temperatures hi and low. I chose these particular attributes as I find they are what I am looking for before I set out to manage my bees.

If the temperature is 20 degrees or over the background of the weather box will change from blue to red. 
If there are adverse weather conditions predicted a weather alert will display above the 5-day forecast displaying the message sent from the API.
If any errors should occur with either APIs, message weather unavailable will be displayed inplace of the weather app.
 
# Download docs to pdf.


The Business potentials of this website are:

This Website is the best way to help them achieve these things because:

## Technology’s used will include:
<div align="center">
   <img width="80%" height:auto;" src="static/images/logos.jpg" alt="logo image"/>
 </div>
                                                                                
[HTML5](https://en.wikipedia.org/wiki/HTML5), [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets), [Bootstrap](https://getbootstrap.com/), [Javascript](https://en.wikipedia.org/wiki/JavaScript), [jQuery](https://jquery.com/), [Python3](https://www.python.org/), [C++](https://en.wikipedia.org/wiki/C%2B%2B), [VScode](https://code.visualstudio.com/), [Balsamiq Mockup 3](https://balsamiq.com/wireframes/desktop/), [Adobe Photoshop](https://www.adobe.com/uk/products/photoshop.html?gclid=EAIaIQobChMIzNru2Myo6AIVF-DtCh28Fgn0EAAYASAAEgKkdvD_BwE&sdid=88X75SKR&mv=search&ef_id=EAIaIQobChMIzNru2Myo6AIVF-DtCh28Fgn0EAAYASAAEgKkdvD_BwE:G:s&s_kwcid=AL!3085!3!394411736356!e!!g!!photoshop)
[PostgreSQL](https://www.postgresql.org/), [OpenWeather API](https://openweathermap.org/), [OpenCage API](https://opencagedata.com/), [Django](https://www.djangoproject.com/), [Heroku](https://www.heroku.com/) and [Arduino](https://www.arduino.cc/).
##


## Bee Metrics

# Transmitter
The ATmega in the top of the hive (Transmitter) will send temperature, humidity, Sound frequency and battery voltage to the ATmega (Receiver) at the bottom of the hive wirelessly via the HC-12 transceivers. 

The Transmitter will sleep for a set period of time then wake, it will then send the capital A via a serial print function, if the transmitter has not received a capital B if will try 30 times then go back to sleep, this is a fail-safe to protect the batteries if the receiver has gone down. If the receiver wakes as intended, on receipt of the capital A it will transmit a capital B, the transmitter will then collect the data and transmit it back to the receiver vis a serial print function, then go back to sleep.

# Transmitter Led status
Green blink sleep-waking.
Red led Awaiting handshake, sending A and waiting to receive B.
Blue Led sending data.

# Boot order of Transmitter.
On Wake, set the sleep delay to zero, wake variable to true, detect the sound frequency, battery voltage, temperature, humidity. Then establish a connection and send data.

Why am I metering the sound frequencies in the beehive?.  There is scientific data that correlates changes in sound frequency inside the beehive when the behaviour of the bees change, this data can be used to predict swarming or intent to swarm, the doc can be found [here](https://www.researchgate.net/publication/229224190_Monitoring_of_swarming_sounds_in_bee_hives_for_early_detection_of_the_swarming_period). It also relates to where the hive is queenless.

Quote form the doc (Swarming is indicated by an increase in the power spectral density at about 110 Hz; approaching to swarm the sound augmented in amplitude and frequency to 300 Hz, occasionally a rapid change occurred from 150 Hz to 500 Hz. Another finding indicating the initiation of a swarming period is the rise in temperature from 33 °C to 35 °C until the actual time of swarming when the temperature starts dropping to 32 °C. With more activity, ventilation from bee wings causes a drop of temperature.) with this I mind is the reason we are also collecting the internal hive temperature.
#

## Library & Dependencies
Django
Django-allauth
Pillow
Django-crispy-form

## Tutorials
Confirm Delete
https://www.youtube.com/watch?v=OIfKHssR1oc

https://pixabay.com/videos/bee-honey-insect-beehive-nature-39121/

## Icons
favicon.io Icons made by https://www.flaticon.com/authors/freepik title=Freepik from https://www.flaticon.com/
Navbar Logo Icons made by https://creativemarket.com/eucalyp title= Eucalyp from https://www.flaticon.com/
Wiki Icons made by https://www.flaticon.com/authors/freepik title=Freepik from https://www.flaticon.com/
Hive Icons made by https://www.flaticon.com/free-icon/bee-hive_1724149?term=hive&page=1&position=72 title= Vitaly Gorbachev from https://www.flaticon.com/www.flaticon.com

## Credits



## Bee Metics Credits
# Voltage metering, 
https://create.arduino.cc/projecthub/next-tech-lab/voltmeter-using-arduino-00e7d1


# Sound Frequency counter,
https://www.youtube.com/watch?v=wbeV0J30LGQ


# Info on Sound frequency,
https://www.researchgate.net/publication/229224190_Monitoring_of_swarming_sounds_in_bee_hives_for_early_detection_of_the_swarming_period
http://www.beehacker.com/wp/?page_id=103


# Arduino Sleep Cycle,
https://github.com/RalphBacon/Arduino-Deep-Sleep 


# Arduino Sleep wake from serial interupt
https://arduino.stackexchange.com/questions/13167/put-atmega328-in-very-deep-sleep-and-listen-to-serial
