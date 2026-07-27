
import argparse
import cv2

def main():
    parser = argparse.ArgumentParser(description="Sharpen an image using unsharp masking.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--output", default="program23_unsharp.jpg", help="Output image path")
    args = parser.parse_args()

    img = cv2.imread(args.input)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    blurred = cv2.GaussianBlur(img, (9, 9), 10.0)
    unsharp = cv2.addWeighted(img, 1.5, blurred, -0.5, 0)
    cv2.imwrite(args.output, unsharp)
    print(f"Saved unsharp masked image to {args.output}")

if __name__ == '__main__':
    main()
