import cv2
import sys

def Capture_Event(event, x, y, flags, params):
	# If the left mouse button is pressed
	if event == cv2.EVENT_LBUTTONDOWN:
		# Print the coordinate of the 
		# clicked point
		print(f"({x}, {y})")

# The Main Function
if __name__=="__main__":
	# Read the Image.
	img = cv2.imread('ZONE_103.png', 1)
	# Show the Image
	cv2.imshow('image', img)
	# Set the Mouse Callback function, and call
	# the Capture_Event function.
	cv2.setMouseCallback('image', Capture_Event)
	# Press any key to exit
	cv2.waitKey(0)
	# Destroy all the windows
	cv2.destroyAllWindows()