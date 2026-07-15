
import argparse
import cv2
import numpy as np

def main():
    parser = argparse.ArgumentParser(description="Perform affine transformation on an image.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    args = parser.parse_args()

    img = cv2.imread(args.input)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    rows, cols = img.shape[:2]
    src_points = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1]])
    dst_points = np.float32([[0, rows * 0.33], [cols * 0.85, rows * 0.25], [cols * 0.15, rows * 0.7]])
    M = cv2.getAffineTransform(src_points, dst_points)
    transformed = cv2.warpAffine(img, M, (cols, rows))
    cv2.imwrite('program11_affine.jpg', transformed)
    print('Saved program11_affine.jpg')

if __name__ == '__main__':
    main()
