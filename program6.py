
import argparse
import cv2

def main():
    parser = argparse.ArgumentParser(description="Read a video and play it normal, slow, and fast.")
    parser.add_argument("--input", default="input.mp4", help="Input video path")
    args = parser.parse_args()

    cap = cv2.VideoCapture(args.input)
    if not cap.isOpened():
        raise SystemExit(f"Could not open video '{args.input}'")

    print("Press q to quit. Showing normal speed first.")
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('Normal Speed', frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    print("Showing slow motion. Press q to continue.")
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('Slow Motion', frame)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    print("Showing fast motion. Press q to quit.")
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('Fast Motion', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
