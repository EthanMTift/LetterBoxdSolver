import cv2

def draw_black_rectangle(image, extremes):
    """
    Draws a black box on the image using the given extreme coordinates.

    Parameters:
        image (numpy.ndarray): The input image (color or grayscale).
        extremes (dict): Dictionary with 'leftmost', 'rightmost', 'topmost', 'bottommost' coordinates.
        thickness (int): Thickness of the rectangle border. Use -1 to fill the rectangle.

    Returns:
        numpy.ndarray: Image with the rectangle drawn.
    """
    if extremes is None:
        raise ValueError("Extremes dictionary is None or empty.")
    
    print(extremes)

    # Extract border values
    left_x = extremes['leftmost'][0]
    right_x = extremes['rightmost'][0]
    top_y = extremes['topmost'][1]
    bottom_y = extremes['bottommost'][1]

    # Make a copy so the original isn’t modified
    img_copy = image.copy()

    # Draw the rectangle (in black, BGR = (0, 0, 0))
    cv2.rectangle(img_copy, (left_x, top_y), (right_x, bottom_y), (0, 0, 0), -1)

    return img_copy
