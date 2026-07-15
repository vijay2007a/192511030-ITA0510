
import argparse
import cv2

def main():
    parser = argparse.ArgumentParser(description="Sharpen an image using high-boost mask.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--output", default="program24_highboost.jpg", help="Output image path")
    parser.add_argument("--weight", type=float, default=1.5, help="High boost weight")
    args = parser.parse_args()

    img = cv2.imread(args.input)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    blurred = cv2.GaussianBlur(img, (9, 9), 10.0)
    mask = cv2.subtract(img, blurred)
    high_boost = cv2.addWeighted(img, args.weight, mask, 1.0, 0)
    cv2.imwrite(args.output, high_boost)
    print(f"Saved high-boost image to {args.output}")

if __name__ == '__main__':
    main()
