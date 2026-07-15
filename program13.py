
import argparse
import cv2
import numpy as np

def main():
    parser = argparse.ArgumentParser(description="Perform perspective transformation on a video.")
    parser.add_argument("--input", default="input.mp4", help="Input video file")
    parser.add_argument("--output", default="program13_perspective.mp4", help="Output video file")
    args = parser.parse_args()

    cap = cv2.VideoCapture(args.input)
    if not cap.isOpened():
        raise SystemExit(f"Could not open video '{args.input}'")

    fps = cap.get(cv2.CAP_PROP_FPS) or 20.0
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(args.output, fourcc, fps, (width, height))

    src = np.float32([[0, 0], [width - 1, 0], [width - 1, height - 1], [0, height - 1]])
    dst = np.float32([[0, 0], [width * 0.9, height * 0.1], [width * 0.8, height * 0.9], [width * 0.2, height * 0.8]])
    M = cv2.getPerspectiveTransform(src, dst)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        warped = cv2.warpPerspective(frame, M, (width, height))
        out.write(warped)

    cap.release()
    out.release()
    print(f"Saved transformed video to {args.output}")

if __name__ == '__main__':
    main()
