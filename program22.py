
import argparse
import cv2
import numpy as np

def main():
    parser = argparse.ArgumentParser(description="Sharpen an image using Laplacian mask with positive center coefficient.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--output", default="program22_sharpen.jpg", help="Output image path")
    args = parser.parse_args()

    img = cv2.imread(args.input)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    kernel = np.array([[1, 1, 1], [1, -7, 1], [1, 1, 1]])
    sharpened = cv2.filter2D(img, -1, kernel)
    cv2.imwrite(args.output, sharpened)
    print(f"Saved sharpened image to {args.output}")

if __name__ == '__main__':
    main()
