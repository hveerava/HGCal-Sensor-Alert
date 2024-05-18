# hgcal_sensor_data
**Provided Scope**

Deliver code in a GitHub repository for a functional environmental monitoring system. Hardware will be provided or purchased as needed by Eva & Jessica.

**Existing Architecture**

_Particle Monitoring Hardware:_
See this GitHub page for details. Our existing setup uses the Enviro Urban which consists of a sensor suite soldered directly to a Raspberry Pi Pico W. Currently, this sensor is only accessible via the local network in the clean room. 

**Base Station Hardware**

The base station, or “broker” in the MQTT framework, is responsible for managing communication between the various sensors and translating their output to a more parse-able format. We use a Raspberry Pi for this. Currently this device is only accessible via a keyboard and monitor in the lab.

_Improvements:_
The current system functions well for occasional use within the lab but leaves a lot to be desired in terms of versatility. There are a few improvements we’d like to implement:

**Network Bridge**

As part of the two below improvements, the base station Raspberry Pi will need to act as a bridge between the lab network (intranet) to communicate with the sensors and the external network (internet) to send alerts and publish a webpage. This will require two network interfaces and additional configuration.

Step 1: Using two separate network interfaces, ping devices on both networks manually switching between them

Step 2: Ping devices on both networks automatically or programmatically switching between them

Step 3: Bridge data across networks (receive from intranet, send to internet)

**External Access**

We would like to be able to access both the current sensor data and the sensor logs via remote computers. 

Step 1: connect to the base station via SSH and easily find current data and logs

Step 2: base station broadcasts to a webpage that is accessible on the local network

Step 3: base station broadcasts to a webpage that is accessible anywhere

**Alerts**

We would like the base station to broadcast alerts if parameters like particle count, temperature, or humidity fall outside of the desired range.

Step 1: record an alert state locally to the base station

Step 2: publish alert state to the webpage

Step 3: send an email to a predefined list of contacts