
import argparse
import cv2
import os

def main():
    parser = argparse.ArgumentParser(description="Read an image and convert to grayscale.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--output", default="program1_gray.jpg", help="Output grayscale image path")
    args = parser.parse_args()

    img = cv2.imread(args.input)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(args.output, gray)
    print(f"Saved grayscale image to {args.output}")

if __name__ == '__main__':
    main()
