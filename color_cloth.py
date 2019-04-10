import cv2
import numpy as np

cap = cv2.VideoCapture(0)
color = np.zeros((3,))
skip = 0

col = np.array([162,60,70])
base_img = []

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output1.mp4',fourcc, 20.0, (640,480))
out1 = cv2.VideoWriter('original1.mp4',fourcc,20.0, (640,480))

while(True):
	ret,frame = cap.read()
	if(ret == False):
		continue
	img = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

	out1.write(img)
	skip+=1

	if(skip<100):
		if(skip==50):
			base_img = img

		continue

	elif(skip==100):
		print("start")

	elif(True):

		channel1 = np.logical_and(np.greater(img[:,:,0],(np.ones(img[:,:,0].shape)*110)),np.less(img[:,:,0],(np.ones(img[:,:,0].shape)*212)))
		channel2 = np.logical_and(np.greater(img[:,:,1],(np.ones(img[:,:,0].shape)*30)),np.less(img[:,:,1],(np.ones(img[:,:,0].shape)*90)))
		channel3 = np.logical_and(np.greater(img[:,:,2],(np.ones(img[:,:,0].shape)*40)),np.less(img[:,:,2],(np.ones(img[:,:,0].shape)*100)))

		channels = np.logical_and(np.logical_and(channel1,channel2),channel3)

		img[:,:,0] = img[:,:,0] * np.logical_not(channels)
		img[:,:,1] = img[:,:,1] * np.logical_not(channels)
		img[:,:,2] = img[:,:,2] * np.logical_not(channels)
		
		img[:,:,0] += base_img[:,:,0] * (channels)
		img[:,:,1] += base_img[:,:,1] * (channels)
		img[:,:,2] += base_img[:,:,2] * (channels)

		

		frame = img
		

		# print(col1)

	
	cv2.imshow("Frames", frame)
	out.write(frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# # Save the dataset in filesystem
# np.save(dataset_path + file_name, face_data)
# print("Dataset saved at: {}".format(dataset_path + file_name + '.npy'))

cap.release()
cv2.destroyAllWindows()





