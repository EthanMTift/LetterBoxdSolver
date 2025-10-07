import cv2
import numpy as np

def nonwhite_to_black(img, white_threshold=200):
    """
    Converts all non-white pixels in the image to black.

    Parameters:
        img (np.ndarray): Input image (grayscale or color).
        white_threshold (int): Minimum value for a pixel to be considered white (0–255).

    Returns:
        np.ndarray: Processed image where non-white pixels are black.
    """
    # Make a copy so original isn't modified
    result = img.copy()

    # If the image is color, check all channels
    if len(result.shape) == 3:
        # Create a mask of "white" pixels
        white_mask = np.all(result >= white_threshold, axis=2)
        # Everything that is not white becomes black
        result[~white_mask] = [0, 0, 0]
    else:
        # Grayscale: everything below threshold becomes black
        result[result < white_threshold] = 0
        # Everything white stays as is (optional, can also force pure white)
        result[result >= white_threshold] = 255

    return result
