import cv2
import pytesseract

def ocr_white_on_black(img):
    """
    Extracts text from an image where letters are white on a black background.

    Parameters:
        img (np.ndarray): Input image (color or grayscale).

    Returns:
        str: Detected text.
    """
    # Convert to grayscale if needed
    if len(img.shape) == 3:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = img.copy()

    # Invert image so letters are black on white (Tesseract works better this way)
    inverted = cv2.bitwise_not(gray)

    # Optional: threshold to binary for sharper OCR
    _, thresh = cv2.threshold(inverted, 127, 255, cv2.THRESH_BINARY)

    # Run OCR
    tesseract_config = r'-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 6'
    text = pytesseract.image_to_string(thresh, config=tesseract_config)  # PSM 6 = Assume a uniform block of text
    return text.strip()
