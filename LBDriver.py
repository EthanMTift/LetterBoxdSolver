from LBExtremes import find_black_extremes
from LBBlackRectangle import draw_black_rectangle
from LBFillBlack import nonwhite_to_black
from LBOCR import ocr_white_on_black
from LBFlatten import flatten_ocr_output
from LBSolver import solve_letters
from LBSelect import select_file_qt
import cv2

img_path = select_file_qt()

image = cv2.imread(img_path)
extremes = find_black_extremes(image)
blackRect = draw_black_rectangle(image, extremes)
fullBlack = nonwhite_to_black(blackRect)
letters = ocr_white_on_black(fullBlack)
betterLetters = flatten_ocr_output(letters)
if betterLetters is not None:
    solve_letters(betterLetters)



