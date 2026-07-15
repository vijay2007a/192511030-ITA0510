
import argparse
import cv2

def main():
    parser = argparse.ArgumentParser(description="Crop, copy, and paste one image inside another.")
    parser.add_argument("--base", default="input.jpg", help="Base image path")
    parser.add_argument("--patch", default="input.jpg", help="Patch image path")
    parser.add_argument("--output", default="program27_paste.jpg", help="Output image path")
    args = parser.parse_args()

    base = cv2.imread(args.base)
    patch = cv2.imread(args.patch)
    if base is None or patch is None:
        raise SystemExit("Could not load both base and patch images")

    h, w = patch.shape[:2]
    crop = base[0:h, 0:w].copy()
    base[0:h, 0:w] = patch
    cv2.imwrite(args.output, base)
    cv2.imwrite('program27_crop.jpg', crop)
    print(f"Saved pasted image to {args.output} and crop to program27_crop.jpg")

if __name__ == '__main__':
    main()
