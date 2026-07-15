
import argparse
import cv2
import numpy as np

def main():
    parser = argparse.ArgumentParser(description="Perform morphological opening.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--output", default="program31_opening.jpg", help="Output image path")
    args = parser.parse_args()

    img = cv2.imread(args.input, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    kernel = np.ones((5, 5), np.uint8)
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    cv2.imwrite(args.output, opening)
    print(f"Saved opening image to {args.output}")

if __name__ == '__main__':
    main()
