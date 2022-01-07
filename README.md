# Graphical Password Authentication System

<p align="center">
  <img src="https://github.com/HxnDev/Graphical-Password-Authentication-System/blob/main/Extras/Picture1.png" width=500 height=300>
</p>

## Description:
For this project, we designed a Graphical Password Authentication System. This is used to increase the protection/security of a website. Our system is divided into further 4 layers of protection. Each layer is totally different and diverse than the others. This not only increases protection, but also makes sure that no non-human can log in to your account using different activities such as Brute Force Algorithm and so on. The motivation for this project came from a recent attack named **Pegasus** in which people had their mobile phones compromised for almost a decade without them ever getting the slightest clue. This motivated us to build a stronger authentication system that generates randomized methods which could weaken the attack and eventually prevent it. The 4 layers of Protection that we are using are as follows:
1.	Segmented Images Authentication
2.	Password Image Authentication
3.	Obscured Images Authentication
4.	Garbled Images Authentication

The above layers have been sorted according to their complexities (1 being the least complex and 4 being most complex). The detailed explanation of the layers are as follows:


### 1: Segmented Images Authentication:
For this layer, the user will be showed 4 different images. These images will be a division of a whole image. User will have to select the correct order of the images. The logic can be explained better with the following picture:
<p align="center">
  <img src="https://github.com/HxnDev/Graphical-Password-Authentication-System/blob/main/Extras/segmented.png" width=200 height=200>
</p>
As can be seen in the above image, a circle is divided into 4 parts. These 4 parts will be randomly displayed on the screen and user will be asked to select the pieces in correct order. The order is determined on the basis of the time of click. If an image is clicked first, it will be selected as the first image and so on. If a user selects all 4 pieces in the correct order, he/she will be authenticated. 

The key thing to note here is how it offers security but without compromising usability – it is very easy for even young humans to recognise patterns in images and choose the correct order.

According to our implementation, we first display the pieces of circle in a randomized order every time. The user is then asked to select the images in the correct order as being displayed on the screen. Our code will detect the time of click here. Every click on a picture is stored along with the time it was clicked. Once all images are clicked, we simply sort by time and check that they were selected in the correct order. If yes, then the user will be authenticated.

This layer in our system can be seen as follows:

<p align="center">
  <img src="https://github.com/HxnDev/Graphical-Password-Authentication-System/blob/main/Extras/segmented.gif" alt="animated" width=400 height=200>
</p>

### 2: Password Image Authentication:
For this layer, we took inspiration from Meezan Bank’s authentication system. Whenever a user registers, he/she is asked to select an image category from the 3 given categories:
-	Cat
-	Mouse
-	Flower

Whatever the user selects, is associated with his/her password and every time the user logs in, he/she will be asked to select the same image from the randomly displayed images.

Now here’s the twist. We have stored multiple images for each category. So, if a user selects cat, he/she will not be displayed the same cat every single time. The images per category are different as can be seen below.
#### a) Cat:
<p align="center">
  <img src="https://github.com/HxnDev/Graphical-Password-Authentication-System/blob/main/Extras/cat.png" width=300 height=100>
</p>

#### b) Mouse:
<p align="center">
  <img src="https://github.com/HxnDev/Graphical-Password-Authentication-System/blob/main/Extras/mouse.png" width=300 height=100>
</p>

#### c) Flower:
<p align="center">
  <img src="https://github.com/HxnDev/Graphical-Password-Authentication-System/blob/main/Extras/flower.png" width=300 height=100>
</p>

According to our implementation, we have stored 3 categories i.e., cat, mouse, flower in our database. Whatever the user has selected while registering has been stored into the database along with his password. Each category has 3 different versions named 0, 1, 2. At the start of the program, a random number is generated between 0 and 2. Whatever the number is, is the picture of each category that is to be displayed. This is to just add a bit more complexity to the code. Let’s say a user has selected image 1 of cat. Upon authentication he may be shown image 0 of cat (which will be a different cat) but the key thing is that it will be a cat and the user must select it in order to be authenticated. 

This layer in our system can be seen as follows:
<p align="center">
  <img src="https://github.com/HxnDev/Graphical-Password-Authentication-System/blob/main/Extras/login.gif" alt="animated" width=400 height=200>
</p>

### 3: Obscure Image Authentication:
This is one of the most interesting layers. In this layer, not only are we preventing bots but we are also enhancing security by introducing image-to-speech-to-text concept. Let’s dig deeper into what this concept really is.

#### Image-to-Speech-to-Text:
In this concept, a user is displayed an image with obscure text. The reason for adding this obscurity is to confuse a NLP or OCR type mechanisms in bypassing the authentication. Random words are generated on a file which is then covered with an obscure text. 

For example:
<p align="center">
  <img src="https://github.com/HxnDev/Graphical-Password-Authentication-System/blob/main/Extras/obscure.jpg" width=300 height=100>
</p>

This picture is then displayed to the user and user is asked to speak the words in the given image. Now, here a trained model will give false results as it wouldn’t know which text to read whereas a human can do so. 

Then the user will speak the text in correct order which our system will then convert to text and verify if the user spoke correct text. If verified, the user will be granted access. 

For this feature, we are using **“Speech Recognition”** module of Python. User will be displayed the obscure text image and there will be a microphone button. When user will click the button, the recording will start and user will be asked to say the words in the image. When user says all the words, he/she must say **stop** in order for the program to stop recording. Then all the speech will be converted into individual words and stored in each index of an array. This array will then be compared to the expected output array. If both the arrays match, then the user will be authenticated.

This module can be installed using: ***pip install speechrecognition***

This layer in our system can be seen as follows:
<p align="center">
  <img src="https://github.com/HxnDev/Graphical-Password-Authentication-System/blob/main/Extras/obscure.gif" alt="animated" width=400 height=200>
</p>

### 4: Garbled Image Authentication:
The last and the most difficult layer is the garbled text authentication. In this layer, the user will be displayed a Garbled text whose readability will be really low and user will be asked to read and then type in the text. The garbled texts will be randomly generated as follows:
<p align="center">
  <img src="https://github.com/HxnDev/Graphical-Password-Authentication-System/blob/main/Extras/garbled.png" width=200 height=300>
</p>
For this layer, we have generated multiple garbled text images and stored the correct value of each image in a file. User is shown a random image in the start of this layer and is asked to type in the correct text. Whatever the user types is then compared to the already stored correct values and if the answer is correct, then user will be authenticated and authentication dialogue box will pop up.

This layer in our system can be seen as follows:
<p align="center">
  <img src="https://github.com/HxnDev/Graphical-Password-Authentication-System/blob/main/Extras/garbled.gif" alt="animated" width=400 height=200>
</p>

## Security Analysis:
Following is the detailed security analysis of our system:

### 1: Issues Covered:
The majority of applications/websites use text-based passwords to authenticate a user, with the additional use of CAPTCHA to verify that the user is a human. Unfortunately, this is not very secure and leaves the system vulnerable to different sorts of attacks. While text-based passwords sound secure in theory, in practice most users will end up making simple, common passwords that are frequently repeated across different applications or accounts. Bot attacks or hackers can take advantage of this and launch dictionary attacks, try to brute force the password or employ other ways to compromise user accounts.

### 2: Security Strengths:
Graphical passwords are a more secure alternative to standard text-based passwords, especially as they don’t significantly lower usability. Using graphical password authentication, we can avoid the problem of keystroke logging, and be protected against dictionary attacks and social engineering. This technique for user authentication also requires human interaction on part of the user, which doubles as verifying the user was a human without having to make use of CAPTCHA (which is infamously annoying for users.) There will be several security layers, and the system will be customizable i.e., you can choose the types of security you want, depending on your security requirements.

### 3: Security Weaknesses:
There are no major security vulnerabilities. However, our system is limited in scope so there are very small number of options for each module. Such as garbled text has a limited number of pictures to be chosen randomly from. This is not an inherent weakness of the system, as on a larger scale it could be adapted to generate or segment images dynamically and so on. But in the current state of the system, it would be possible for a computer to eventually brute force its way to the solution. 

## Contributors:
In the end, I'd like to mention my group members who helped me alot in this project. You can find them at:

[Sana Khan](https://github.com/sanaa-khan)

[Wajeeha Malik](https://github.com/wajeehamalik913)

## 📫 Contact Me: 
<p align="center">
  <a href="http://www.hxndev.com/"><img src="https://img.icons8.com/bubbles/50/000000/web.png" alt="Website"/></a>
	<a href="mailto:chhxnshah@gmail.com"><img src="https://img.icons8.com/bubbles/50/000000/gmail.png" alt="Gmail"/></a>
	<a href="https://github.com/HxnDev"><img src="https://img.icons8.com/bubbles/50/000000/github.png" alt="GitHub"/></a>
	<a href="https://www.linkedin.com/in/hassan-shahzad-2a6617212/"><img src="https://img.icons8.com/bubbles/50/000000/linkedin.png" alt="LinkedIn"/></a>	
</p>
