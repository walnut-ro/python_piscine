from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np

def rgb_to_grayscale(rgb_image: np.ndarray) -> np.ndarray:
    """
    Converts an RGB image to grayscale.

    Parameters:
    rgb_image (np.ndarray): Input RGB image.

    Returns:
    np.ndarray: Grayscale image.
    """
    grayscale_image = np.dot(rgb_image[...,:3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)
    return np.stack([grayscale_image], axis=-1)

def main():
    image_path = 'animal.jpeg'
    
    # Load the image
    image = ft_load(image_path)
    
    # Check if the image was successfully loaded
    if image.size == 0:
        return

    # Print image information
    print(f"The shape of image is: {image.shape}")
    print(image)
    
    # Perform zoom by slicing
    zoomed_image = image[100:500, 440:840]
    grayscale_zoomed_image = rgb_to_grayscale(zoomed_image)
    print(f"New shape after slicing: {grayscale_zoomed_image.shape} or ({grayscale_zoomed_image.shape[0]}, {grayscale_zoomed_image.shape[1]})")
    print(grayscale_zoomed_image)
#    print(f"New shape after slicing: {zoomed_image.shape}")
#    print(zoomed_image)
    
    # Display the original image
#    plt.figure()
#    plt.title('Original Image')
#    plt.imshow(image)
#    plt.xlabel('X axis')
#    plt.ylabel('Y axis')
#    plt.colorbar()
    
    # Display the zoomed image
    plt.figure()
    plt.title('Zoomed Image')
    plt.imshow(grayscale_zoomed_image, cmap="gray")
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.colorbar()
    
    plt.show()

if __name__ == "__main__":
    main()