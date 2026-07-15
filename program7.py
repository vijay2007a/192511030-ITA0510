
import argparse
import cv2

def main():
    parser = argparse.ArgumentParser(description="Capture webcam video and display slow/fast motion.")
    parser.add_argument("--device", type=int, default=0, help="Camera device index")
    args = parser.parse_args()

    cap = cv2.VideoCapture(args.device)
    if not cap.isOpened():
        raise SystemExit(f"Could not open webcam device {args.device}")

    print("Press q to quit. Displaying normal fps.")
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('Webcam Normal', frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    print("Displaying slow motion. Press q to quit.")
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('Webcam Slow', frame)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    print("Displaying fast motion. Press q to quit.")
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('Webcam Fast', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
