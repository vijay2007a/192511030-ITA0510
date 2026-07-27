
import argparse
import cv2
import numpy as np

def main():
    parser = argparse.ArgumentParser(description="Perform morphological gradient.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--output", default="program33_gradient.jpg", help="Output image path")
    args = parser.parse_args()

    img = cv2.imread(args.input, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    kernel = np.ones((5, 5), np.uint8)
    gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
    cv2.imwrite(args.output, gradient)
    print(f"Saved morphological gradient image to {args.output}")

if __name__ == '__main__':
    main()
