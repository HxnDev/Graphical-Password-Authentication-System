# Graphical Password Authentication System

<p align="center">
  <img src="https://github.com/HxnDev/Graphical-Password-Authentication-System/blob/main/Extras/Picture1.png" width=500 height=300>
</p>

## Description:
For this project, we designed a Graphical Password Authentication System. This is used to increase the protection/security of a website. Our system is divided into further 4 layers of protection. Each layer is totally different and diverse than the others. This not only increases protection, but also makes sure that no non-human can log in to your account using different activities such as Brute Force Algorithm and so on. The motivation for this project came from a recent attack named Pegasus in which people had their mobile phones compromised for almost a decade without them ever getting the slightest clue. This motivated us to build a stronger authentication system that generates randomized methods which could weaken the attack and eventually prevent it. The 4 layers of Protection that we are using are as follows:
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

![Demo Video](https://github.com/HxnDev/Graphical-Password-Authentication-System/blob/main/Extras/segmented.gif)

### 2: Password Image Authentication:

### 3: Obscure Image Authentication:

### 4: Garbled Image Authentication:

## Security Analysis:

### 1: Issues Covered:

### 2: Security Strengths:

### 3: Security Weaknesses:


## Demo Video:

![Alt Text](https://github.com/HxnDev/HospitalAid/blob/main/Features/Fainting%20Detection/Extras/fainting.gif)
