<img src="https://github.com/Dorahan/First-Python-Project/blob/master/README/smc-1.png" alt="logo" width="150">
# SOCIAL MEDIA CONTROLLER
First python project, connect and control multiple social media accounts to access and control activity from a single dashboard. The purpose of this project is to learn and practice python and also have fun.

<br>
### INITIAL DESIGNS
**Home Page**  
When the app is launched the user is greeted with an option to pick which social media to use.

<img src="https://github.com/Dorahan/First-Python-Project/blob/master/README/smc-2.png" alt="logo" width="400">

**Post Page**  
After selecting Twitter application user will go into the post screen. If there is not text the post button will be disabled.

<img src="https://github.com/Dorahan/First-Python-Project/blob/master/README/smc-3.png" alt="logo" width="800">

**Error Messages**  
There will be social media platform specific error messages. For example for Twitter if there is more than 140 characters the post button will be disabled with a highlight color accompanied with an error message.

<img src="https://github.com/Dorahan/First-Python-Project/blob/master/README/smc-4.png" alt="logo" width="400">

**Different Platforms**  
Each platform will have its specific UI design and color. In the current design, only the background and button color will change to social media brand color. Also the account name will change for each platform.

<img src="https://github.com/Dorahan/First-Python-Project/blob/master/README/smc-5.png" alt="logo" width="400">

-

###FINAL OUTPUT
**Home Page & Post Page**

<img src="https://github.com/Dorahan/First-Python-Project/blob/master/README/smc-6.png" alt="logo" width="800">

**Error Messages**

<img src="https://github.com/Dorahan/First-Python-Project/blob/master/README/smc-7.png" alt="logo" width="400">

-

###FUTURE WORK  
The first attempt will be to match the initial planned designs and implement the error messages inside the UI instead of a popup messages. Other future work will include additional social media accounts and to be able to have a login module for anyone to setup their account. Right now the access tokens are hard coded inside the project, this is neither safe nor practical for distribution of this project.

The learnings to apply for this project is that designing UI inside tkinter is not as practical compared to other platforms, so when going forward with this project the best decision would be to keeping the UI as simple as possible without losing much context.

-

###REFERENCES###
1. Main body is based on the ITU Editor project.
2. Source for creating multiple frames:  
http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
3. Tweepy API Reference: http://tweepy.readthedocs.io/en/v3.5.0/index.html
4. Check posts at: https://twitter.com/PythonTests
5. Tutorial to post on Facebook: http://nodotcom.org/python-facebook-tutorial.html
6. Facebook API Reference: http://facebook-sdk.readthedocs.io/en/latest/api.html
7. How to receive the access tokens:  
https://developers.facebook.com/docs/facebook-login/access-tokens



