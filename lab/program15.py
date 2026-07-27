
import argparse
import cv2
import numpy as np

def main():
    parser = argparse.ArgumentParser(description="Apply Direct Linear Transformation style perspective transform.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    args = parser.parse_args()

    img = cv2.imread(args.input)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    rows, cols = img.shape[:2]
    src = np.float32([[0, 0], [cols - 1, 0], [cols - 1, rows - 1], [0, rows - 1]])
    dst = np.float32([[cols * 0.0, rows * 0.1], [cols * 0.85, rows * 0.05], [cols * 0.9, rows * 0.95], [cols * 0.1, rows * 0.9]])
    M = cv2.getPerspectiveTransform(src, dst)
    dlt = cv2.warpPerspective(img, M, (cols, rows))
    cv2.imwrite('program15_dlt.jpg', dlt)
    print('Saved program15_dlt.jpg')

if __name__ == '__main__':
    main()
