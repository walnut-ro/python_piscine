#import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import os



def ft_load(path: str) -> np.ndarray:
    """
    Loads an image from the specified path and returns its pixel content as a NumPy array.
    Prints the image format and its dimensions. Handles JPG and JPEG formats.

    Parameters:
    path (str): Path to the image file.

    Returns:
    np.ndarray: NumPy array containing the pixel data of the image.
    """
    # Check if file exists
    if not os.path.exists(path):
        print(f"Error: The file '{path}' does not exist.")
        return np.array([])  # Return an empty array to indicate failure
    
    # Try to load the image
    try:
        img = mpimg.imread(path)
    except Exception as e:
        print(f"Error: Unable to load the image. {e}")
        return np.array([])  # Return an empty array to indicate failure
    
    # Check if the image format is supported
    if not path.lower().endswith(('.jpg', '.jpeg')):
        print(f"Error: Unsupported file format. Please use JPG or JPEG images.")
        return np.array([])  # Return an empty array to indicate failure
    
    # Print image format and dimensions
    print(f"Image format: {path.split('.')[-1].upper()}")
    print(f"Image dimensions: {img.shape}")
    
    # If the image is grayscale, convert it to RGB
    #if len(img.shape) == 2:  # Grayscale image
    #    img = np.stack((img,) * 3, axis=-1)  # Convert to RGB by stacking
    #elif img.shape[2] == 4:  # Image with alpha channel
    #    img = img[:, :, :3]  # Discard the alpha channel
    
    # Display the image using matplotlib
    #plt.imshow(img)
    #plt.axis('off')  # Hide axes
    #plt.show()
    
    return img
