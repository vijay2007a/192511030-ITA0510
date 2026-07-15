
import argparse
import cv2
import numpy as np

def main():
    parser = argparse.ArgumentParser(description="Detect image boundary with a convolution kernel.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--output", default="program28_boundary.jpg", help="Output image path")
    args = parser.parse_args()

    img = cv2.imread(args.input, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
    boundary = cv2.filter2D(img, -1, kernel)
    cv2.imwrite(args.output, boundary)
    print(f"Saved boundary image to {args.output}")

if __name__ == '__main__':
    main()
