import cv2
import numpy as np
img=cv2.imread('l1.png')
img1=img
s=img.shape
x=s[0]
y=s[1]
for i in range(1,x):
	for j in range(1,y):
		v=img[i,j]
		if (v[2]>=v[0]|v[2]>=v[1]):
			img[i,j]=v
		else:
			img[i,j]=[0,0,0]
cv2.imshow('ori',img1)
cv2.imshow('img',img)
cv2.waitKey(0)




