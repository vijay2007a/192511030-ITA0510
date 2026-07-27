
import argparse
import cv2
import os

def main():
    parser = argparse.ArgumentParser(description="Read an image and apply Gaussian blur.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--output", default="program2_blur.jpg", help="Output blurred image path")
    parser.add_argument("--kernel", type=int, default=7, help="Gaussian kernel size (odd)")
    args = parser.parse_args()

    img = cv2.imread(args.input)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    k = args.kernel if args.kernel % 2 == 1 else args.kernel + 1
    blur = cv2.GaussianBlur(img, (k, k), 0)
    cv2.imwrite(args.output, blur)
    print(f"Saved blurred image to {args.output}")

if __name__ == '__main__':
    main()
