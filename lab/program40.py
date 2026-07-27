
import argparse
import cv2

def main():
    parser = argparse.ArgumentParser(description="Draw a rectangle and extract the object inside it.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--output", default="program40_object.jpg", help="Output image path")
    args = parser.parse_args()

    img = cv2.imread(args.input)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    h, w = img.shape[:2]
    x1, y1 = int(w * 0.2), int(h * 0.2)
    x2, y2 = int(w * 0.8), int(h * 0.8)
    cropped = img[y1:y2, x1:x2]
    cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
    cv2.imwrite(args.output, cropped)
    cv2.imwrite('program40_rectangle.jpg', img)
    print(f"Saved extracted object to {args.output} and annotation to program40_rectangle.jpg")

if __name__ == '__main__':
    main()
