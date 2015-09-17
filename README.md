# hangouts_ros_automation

## Requirements
 Install the latest version of selenium with 
 pip install -U selenium

## Description

 The description of this package is it performs the following fucntions:
 1. Login to Sophia's webpage account located at [sophia.v1.api@gmail.com](mailto://sophia.v1.api@gmail.com)
 2. Validate whether Sophia is logged in her account by using the profile name found in the system. 
 3. Wait until a call comes to Sophia by waiting on the iframes. When a call comes accept the first call. And tell other
 calls that come after accepting the call (while that call is in progress) that she tells other people that she is in 
 call with (The Amount of People Available in the Video Hangout) and prompt the user to be added to that account.
  In other words this functionality can be defined as accepting upto ten people in the video conference to the google 
  hangout app developed earlier in the iteration.  
 4. Chat people up to 150 by spawning the chat engine the amount of times people are available. 
 
## Concept limitations
 
 Well Sophia must be online always. So for the missing texts which will be sent into the email a mechanism must be placed
 to circumvent that. 
 
## Why Such Implementation
 
 The concept of using the hangout api to develop application has nothing to do with the ability to access the google 
 plus features of a certain user. The hangout api has the ability to develop gadgets and extension that appear in the 
 hangout place placed in such a place as [Google apps Market Place](https://apps.google.com/marketplace/). That has the 
 added advantage of making it easier for people to chat with Sophia even if she is not available with a Google Account. 
 
 But to make the idea of Sophia more smooth a method to couple the features of google account based sophia has been 
 placed in the system for development. 
 
## Maintainability

 One of the primiary concerns that any person about using such functionality would be the ability or feasibility of using
 the broswer automation is how consistent is it to use the tools such as selenium on a platform such as that of the Google. 
 
 The answer being, I DON'T KNOW. What i can say is that the code is organized such that the changes to the UI of google
 would affect the UI processing unit and as such fixes need be done in only WebElements processing part of the code. This
 in my opnion, would limit the risk of making such developement from being obsolete in a matter of days. Though, That is
 dependent on people in Google.
 
## Running the Code
 
 A launcher that starts up the docker now also starts a selenium based fucntion at the following locations
 
## TODO

 Deployment of the hangouts app in [Google apps Market Place](https://apps.google.com/marketplace/). Tests for the App. 
 
