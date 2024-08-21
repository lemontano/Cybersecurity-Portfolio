# Capturing Username and Password

## Steps
1. The first thing you want to do is make sure that you are on a secure network. I like to use a VM since its contained and has no where to go. 
2. Once you load up your environment load up Wireshark.
3. Wireshark should be open now you have to select what network to scan or you can just select the blue fin at the upper right hand corner. See image below. 

![image](https://github.com/user-attachments/assets/ff109b24-0226-4f44-a181-a4907adcd248)
Wireshark should look like the image below if you started it correctly.
![image](https://github.com/user-attachments/assets/cf533e05-d397-401a-b1b0-26bda11f653f)

4. Load up a website on google and look for an unsecure website which should search http website login. This will allow you to see unsecure websites. Note: That is why it is important to be on a secure environment.
5. Select any webpage you like. I will be selecting Vulnweb. See image below
![image](https://github.com/user-attachments/assets/dc24e0d9-69ba-4c03-abbe-744b7e3e426b)

6. While Wireshark is running in the background I will be inserting made up credentials. See image below
![image](https://github.com/user-attachments/assets/3b56eacb-d1a9-4e7e-9a80-31b045500cc0)
7. Obivously the username and password are incorrect. I hit entered and nothing happen.
8. Now I have to go back to Wireshark and hit the red square next the blue fin to stop the scan.
9. Once the scan has been stopped we have to filter out to http since that is the protocol we want to jump to. See image below on how to filter in Wireshark.
 ![image](https://github.com/user-attachments/assets/4c410e45-c934-4353-80ab-1a60044753cb)
10. Once you filter then you'll see it filter to only http.
   ![image](https://github.com/user-attachments/assets/a9388573-d651-4eb1-8a91-43443b618745)
11. Select the capture with OK right click on it and follow the TCP stream.
    ![image](https://github.com/user-attachments/assets/ebe10f04-0cf0-48c9-8881-8212680b1f1b)
12. Once you open up the TCP stream then a window will pop up with addtional information. That is where you can find the username and password that was inserted in the website above. See image below. 
   ![image](https://github.com/user-attachments/assets/33093dfe-c07f-46d6-91e3-d282f359fa76)

     
