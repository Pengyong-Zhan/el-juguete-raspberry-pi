# How to Install Raspberry Pi OS on SD Card

#### Step 1. format your SD card

1. Download the software "SD Card Formatter" from https://www.sdcardformatter.com/

   <img src="assets/image-20230624184009343.png" alt="image-20230624184009343" style="zoom:23%;" />

2. Install "SD Card Formatter" in computer

3. Insert your SD card to computer

4. Open "SD Card Formatter", format the SD card by clicking below 3 icon or buttons.

   ![image-20230624185113316](assets/image-20230624185113316.png)

   Final Prompt:

   <img src="assets/image-20230624184819709.png" alt="image-20230624184819709" style="zoom:33%;" />



#### Step 2. Download and install Raspberry Pi Imager on computer

1. Download Raspberry Pi Imager from https://www.raspberrypi.com/software/

   Raspberry Pi Imager is used to write operating system (OS) to SD cards.

   ![image-20230624185739198](assets/image-20230624185739198.png)

2. Install Raspberry Pi Imager on computer



#### Step 3. Burn the OS to SD card

1. Open Raspberry Pi Imager

2. Select OS (the 1st option ended with "32-BIT") and your SD card

   <img src="assets/image-20230624190739183.png" alt="image-20230624190739183" style="zoom:33%;" />

3. Click the gear-like Setting button on the bottom right, set according to your preferences and needs, then click Save button

   <img src="assets/image-20230624191238431.png" alt="image-20230624191238431" style="zoom:33%;" />

   

   <img src="assets/image-20230624191821958.png" alt="image-20230624191821958" style="zoom:33%;" />

   

   <img src="assets/image-20230624192237138.png" alt="image-20230624192237138" style="zoom:33%;" />

4. Now, click "Burn", then click "Yes" in new prompt message box

   <img src="assets/image-20230624192342591.png" alt="image-20230624192342591" style="zoom:33%;" />

   

   <img src="assets/image-20230624192543324.png" alt="image-20230624192543324" style="zoom:33%;" />

5. Next, we need to be patient, have a cup of coffee or listen to Maluma, and wait for the OS to be written in SD card.

   About 10 minutes later, when the process is completed, click Continue button to finish this process.

   <img src="assets/image-20230624192728489.png" alt="image-20230624192728489" style="zoom:33%;" />

   no hurry, wait

   <img src="assets/image-20230624193054685.png" alt="image-20230624193054685" style="zoom:33%;" />

   no hurry, drink coffee and listen to music

   <img src="assets/image-20230624193451288.png" alt="image-20230624193451288" style="zoom:33%;" />

   finally!

   <img src="assets/image-20230624193609135.png" alt="image-20230624193609135" style="zoom:33%;" />

#### Step 4. Before Raspberry Pi setting - Connect to a Raspberry Pi Remotely via SSH in terminal

1. Remove the SD card from computer, then insert SD card to Raspberry Pi, power on the Raspberry Pi

2. Find your Raspberry Pi's IP address using Advanced IP Scanner downloaded from https://www.advanced-ip-scanner.com/

   -Firstly, install Advanced IP Scanner

   -Secondly, enter `ipconfig` in Powershell, find Default Gateway, in the example below is 192.168.0.1

   <img src="assets/image-20230625094116679.png" alt="image-20230625094116679" style="zoom:33%;" />

   

   -Thirdly, open it, enter IP address range from 192.168.0.1 to 192.168.0.255 (max 255, 200 is fine if no so many device in the same network) in the input box 

   <img src="assets/image-20230624201009834.png" alt="image-20230624201009834" style="zoom:33%;" />

3. Open Powershell (for Windows user), to login your Pi:

   -Firstly, enter one of the commands below, all commands (here and later on) should be followed by pressing Enter Key 

   -Secondly, enter your password, the password won't be show as you typing.

   **Notice**: this step might require patience, in case of login failure, don't lose heart, try it more times.

   ```
   #command 1: replace "pi" and "192.168.0.76" with your own username and IP address 
   ssh pi@192.168.0.76 
   
   or:
   //command 2: magia is host name, please refer to Step3.3
   ssh pi@magia.local
   ```

   login with `ssh pi@192.168.0.76` 

   <img src="assets/image-20230624201613937.png" alt="image-20230624201613937" style="zoom:33%;" />

   

   or login with `ssh pi@magia.local`

   <img src="assets/image-20230624201512335.png" alt="image-20230624201512335" style="zoom:33%;" />

   

#### Step 5. Basic Raspberry Pi setting 

Once we login, we can start setting!

1. Enter this command to start setting: `sudo raspi-config`, the following interface will be shown

   ![image-20230624221445275](assets/image-20230624221445275.png)

   

2. Setting the resolution

   -Firstly, press downward arrow key (↓) to select "2 Display Options", then press Enter key to continue

   ![image-20230624221753038](assets/image-20230624221753038.png)

   

   -Secondly, press downward arrow key (↓) to select "D5 VNC Resolution", then press Enter key to continue

   ![image-20230624221920119](assets/image-20230624221920119.png)

   

   -Thirdly, select 1024x768, then press Enter key

   ![image-20230624222225086](assets/image-20230624222225086.png)

   

   -Fourthly, with <ok> already auto selected, press Enter key to finish resolution setting process.

   ![image-20230624222457295](assets/image-20230624222457295.png)

   

3. Enable VNC

   -Firstly, select "3 Interface Options", then press Enter key to continue

   ![image-20230624223428693](assets/image-20230624223428693.png)

   

   -Secondly, select "I3 VNC", then press Enter key to continue

   ![image-20230624223501500](assets/image-20230624223501500.png)

   

   -Thirdly, press left arrow key (**←**) to select <yes>, then press Enter key to continue

   ![image-20230624223637881](assets/image-20230624223637881.png)

   

   -Fourthly, the following prompt screen will come up automatically, press Enter key to finish VNC enabling process

   ![image-20230624223708917](assets/image-20230624223708917.png)

   

4. Reboot Pi to enable changes to take effect

   -Firstly, press Tab key to select <finish> in the setting interface, then press Enter key to continue

   ![image-20230624223907142](assets/image-20230624223907142.png)

   

   -Secondly, press <Yes> to finish reboot process

   ![image-20230624223953164](assets/image-20230624223953164.png)

   

#### Step 6. Connect to a Raspberry Pi via VNC

Except login Raspberry Pi via SSH in terminal, we can also login via VNC.

1. Enter Pi's IP address, then press Enter key

   <img src="assets/image-20230624224752100.png" alt="image-20230624224752100" style="zoom:33%;" />

2. Click Continue in the prompt below

   <img src="assets/image-20230624224904059.png" alt="image-20230624224904059" style="zoom:33%;" />

3. Enter user name and password, then click OK

   <img src="assets/image-20230624225048785.png" alt="image-20230624225048785" style="zoom:33%;" />

4. Voila, now we see Raspberry Pi's desktop! 

   ![image-20230624230827331](assets/image-20230624230827331.png)

   

#### Step 7. Explore Pi setting through VNC

1. Click the raspberry logo on the top left, then click "Preferences", then click "Raspberry Pi Configuration"

   ![image-20230624231342610](assets/image-20230624231342610.png)

2. Let's set resolution again.

   -Firstly, click Display on the top, then select a different solution, for example: 1280x1024, then click OK

   ![image-20230624231439097](assets/image-20230624231439097.png)

   

   -Then, the interface below indicating "reboot is required to take effect" will be shown.

   Let's click "No" for now, so that we can continue to explore.

   ![image-20230624231542156](assets/image-20230624231542156.png)

3. Let's set time zone 

   Click Localisation - Set Timezone - select your Area and Location - click OK button

   ![image-20230625082156872](assets/image-20230625082156872.png)

4. Once finish all settings, click the OK button in Configuration interface on bottom right.

   Remember resolution change will take effect after reboot. 

   ![image-20230625082536738](assets/image-20230625082536738.png)

   