# WIT-CMU
Vehicle Interior Monitoring System - IoT Project | Collaboration WIT and CMU. 

# Team
Beatrice Smetana (CMU) ｜ Loti Ibrahimi (WIT) ｜ Justin Lizotte (CMU)

We worked on a Vehicle Interior Monitoring System to prevent chidren being left behind in dangerous situations with the parent not being in range. This can be very dangerous especially in some warmer countries, and has resulted in many fatalities each year, with children primarily under the age of 3. The cause usually being heatstrokes.

# Tools/Software
## Raspberry pi
We are using a raspberry pi (to act as the car), which is the core of all events/actions. We decided to go with just three sensors for demonstration purposes: Temperature Sensor, Pressure Sensor & Bluetooth (for proximity check). 

- BME680 used for taking in the temperature readings. 
- Raspberry Pi has built in bluetooth. Used (preferrably an Android phone for accuaracy) as the parents device.

## Wia.io
Wia powers the future of the Internet of Things by enabling devices to communicate with one another in a simple, easy way. We are handling all functions within a single python script and determining severity of the sitation under different conditions, then publishing one event to Wia (Alert = 'Unsafe') which, with the use of Wias Flow Builder, allow for notifications to be sent to guardian. We decided to simply go with email alerts. 
