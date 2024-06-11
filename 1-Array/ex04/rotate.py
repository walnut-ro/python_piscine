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

def transpose_image(grayscale_zoomed_image: np.ndarray) -> np.ndarray:
    """
    Transposes the given grayscale image.

    Parameters:
    grayscale_zoomed_image (np.ndarray): Input grayscale image.

    Returns:
    np.ndarray: Transposed grayscale image.
    """
    height, width, channels = grayscale_zoomed_image.shape
    transposed_image = np.zeros((width, height, channels), dtype=grayscale_zoomed_image.dtype)
    
    for i in range(height):
        for j in range(width):
            for k in range(channels):
                transposed_image[j, i, k] = grayscale_zoomed_image[i, j, k]

    return transposed_image

def main():
    image_path = 'animal.jpeg'
    
    # Load the image
    image = ft_load(image_path)
    
    # Check if the image was successfully loaded
    if image.size == 0:
        return

    # Print image information
 #   print(f"The shape of image is: {image.shape}")
 #   print(image)
    
    # Perform zoom by slicing
    zoomed_image = image[100:500, 440:840]
    grayscale_zoomed_image = rgb_to_grayscale(zoomed_image)
    print(f"The shape of image is: {grayscale_zoomed_image.shape} or ({grayscale_zoomed_image.shape[0]}, {grayscale_zoomed_image.shape[1]})")
    print(grayscale_zoomed_image)
    
    # Transpose the grayscale zoomed image
    transposed_image = transpose_image(grayscale_zoomed_image)
    print(f"New shape after transposing: {transposed_image.shape} or ({transposed_image.shape[0]}, {transposed_image.shape[1]})")
    print(transposed_image)
    
    # Display the zoomed grayed and transposed image
    plt.figure()
    plt.title('Zoomed and Transposed Image')
    plt.imshow(transposed_image, cmap="gray")
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.colorbar()
    
    plt.show()

if __name__ == "__main__":
    main()