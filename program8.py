
import argparse
import cv2

def main():
    parser = argparse.ArgumentParser(description="Scale an image bigger and smaller.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--scale-up", type=float, default=1.5, help="Scale up factor")
    parser.add_argument("--scale-down", type=float, default=0.5, help="Scale down factor")
    args = parser.parse_args()

    img = cv2.imread(args.input)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    up = cv2.resize(img, None, fx=args.scale_up, fy=args.scale_up, interpolation=cv2.INTER_LINEAR)
    down = cv2.resize(img, None, fx=args.scale_down, fy=args.scale_down, interpolation=cv2.INTER_AREA)
    cv2.imwrite('program8_scale_up.jpg', up)
    cv2.imwrite('program8_scale_down.jpg', down)
    print('Saved program8_scale_up.jpg and program8_scale_down.jpg')

if __name__ == '__main__':
    main()
