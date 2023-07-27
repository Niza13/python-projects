import cv2

def flip_image_horizontal(image_path, output_path):
    # Read the image from the specified file path
    image = cv2.imread(image_path)

    # Check if the image is loaded successfully
    if image is None:
        print("Error: Unable to load the image.")
        return

    # Flip the image horizontally
    flipped_image = cv2.flip(image, 1)

    # Save the flipped image to the specified output path
    cv2.imwrite(output_path, flipped_image)

if __name__ == "__main__":
    # Replace 'input_image.jpg' with the path to your input image
    input_image_path = "try.png"
    
    # Replace 'output_image_flipped.jpg' with the desired filename for the flipped image
    output_image_path = "try.png"

    flip_image_horizontal(input_image_path, output_image_path)
