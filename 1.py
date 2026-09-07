import cv2 as cv
import numpy as np

# Image size: width=600, height=400
width, height = 600, 400

# Create a white image (BGR: 255,255,255)
img = np.full((height, width, 3), 255, dtype=np.uint8)

x = 0
y = 0

# Change pixels to red (BGR: 0,0,255) one by one using a while loop
while y < height:
	img[y, x] = (0, 0, 255)
	cv.imshow("Result", img)

	# Refresh the window after each pixel update
	# Press q to stop early
	if cv.waitKey(1) & 0xFF == ord("q"):
		break

	x += 1
	if x == width:
		x = 0
		y += 1

# Save and display the final image
filepath = "outputs/red_pixels.png"
cv.imwrite(filepath, img)
cv.imshow("Result", img)
cv.waitKey(0)
cv.destroyAllWindows()

