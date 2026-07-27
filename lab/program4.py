
import argparse
import cv2
import numpy as np

def main():
    parser = argparse.ArgumentParser(description="Read an image and dilate it.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--output", default="program4_dilate.jpg", help="Output image path")
    parser.add_argument("--kernel-size", type=int, default=5, help="Structuring element size")
    args = parser.parse_args()

    img = cv2.imread(args.input, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    kernel = np.ones((args.kernel_size, args.kernel_size), np.uint8)
    dilated = cv2.dilate(img, kernel, iterations=1)
    cv2.imwrite(args.output, dilated)
    print(f"Saved dilated image to {args.output}")

if __name__ == '__main__':
    main()
