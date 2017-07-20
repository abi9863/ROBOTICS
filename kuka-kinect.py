import cv2
import imutils
import numpy as np

#getting video from kinect KV=DEPTH=KVO BG=rgb video

hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)#CONVERTING TO HSV
g=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#CONVERTING TO GRAYSCALE

lb=np.array([180,255,0])#POSSIBLE HSV VALUE FOR BLACK THRESHOLDING
hb=np.array([180,255,40])

mask=cv2.inRange(hsv,lb,hb)
res=cv2.bitwise_and(frame,frame,mask=mask)#THRESHOLDING

kernel=np.ones((5,5),np.uint8)
closing=cv2.morphologyEx(res,cv2.MORPH_CLOSE,kernel)#BETTER IMAGE

r,c= BG.shape#GETTING SIZE OF THE VIDEO SCREEN


for i in range(0,r):
	for j in range(0,c):
		v=KV[i,j]
		if (v[2]>=v[0]|v[2]>=v[1]) & (closing[i][j]==1):
			KV[i,j]=v#for target object
		elif (v[2]>=v[0]|v[2]>=v[1]) & (closing[i][j]!=1):
			KVO[i,j]=[255,0,0]#obstructions shown in blue
		else:
			KV[i,j]=[0,0,0]
			KV0[i,j]=[0,0,0]
gr=cv2.cvtColor(KV,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gr,(5,5),0)
thresh=cv2.threshold(blur,12,255,cv2.THRESH_BINARY)[1]
###################################################

cnts=cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts=cnts[0] if imutils.is_cv2() else cnts[1]

for c in cnts:

	M=cv2.moments(c)
	cx=int(M["m10"]/M["m00"])#FINDING CENTRE OF THE TARGET OBJECTS
	cy=int(int(M["m01"]/M["m00"])

ic_r=r/2 if r%2==0 else ((r+1)/2)#FINDING CENTRE OF THE VIDEO SCREEN
ic_c=c/2 if c%2==0 else ((c+1)/2)

if (ic_c!=cy):
	if(ic_c>cy):#BOT IS LOOKING TO LEFT OR RIGHT
		#ros block to move the bot left
	else 
		#ros block to move the bot right



