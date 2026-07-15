
import argparse
import cv2

def main():
    parser = argparse.ArgumentParser(description="Edge detection using Sobel matrix along both X and Y axes.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--output", default="program19_sobel_xy.jpg", help="Output image path")
    args = parser.parse_args()

    img = cv2.imread(args.input, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    sobel = cv2.magnitude(sobelx, sobely)
    sobel = cv2.convertScaleAbs(sobel)
    cv2.imwrite(args.output, sobel)
    print(f"Saved Sobel XY image to {args.output}")

if __name__ == '__main__':
    main()
