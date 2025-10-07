def flatten_ocr_output(text):
    """
    Flattens OCR text by removing newlines and keeping all letters separated by spaces.

    Example:
        Input:  "W F I\nH N\nE C\nM Y\nG T A"
        Output: "W F I H N E C M Y G T A"
    """
    # Split on any whitespace (spaces, tabs, newlines) and filter out empty strings
    tokens = text.split()
    if len(tokens) == 12:
        # Join back with single spaces
        flattened = ' '.join(tokens)
        return flattened
    else:
        print("Failed to detect exactly 12 letters")