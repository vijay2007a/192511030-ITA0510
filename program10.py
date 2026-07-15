
import argparse
import cv2
import numpy as np

def main():
    parser = argparse.ArgumentParser(description="Translate an image from one place to another.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--dx", type=int, default=100, help="Shift along x")
    parser.add_argument("--dy", type=int, default=50, help="Shift along y")
    args = parser.parse_args()

    img = cv2.imread(args.input)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    rows, cols = img.shape[:2]
    matrix = np.float32([[1, 0, args.dx], [0, 1, args.dy]])
    moved = cv2.warpAffine(img, matrix, (cols, rows))
    cv2.imwrite('program10_translated.jpg', moved)
    print('Saved program10_translated.jpg')

if __name__ == '__main__':
    main()
