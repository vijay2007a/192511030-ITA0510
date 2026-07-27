
import argparse
import cv2

def main():
    parser = argparse.ArgumentParser(description="Detect edges using the Canny method.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--output", default="program16_canny.jpg", help="Output edge image path")
    args = parser.parse_args()

    img = cv2.imread(args.input, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    edges = cv2.Canny(img, 100, 200)
    cv2.imwrite(args.output, edges)
    print(f"Saved edge image to {args.output}")

if __name__ == '__main__':
    main()
