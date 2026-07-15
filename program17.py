
import argparse
import cv2

def main():
    parser = argparse.ArgumentParser(description="Edge detection using Sobel matrix along X axis.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--output", default="program17_sobel_x.jpg", help="Output image path")
    args = parser.parse_args()

    img = cv2.imread(args.input, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobelx = cv2.convertScaleAbs(sobelx)
    cv2.imwrite(args.output, sobelx)
    print(f"Saved Sobel X image to {args.output}")

if __name__ == '__main__':
    main()
