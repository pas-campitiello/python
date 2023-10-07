import cv2
import numpy as np

def remove_watermark(image_path, output_path, threshold=220):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Threshold the image to create a binary image
    _, thresh = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY_INV)

    # Perform morphological operations to remove small noise
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
    
    # Inpainting
    inpainted = cv2.inpaint(image, opening, inpaintRadius=7, flags=cv2.INPAINT_TELEA)

    # Save the result
    cv2.imwrite(output_path, inpainted)
    print(f"Saved to {output_path}")

image_path = "LICA14808.jpeg"
output_path = "LICA14808_cleaned_image.jpeg"
remove_watermark(image_path, output_path)
