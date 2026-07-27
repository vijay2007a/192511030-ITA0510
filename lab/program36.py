
import argparse
import cv2

def main():
    parser = argparse.ArgumentParser(description="Recognize a watch in an image using ORB feature matching.")
    parser.add_argument("--input", default="input.jpg", help="Scene image path")
    parser.add_argument("--template", default="watch_template.jpg", help="Watch template image path")
    parser.add_argument("--output", default="program36_watch_match.jpg", help="Output image path")
    args = parser.parse_args()

    img = cv2.imread(args.input)
    template = cv2.imread(args.template)
    if img is None or template is None:
        raise SystemExit("Could not load both scene and template images")

    orb = cv2.ORB_create(500)
    kp1, des1 = orb.detectAndCompute(template, None)
    kp2, des2 = orb.detectAndCompute(img, None)
    if des1 is None or des2 is None:
        raise SystemExit("Could not compute ORB descriptors")

    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = matcher.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)[:30]
    matched = cv2.drawMatches(template, kp1, img, kp2, matches, None, flags=2)
    cv2.imwrite(args.output, matched)
    print(f"Saved watch match visualization to {args.output}")

if __name__ == '__main__':
    main()
