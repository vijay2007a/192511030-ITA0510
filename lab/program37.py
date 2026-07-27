
import argparse
import cv2

def main():
    parser = argparse.ArgumentParser(description="Play a video in reverse mode.")
    parser.add_argument("--input", default="input.mp4", help="Input video file")
    args = parser.parse_args()

    cap = cv2.VideoCapture(args.input)
    if not cap.isOpened():
        raise SystemExit(f"Could not open video '{args.input}'")

    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()
    for frame in reversed(frames):
        cv2.imshow('Reverse Video', frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
