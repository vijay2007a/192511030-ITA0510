
import argparse
import cv2

def main():
    parser = argparse.ArgumentParser(description="Insert watermark text into an image.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--output", default="program26_watermark.jpg", help="Output image path")
    parser.add_argument("--text", default="Watermark", help="Watermark text")
    args = parser.parse_args()

    img = cv2.imread(args.input)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    overlay = img.copy()
    cv2.putText(overlay, args.text, (20, img.shape[0] - 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    output = cv2.addWeighted(overlay, 0.5, img, 0.5, 0)
    cv2.imwrite(args.output, output)
    print(f"Saved watermark image to {args.output}")

if __name__ == '__main__':
    main()
