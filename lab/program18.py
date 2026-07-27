
import argparse
import cv2

def main():
    parser = argparse.ArgumentParser(description="Edge detection using Sobel matrix along Y axis.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--output", default="program18_sobel_y.jpg", help="Output image path")
    args = parser.parse_args()

    img = cv2.imread(args.input, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    sobely = cv2.convertScaleAbs(sobely)
    cv2.imwrite(args.output, sobely)
    print(f"Saved Sobel Y image to {args.output}")

if __name__ == '__main__':
    main()
