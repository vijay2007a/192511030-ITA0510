
import argparse
import cv2

def rotate(img, angle):
    h, w = img.shape[:2]
    matrix = cv2.getRotationMatrix2D((w / 2, h / 2), angle, 1)
    return cv2.warpAffine(img, matrix, (w, h))

def main():
    parser = argparse.ArgumentParser(description="Rotate an image clockwise and counterclockwise.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    args = parser.parse_args()

    img = cv2.imread(args.input)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    cw = rotate(img, -45)
    ccw = rotate(img, 45)
    cv2.imwrite('program9_rotate_cw.jpg', cw)
    cv2.imwrite('program9_rotate_ccw.jpg', ccw)
    print('Saved program9_rotate_cw.jpg and program9_rotate_ccw.jpg')

if __name__ == '__main__':
    main()
