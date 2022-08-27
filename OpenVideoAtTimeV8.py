import os
import datetime
import time
# requires import of opencv through pip
# pip install opencv-python
import cv2
# requires import of PIL pillow through pip
# python -m pip install pillow
from PIL import Image, ImageTk

import sys
import tkinter
  
def my_VidFunction(vid_name):
	cap = cv2.VideoCapture(vid_name)
	#check if the video capture is open
	if(cap.isOpened() == False):
		print("Error Opening Video Stream Or File")

	while(cap.isOpened()):
		ret, frame =cap.read()

		if ret == True:
			cv2.namedWindow('frame', cv2.WINDOW_KEEPRATIO)
			cv2.setWindowProperty('frame',cv2.WND_PROP_ASPECT_RATIO,cv2.WINDOW_KEEPRATIO)
			#cv2.namedWindow('frame', cv2.WND_PROP_FULLSCREEN)
			cv2.setWindowProperty('frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
			cv2.imshow('frame', frame)

			if cv2.waitKey(25)  == ord('q'):
				break

		else:
			break

	cap.release()
	cv2.destroyAllWindows()

def showPIL(pilImage):
	root = tkinter.Tk()
	w, h = root.winfo_screenwidth(), root.winfo_screenheight()
	root.overrideredirect(1)
	root.geometry("%dx%d+0+0" % (w, h))
	root.focus_set()
	root.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))
	canvas = tkinter.Canvas(root,width=w,height=h)
	canvas.pack()
	canvas.configure(background='black')
	imgWidth, imgHeight = pilImage.size
	if imgWidth > w or imgHeight > h:
		ratio = min(w/imgWidth, h/imgHeight)
		imgWidth = int(imgWidth*ratio)
		imgHeight = int(imgHeight*ratio)
		pilImage = pilImage.resize((imgWidth,imgHeight), Image.ANTIALIAS)
	image = ImageTk.PhotoImage(pilImage)
	imagesprite = canvas.create_image(w/2,h/2,image=image)
	root.after(2000, root.destroy)
	root.mainloop()
	
#grab time now
now = datetime.datetime.now()

print('Press ctl and c in terminal or command window to exit slide show.')
print('Make sure default image viewer opens full screen. Then close it when full screen.')

im = Image.open(r"black_all.png")
showPIL(im)

while (True):
	# open method used to open different extension image file
	
	# resized_im = im.resize((round(im.size[0]*4), round(im.size[1]*4)))
	# This method will show image in any image viewer 
	# resized_im.show()

	if ((now.hour >= 8) and (now.hour <= 22 )):
		if ((now.hour == 12) and ((now.minute % 30 == 0) or (now.minute % 30 == 1))) or ((now.hour == 17) and ((now.minute % 60 == 0) or (now.minute % 60 == 1))):
			my_VidFunction('ShiftChangeYouTubeHIGH.mp4')
			# grab time again, so not using time at stop of this loop instance
			now = datetime.datetime.now()
		else:
			my_VidFunction('cci_icommons_album.mp4')
			# grab time again, so not using time at stop of this loop instance
			now = datetime.datetime.now()
	else:
		showPIL(im)

	# close the image
	#im.close()
	#resized_im.close()
