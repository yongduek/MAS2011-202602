import cv2 as cv
import numpy as np

# Image size: width=600, height=400
width, height = 600, 400

# Create a white image (BGR: 255,255,255)
img = np.full((height, width, 3), 255, dtype=np.uint8)

# Change pixels to red (BGR: 0,0,255) one by one using a while loop
while True:
	cv.imshow("Result", img)

	# Refresh the window after each pixel update
	# Press q to stop early
	if cv.waitKey(1) & 0xFF == ord("q"):
		break

# Save and display the final image
filepath = "outputs/white_pixels.png"
cv.imwrite(filepath, img)
cv.destroyAllWindows()

