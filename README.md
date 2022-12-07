# betterer  

## Problem:  
I have collections of thousands of camera images which may or may not 
have interesting content in them.  Most of the time, there's barely
any changes from frame to frame.  It would be convenient to also zoom
to a date/time as opposed to scrolling through.  

The Files viewer in Ubuntu (20.04) is really inefficient w.r.t. loading 
folders that contain 100 000 folders.  

## The Proposed Solution:  
Ultimately, a simple tool that pops up, shows an image, a preview of 
images around it, and allows for circular scrolling AND feature change
fast forward.  

## Phase I (MVP):  
A UI tool can be pointed to a folder and if it contains images, to fetch 
the names of all of the images, pick the middle image as primary, and 
allow for backward and forward scrolling through the images.  

### Expansion:  
Assuming 100 000 photos in a folder - they are all chronologically sequenced.  Pick the middle photo and 10 photos either side of it.  Display the 
main photo, and a small reel below of the other 10.  Moving right means that one or more off of the left side go away, and one ore more are added to the right with the main now being the root.  

That is the tip off: 'root'.  I suspect that I'll use a tree.  

THe root will be the main photo.  When one side or another becomes too unbalanced, it will adjust.  (Thinking about how to do this.)

## Phase II:  
A carosel of images should be displayed under the current image, reflecting
the +X and -X images from its position.  

## Phase III:  
Time and date search - move the image pointer to the closest time and date 
within the carosel.  

## Phase IV:  
Fast Forward/Reverse - avoid long stretches of nearly static images and 
only zoom to the changes which is where the cool stuff happens.  


