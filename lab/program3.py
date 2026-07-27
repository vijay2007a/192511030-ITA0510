
import argparse
import cv2

def main():
    parser = argparse.ArgumentParser(description="Read an image and show edges with Canny.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--output", default="program3_canny.jpg", help="Output edge image path")
    parser.add_argument("--threshold1", type=int, default=100, help="First Canny threshold")
    parser.add_argument("--threshold2", type=int, default=200, help="Second Canny threshold")
    args = parser.parse_args()

    img = cv2.imread(args.input)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, args.threshold1, args.threshold2)
    cv2.imwrite(args.output, edges)
    print(f"Saved edge image to {args.output}")

if __name__ == '__main__':
    main()
