
import argparse
import cv2
import numpy as np

def main():
    parser = argparse.ArgumentParser(description="Perform black hat morphological operation.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--output", default="program35_blackhat.jpg", help="Output image path")
    args = parser.parse_args()

    img = cv2.imread(args.input, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    kernel = np.ones((5, 5), np.uint8)
    blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
    cv2.imwrite(args.output, blackhat)
    print(f"Saved black hat image to {args.output}")

if __name__ == '__main__':
    main()
