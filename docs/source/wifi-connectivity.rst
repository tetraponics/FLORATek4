WiFi Connectivity
==================

Beginning with firmware version 2.x.x, the FLORATek 4 has 3 different ways that the user can interact with the control remotely:

1. FLORATek Connect: Access your control from anywhere in the world using the FLORATek Connect dashboard. To access this service, you must have a current FLORATek Connect subscription, which can be purchased at www.tetraponics.com
2. Local Web UI: Access your control from any device on the same WiFi network. You can view current sensor status, make changes to setpoints, and download logs directly from your device. 
3. REST API: For advanced users, the FLORATek 4 control has a REST API that can be accessed from any device on the same WiFi network. This allows you to read data from and send commands to your control using custom scripts or applications, such as Home Assistant.


WiFi Connection Instructions
-----------------------------

All 3 of the above connectivity options require your FLORATek 4 control to be connected to your WiFi network. To connect your control to WiFi:

1. On your FLORATek 4 control, navigate to the "WiFi and Updates" menu
2. For Connection Type, select FTC if you wish to use FLORATek Connect, or Local if you only want to connect to your local network. 
  
  Note: If you select Local, your device will still be able to receive updates from Tetraponics. 

3. Select Start WiFi Provisioning. Your control will create a temporary WiFi network.
4. Connect to the temporary WiFi network using your smartphone or computer. The network name will be "FT4_XXXX Setup", where XXXX is the last 4 digits of your device's serial number.
  
  NOTE: If using a smartphone, you may need to disable cellular data to ensure that you are connected to the temporary WiFi network. Your smartphone may also warn you that no internet is available, with an option to stay connected. Please select to stay connected to the WiFi network, even if no internet is available.

5. Open a web browser and navigate to "192.168.4.1". Follow the on-screen instructions to connect your FLORATek 4 control to your WiFi network.

Once connected to WiFi, the Local Web UI and REST API will be accessible from any device on the same network. If you selected FTC as your connection type, you can also access your control from the FLORATek Connect dashboard from anywhere in the world.


FLORATek Connect
-----------------------------------------

Access to the FLORATek Connect functionality on your FLORATek 4 requires a current Remote Access Subscription.

You can access the FLORATek Connect dashboard from any browser on your computer or smartphone. 

FLORATek Connect Setup Instructions:

1. After subscribing to FLORATek Connect, proceed to www.connect.tetraponics.com
2. Login to FLORATek Connect using the same email used to purchase your subscription. You will need to create a password if you do not already have an account.
3. On the FLORATek Connect dashboard, select "Add Device". 
4. You will be prompted to enter your device's UID, which can be found on the bottom of your FLORATek 4 control near the pH probe plug. The UID is simply the last 4 digits of the serial number that starts with "FT4". You can also navigate to the "About" menu on your control using the left and right arrow keys, where the UID will be listed. 
5. You will also need to add your device's 6-digit PIN. This is found at the bottom of the WiFi & Updates menu.
6. Confirm that your device is connected to WiFi, and select "Add Device". Our servers will verify the information and connect your device to your FLORATek Connect account. This may take up to a minute.

You can now access your control directly from the FLORATek Connect dashboard on any computer or smartphone.


Local Web UI
-----------------------------------------

The Local Web UI can be accessed from any device on the same WiFi network as your FLORATek 4 control. 

1. Confirm your FLORATek 4 is connected to WiFi. Your computer or smartphone must be connected to the same WiFi network as your control.
2. On your control, navigate to the "Network Info" menu to find your control's local address. It will be formatted as "floratek4xxxx.local", where xxxx are the last 4 digits of your control's serial number. 
3. Open a web browser and navigate to your control's local address. 


REST API
-----------------------------------------

The FLORATek 4 control has a REST API that can be accessed from any device on the same WiFi network. This allows you to read data from and send commands to your control using custom scripts or applications, such as Home Assistant.

1. Confirm your FLORATek 4 is connected to WiFi. Your computer or smartphone must be connected to the same WiFi network as your control.
2. On your control, navigate to the "Network Info" menu to find your control's local address. It will be formatted as "floratek4xxxx.local", where xxxx are the last 4 digits of your control's serial number. 
3. You can send an HTTP GET request to "floratek4xxxx.local/datastream" to retrieve current sensor data in JSON format, or 
4. You can send an HTTP POST request to "floratek4xxxx.local/toggle" to toggle the control between run and pause mode.

Additional information about using REST API is beyond the scope of this manual. Tetraponics support cannot assist you with custom scripts or implementations. 


Monitoring Connection Status
-----------------

When enabled, WiFi connection status is displayed in the upper right corner of the main status screen:

* If ``.X`` is visible, your FLORATek is not connected to your WiFi network (or is not yet provisioned).
* When connected to FLORATek Connect, a "C" will be visible next to the WiFi Connection Symbol. 
* When connected without FLORATek Connect, an "L" will be visible next to the WiFi Connection Symbol.


WiFi and Updates Menu
----------------------

Connection Type
  This setting determines how your FLORATek 4 control connects to the internet. If you select FTC, your control will be able to connect to the FLORATek Connect dashboard from anywhere in the world. If you select Local, your control will only be able to connect to devices on the same WiFi network, but will still be able to receive updates from Tetraponics.

Automatic Updates
  When enabled, your FLORATek 4 control will automatically receive, download, and install updates. These updates will only be installed when the control is in the pause mode. If not enabled, you will be able to manually download updates from the WiFi & Updates menu when they are available from our servers.

Network Info
  Displays your current WiFi connection status, including the name of the network you are connected to, the signal strength, and the IP address of your control on the local network. You are also able to Reset your network information, which will disconnect you from your WiFi network and require you to go through the WiFi provisioning process again to reconnect.
