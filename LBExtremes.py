import cv2
import numpy as np

def find_black_extremes(img, threshold=20):
    """
    Finds the black pixels that are farthest left, right, top, and bottom in the given image.
    
    Parameters:
        image_path (str): Path to the image file.
        threshold (int): Max brightness for a pixel to count as "black" (0–255).
    
    Returns:
        dict: Coordinates of the extreme black pixels (top, bottom, left, right).
    """
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Find pixels that are "black" (brightness below threshold)
    black_mask = img < threshold
    
    
    # Get coordinates of black pixels
    y_coords, x_coords = np.where(black_mask)
    if len(x_coords) == 0:
        print("No black pixels found.")
        return None
    
    # Find extremes
    leftmost_idx = np.argmin(x_coords)
    rightmost_idx = np.argmax(x_coords)
    topmost_idx = np.argmin(y_coords)
    bottommost_idx = np.argmax(y_coords)
    
    extremes = {
        "leftmost": (x_coords[leftmost_idx], y_coords[leftmost_idx]),
        "rightmost": (x_coords[rightmost_idx], y_coords[rightmost_idx]),
        "topmost": (x_coords[topmost_idx], y_coords[topmost_idx]),
        "bottommost": (x_coords[bottommost_idx], y_coords[bottommost_idx]),
    }
    
    return extremes