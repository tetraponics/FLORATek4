System Configuration
====================

Configuration settings that are typically adjusted infrequently.

Dosing Pump Setup
-----------------

Enters the Dosing Pump Setup submenu.

Manage Remote Pumps
~~~~~~~~~~~~~~~~~~~

Connected Pumps
  Displays the number of currently paired pumps.

Connect Remote Pumps
  Commands the control to find and pair any remote pumps.

Forget Remote Pumps
  Unpairs all remote pump connections.

pH Configuration
~~~~~~~~~~~~~~~~
Sets the current pH configuration to Up, Down, Down and Up, or None.

Track Consumption
~~~~~~~~~~~~~~~~~
Enables the solution level tracking functionality.

Pump Settings
~~~~~~~~~~~~~
For each pump (Pump 1, 2, ...):

Container Cap mL
  Set the capacity of the container for this pump.

Current Level mL
  Displays the current solution level in the container.

Set to Full
  Sets the container level to full.

Nutrient Labels
~~~~~~~~~~~~~~~
Sets custom labels for the installed nutrients.

Enable pH Control
-----------------
Enables or Disables pH control.

System Capacity (gal)
---------------------
Sets the water capacity of the hydroponics system in gallons.

Blend Time (min)
----------------
Sets the amount of time that the control will wait in between doses when in Run mode.

Alarm Settings
--------------

EC Alarm Band
  Sets the EC alarm band. If the measured EC is different from the setpoint by more than this amount, the appropriate EC alarm will be triggered.

pH Alarm Band
  Sets the pH alarm band. If the measured pH is different from the setpoint by more than this amount, the appropriate pH alarm will be triggered.

Low Temp Alarm
  If the temperature drops below this setting, the low temperature alarm will be triggered.

High Temp Alarm
  If the temperature rises above this setting, the high temperature alarm will be triggered.

Advanced Setup
--------------

Factory Reset
  Triggers a full factory reset. This will erase all saved variables/settings and revert the control back to the factory default settings.

Units
-----

EC Units
  Sets PPM or mS as the EC units. The FLORATek 4 uses the x500 scale (mS x 500 = PPM).

Temp Units
  Sets the temp units to Fahrenheit or Celsius.

Interface Settings
------------------

Backlight
  Sets the backlight level. (10 = max, 0 = off)

Backlight Timer (s)
  Sets the backlight timer in seconds. (0 = off)

LED Brightness
  Sets the brightness of the Alarm and Mode LEDs. (10 = max, 1 = min)

Enable Beeps
  Enables or disables the beeper.

Custom Gains
------------

pH Down Gain %
  Sets a custom pH down gain to compensate for strong/weak pH down solution (for example, setting to 50 will reduce the pH down solution used by half. Setting to 200 will double).

pH Up Gain %
  Sets a custom pH up gain.

Nutrnt Gain %
  Sets a custom nutrient gain.

Set Time
--------
Used to set the current time. Input the current date and time, then select "Set Time".

System Setup Details
--------------------

System Capacity & Blend Time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The FLORATek control uses the system capacity setting to calculate doses. It is important to input the full water capacity of your entire hydroponics system, not just the capacity of your reservoir.

After the FLORATek control calculates and adds a dose, the added nutrients and pH solutions need time to thoroughly blend with the water in your system. If the blend time is set too low, the control will quickly overshoot the setpoints. If this number is too high, the control will take an excessively long amount of time to reach the setpoints. Always start with a blend time higher than you believe is appropriate! It is much safer for your plants if the control slowly reaches the setpoints compared to if the control overshoots the setpoints. The blend time can be reduced as you learn how "fast" or "slow" your hydroponic system is.

A good starting point for Blend Time is 3 times the turnover time:

  (System Capacity / GPM) x 3 = Blend Time

.. note::

   Your actual pump rate may be much slower than the rate listed by the pump manufacturer, especially if smaller tubing and large pumping heights are used.

Solution Concentrations
~~~~~~~~~~~~~~~~~~~~~~~

The FLORATek 4 control is designed to work with a wide variety of pH control and nutrient solutions. However, some commercially available solutions can be more or less concentrated than the FLORATek's control algorithm is expecting. After using your control for a few cycles, if you notice that the pH or EC is consistently overshooting the setpoint, you probably are using more concentrated solutions. In the "Custom Gains" setup submenu, decrease the affected solution's gain to reduce the amount of solution the control will add. Conversely, if you notice the control takes an exceedingly long time to reach the setpoint, you can try increasing the gain of the affected solution to increase the amount of solution the control will add.

The default gain is 100%. By lowering the nutrient gain to 20% for example, the control will only add 20% of the calculated dose. By increasing the nutrient gain to 200%, the control will add 200% (or double) of the calculated dose.

.. warning::

   We strongly recommend keeping your gains set to 100% unless you are repeatedly experiencing dosing overshoots or undershoots and have confirmed all other settings are correct.
