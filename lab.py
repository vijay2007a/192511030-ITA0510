\n# ===== program1.py =====

import argparse
import cv2
import os

def main():
    parser = argparse.ArgumentParser(description="Read an image and convert to grayscale.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--output", default="program1_gray.jpg", help="Output grayscale image path")
    args = parser.parse_args()

    img = cv2.imread(args.input)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(args.output, gray)
    print(f"Saved grayscale image to {args.output}")

if __name__ == '__main__':
    main()
\n# ===== program10.py =====

import argparse
import cv2
import numpy as np

def main():
    parser = argparse.ArgumentParser(description="Translate an image from one place to another.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--dx", type=int, default=100, help="Shift along x")
    parser.add_argument("--dy", type=int, default=50, help="Shift along y")
    args = parser.parse_args()

    img = cv2.imread(args.input)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    rows, cols = img.shape[:2]
    matrix = np.float32([[1, 0, args.dx], [0, 1, args.dy]])
    moved = cv2.warpAffine(img, matrix, (cols, rows))
    cv2.imwrite('program10_translated.jpg', moved)
    print('Saved program10_translated.jpg')

if __name__ == '__main__':
    main()
\n# ===== program11.py =====

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
\n# ===== program12.py =====

import argparse
import cv2
import numpy as np

def main():
    parser = argparse.ArgumentParser(description="Perform perspective transformation on an image.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    args = parser.parse_args()

    img = cv2.imread(args.input)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    rows, cols = img.shape[:2]
    src = np.float32([[0, 0], [cols - 1, 0], [cols - 1, rows - 1], [0, rows - 1]])
    dst = np.float32([[0, 0], [cols * 0.9, rows * 0.1], [cols * 0.8, rows * 0.9], [cols * 0.2, rows * 0.8]])
    M = cv2.getPerspectiveTransform(src, dst)
    warped = cv2.warpPerspective(img, M, (cols, rows))
    cv2.imwrite('program12_perspective.jpg', warped)
    print('Saved program12_perspective.jpg')

if __name__ == '__main__':
    main()
\n# ===== program13.py =====

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
\n# ===== program14.py =====

import argparse
import cv2
import numpy as np

def main():
    parser = argparse.ArgumentParser(description="Apply a homography transformation to an image.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    args = parser.parse_args()

    img = cv2.imread(args.input)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    rows, cols = img.shape[:2]
    src = np.float32([[0, 0], [cols - 1, 0], [cols - 1, rows - 1], [0, rows - 1]])
    dst = np.float32([[cols * 0.05, rows * 0.33], [cols * 0.95, rows * 0.1], [cols * 0.8, rows * 0.9], [cols * 0.2, rows * 0.8]])
    H, _ = cv2.findHomography(src, dst)
    warped = cv2.warpPerspective(img, H, (cols, rows))
    cv2.imwrite('program14_homography.jpg', warped)
    print('Saved program14_homography.jpg')

if __name__ == '__main__':
    main()
\n# ===== program15.py =====

import argparse
import cv2
import numpy as np

def main():
    parser = argparse.ArgumentParser(description="Apply Direct Linear Transformation style perspective transform.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    args = parser.parse_args()

    img = cv2.imread(args.input)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    rows, cols = img.shape[:2]
    src = np.float32([[0, 0], [cols - 1, 0], [cols - 1, rows - 1], [0, rows - 1]])
    dst = np.float32([[cols * 0.0, rows * 0.1], [cols * 0.85, rows * 0.05], [cols * 0.9, rows * 0.95], [cols * 0.1, rows * 0.9]])
    M = cv2.getPerspectiveTransform(src, dst)
    dlt = cv2.warpPerspective(img, M, (cols, rows))
    cv2.imwrite('program15_dlt.jpg', dlt)
    print('Saved program15_dlt.jpg')

if __name__ == '__main__':
    main()
\n# ===== program16.py =====

import argparse
import cv2

def main():
    parser = argparse.ArgumentParser(description="Detect edges using the Canny method.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--output", default="program16_canny.jpg", help="Output edge image path")
    args = parser.parse_args()

    img = cv2.imread(args.input, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    edges = cv2.Canny(img, 100, 200)
    cv2.imwrite(args.output, edges)
    print(f"Saved edge image to {args.output}")

if __name__ == '__main__':
    main()
\n# ===== program17.py =====

import argparse
import cv2

def main():
    parser = argparse.ArgumentParser(description="Edge detection using Sobel matrix along X axis.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--output", default="program17_sobel_x.jpg", help="Output image path")
    args = parser.parse_args()

    img = cv2.imread(args.input, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobelx = cv2.convertScaleAbs(sobelx)
    cv2.imwrite(args.output, sobelx)
    print(f"Saved Sobel X image to {args.output}")

if __name__ == '__main__':
    main()
\n# ===== program18.py =====

import argparse
import cv2

def main():
    parser = argparse.ArgumentParser(description="Edge detection using Sobel matrix along Y axis.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--output", default="program18_sobel_y.jpg", help="Output image path")
    args = parser.parse_args()

    img = cv2.imread(args.input, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    sobely = cv2.convertScaleAbs(sobely)
    cv2.imwrite(args.output, sobely)
    print(f"Saved Sobel Y image to {args.output}")

if __name__ == '__main__':
    main()
\n# ===== program19.py =====

import argparse
import cv2

def main():
    parser = argparse.ArgumentParser(description="Edge detection using Sobel matrix along both X and Y axes.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--output", default="program19_sobel_xy.jpg", help="Output image path")
    args = parser.parse_args()

    img = cv2.imread(args.input, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    sobel = cv2.magnitude(sobelx, sobely)
    sobel = cv2.convertScaleAbs(sobel)
    cv2.imwrite(args.output, sobel)
    print(f"Saved Sobel XY image to {args.output}")

if __name__ == '__main__':
    main()
\n# ===== program2.py =====

import argparse
import cv2
import os

def main():
    parser = argparse.ArgumentParser(description="Read an image and apply Gaussian blur.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--output", default="program2_blur.jpg", help="Output blurred image path")
    parser.add_argument("--kernel", type=int, default=7, help="Gaussian kernel size (odd)")
    args = parser.parse_args()

    img = cv2.imread(args.input)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    k = args.kernel if args.kernel % 2 == 1 else args.kernel + 1
    blur = cv2.GaussianBlur(img, (k, k), 0)
    cv2.imwrite(args.output, blur)
    print(f"Saved blurred image to {args.output}")

if __name__ == '__main__':
    main()
\n# ===== program20.py =====

import argparse
import cv2
import numpy as np

def main():
    parser = argparse.ArgumentParser(description="Sharpen an image using Laplacian mask with negative center coefficient.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--output", default="program20_sharpen.jpg", help="Output image path")
    args = parser.parse_args()

    img = cv2.imread(args.input)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    sharpened = cv2.filter2D(img, -1, kernel)
    cv2.imwrite(args.output, sharpened)
    print(f"Saved sharpened image to {args.output}")

if __name__ == '__main__':
    main()
\n# ===== program21.py =====

import argparse
import cv2
import numpy as np

def main():
    parser = argparse.ArgumentParser(description="Sharpen an image using Laplacian mask with diagonal neighbors extension.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--output", default="program21_sharpen.jpg", help="Output image path")
    args = parser.parse_args()

    img = cv2.imread(args.input)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    sharpened = cv2.filter2D(img, -1, kernel)
    cv2.imwrite(args.output, sharpened)
    print(f"Saved sharpened image to {args.output}")

if __name__ == '__main__':
    main()
\n# ===== program22.py =====

import argparse
import cv2
import numpy as np

def main():
    parser = argparse.ArgumentParser(description="Sharpen an image using Laplacian mask with positive center coefficient.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--output", default="program22_sharpen.jpg", help="Output image path")
    args = parser.parse_args()

    img = cv2.imread(args.input)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    kernel = np.array([[1, 1, 1], [1, -7, 1], [1, 1, 1]])
    sharpened = cv2.filter2D(img, -1, kernel)
    cv2.imwrite(args.output, sharpened)
    print(f"Saved sharpened image to {args.output}")

if __name__ == '__main__':
    main()
\n# ===== program23.py =====

import argparse
import cv2

def main():
    parser = argparse.ArgumentParser(description="Sharpen an image using unsharp masking.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--output", default="program23_unsharp.jpg", help="Output image path")
    args = parser.parse_args()

    img = cv2.imread(args.input)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    blurred = cv2.GaussianBlur(img, (9, 9), 10.0)
    unsharp = cv2.addWeighted(img, 1.5, blurred, -0.5, 0)
    cv2.imwrite(args.output, unsharp)
    print(f"Saved unsharp masked image to {args.output}")

if __name__ == '__main__':
    main()
\n# ===== program24.py =====

import argparse
import cv2

def main():
    parser = argparse.ArgumentParser(description="Sharpen an image using high-boost mask.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--output", default="program24_highboost.jpg", help="Output image path")
    parser.add_argument("--weight", type=float, default=1.5, help="High boost weight")
    args = parser.parse_args()

    img = cv2.imread(args.input)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    blurred = cv2.GaussianBlur(img, (9, 9), 10.0)
    mask = cv2.subtract(img, blurred)
    high_boost = cv2.addWeighted(img, args.weight, mask, 1.0, 0)
    cv2.imwrite(args.output, high_boost)
    print(f"Saved high-boost image to {args.output}")

if __name__ == '__main__':
    main()
\n# ===== program25.py =====

import argparse
import cv2
import numpy as np

def main():
    parser = argparse.ArgumentParser(description="Sharpen an image using gradient masking.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--output", default="program25_gradient.jpg", help="Output image path")
    args = parser.parse_args()

    img = cv2.imread(args.input, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    kernel = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    gradient = cv2.filter2D(img, -1, kernel)
    cv2.imwrite(args.output, gradient)
    print(f"Saved gradient image to {args.output}")

if __name__ == '__main__':
    main()
\n# ===== program26.py =====

import argparse
import cv2

def main():
    parser = argparse.ArgumentParser(description="Insert watermark text into an image.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--output", default="program26_watermark.jpg", help="Output image path")
    parser.add_argument("--text", default="Watermark", help="Watermark text")
    args = parser.parse_args()

    img = cv2.imread(args.input)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    overlay = img.copy()
    cv2.putText(overlay, args.text, (20, img.shape[0] - 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    output = cv2.addWeighted(overlay, 0.5, img, 0.5, 0)
    cv2.imwrite(args.output, output)
    print(f"Saved watermark image to {args.output}")

if __name__ == '__main__':
    main()
\n# ===== program27.py =====

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
\n# ===== program28.py =====

import argparse
import cv2
import numpy as np

def main():
    parser = argparse.ArgumentParser(description="Detect image boundary with a convolution kernel.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--output", default="program28_boundary.jpg", help="Output image path")
    args = parser.parse_args()

    img = cv2.imread(args.input, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
    boundary = cv2.filter2D(img, -1, kernel)
    cv2.imwrite(args.output, boundary)
    print(f"Saved boundary image to {args.output}")

if __name__ == '__main__':
    main()
\n# ===== program29.py =====

import argparse
import cv2
import numpy as np

def main():
    parser = argparse.ArgumentParser(description="Perform morphological erosion.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--output", default="program29_erode.jpg", help="Output image path")
    args = parser.parse_args()

    img = cv2.imread(args.input, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    kernel = np.ones((5, 5), np.uint8)
    eroded = cv2.erode(img, kernel, iterations=1)
    cv2.imwrite(args.output, eroded)
    print(f"Saved eroded image to {args.output}")

if __name__ == '__main__':
    main()
\n# ===== program3.py =====

import argparse
import cv2

def main():
    parser = argparse.ArgumentParser(description="Read an image and show edges with Canny.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--output", default="program3_canny.jpg", help="Output edge image path")
    parser.add_argument("--threshold1", type=int, default=100, help="First Canny threshold")
    parser.add_argument("--threshold2", type=int, default=200, help="Second Canny threshold")
    args = parser.parse_args()

    img = cv2.imread(args.input)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, args.threshold1, args.threshold2)
    cv2.imwrite(args.output, edges)
    print(f"Saved edge image to {args.output}")

if __name__ == '__main__':
    main()
\n# ===== program30.py =====

import argparse
import cv2
import numpy as np

def main():
    parser = argparse.ArgumentParser(description="Perform morphological dilation.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--output", default="program30_dilate.jpg", help="Output image path")
    args = parser.parse_args()

    img = cv2.imread(args.input, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    kernel = np.ones((5, 5), np.uint8)
    dilated = cv2.dilate(img, kernel, iterations=1)
    cv2.imwrite(args.output, dilated)
    print(f"Saved dilated image to {args.output}")

if __name__ == '__main__':
    main()
\n# ===== program31.py =====

import argparse
import cv2
import numpy as np

def main():
    parser = argparse.ArgumentParser(description="Perform morphological opening.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--output", default="program31_opening.jpg", help="Output image path")
    args = parser.parse_args()

    img = cv2.imread(args.input, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    kernel = np.ones((5, 5), np.uint8)
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    cv2.imwrite(args.output, opening)
    print(f"Saved opening image to {args.output}")

if __name__ == '__main__':
    main()
\n# ===== program32.py =====

import argparse
import cv2
import numpy as np

def main():
    parser = argparse.ArgumentParser(description="Perform morphological closing.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--output", default="program32_closing.jpg", help="Output image path")
    args = parser.parse_args()

    img = cv2.imread(args.input, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    kernel = np.ones((5, 5), np.uint8)
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    cv2.imwrite(args.output, closing)
    print(f"Saved closing image to {args.output}")

if __name__ == '__main__':
    main()
\n# ===== program33.py =====

import argparse
import cv2
import numpy as np

def main():
    parser = argparse.ArgumentParser(description="Perform morphological gradient.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--output", default="program33_gradient.jpg", help="Output image path")
    args = parser.parse_args()

    img = cv2.imread(args.input, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    kernel = np.ones((5, 5), np.uint8)
    gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
    cv2.imwrite(args.output, gradient)
    print(f"Saved morphological gradient image to {args.output}")

if __name__ == '__main__':
    main()
\n# ===== program34.py =====

import argparse
import cv2
import numpy as np

def main():
    parser = argparse.ArgumentParser(description="Perform top hat morphological operation.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--output", default="program34_tophat.jpg", help="Output image path")
    args = parser.parse_args()

    img = cv2.imread(args.input, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    kernel = np.ones((5, 5), np.uint8)
    tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
    cv2.imwrite(args.output, tophat)
    print(f"Saved top hat image to {args.output}")

if __name__ == '__main__':
    main()
\n# ===== program35.py =====

import argparse
import cv2
import numpy as np

def main():
    parser = argparse.ArgumentParser(description="Perform black hat morphological operation.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--output", default="program35_blackhat.jpg", help="Output image path")
    args = parser.parse_args()

    img = cv2.imread(args.input, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    kernel = np.ones((5, 5), np.uint8)
    blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
    cv2.imwrite(args.output, blackhat)
    print(f"Saved black hat image to {args.output}")

if __name__ == '__main__':
    main()
\n# ===== program36.py =====

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
\n# ===== program37.py =====

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
\n# ===== program38.py =====

import argparse
import cv2

def main():
    parser = argparse.ArgumentParser(description="Detect faces in an image.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--output", default="program38_faces.jpg", help="Output image path")
    args = parser.parse_args()

    img = cv2.imread(args.input)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imwrite(args.output, img)
    print(f"Saved face detection image to {args.output}")

if __name__ == '__main__':
    main()
\n# ===== program39.py =====

import argparse
import cv2

def main():
    parser = argparse.ArgumentParser(description="Detect moving vehicles in a video frame using background subtraction.")
    parser.add_argument("--input", default="input.mp4", help="Input video file")
    args = parser.parse_args()

    cap = cv2.VideoCapture(args.input)
    if not cap.isOpened():
        raise SystemExit(f"Could not open video '{args.input}'")

    subtractor = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=50, detectShadows=False)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        mask = subtractor.apply(frame)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        clean = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
        contours, _ = cv2.findContours(clean, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            if cv2.contourArea(contour) > 500:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.imshow('Vehicle Detection', frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
\n# ===== program4.py =====

import argparse
import cv2
import numpy as np

def main():
    parser = argparse.ArgumentParser(description="Read an image and dilate it.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--output", default="program4_dilate.jpg", help="Output image path")
    parser.add_argument("--kernel-size", type=int, default=5, help="Structuring element size")
    args = parser.parse_args()

    img = cv2.imread(args.input, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    kernel = np.ones((args.kernel_size, args.kernel_size), np.uint8)
    dilated = cv2.dilate(img, kernel, iterations=1)
    cv2.imwrite(args.output, dilated)
    print(f"Saved dilated image to {args.output}")

if __name__ == '__main__':
    main()
\n# ===== program40.py =====

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
\n# ===== program5.py =====

import argparse
import cv2
import numpy as np

def main():
    parser = argparse.ArgumentParser(description="Read an image and erode it.")
    parser.add_argument("--input", default="input.jpg", help="Input image path")
    parser.add_argument("--output", default="program5_erode.jpg", help="Output image path")
    parser.add_argument("--kernel-size", type=int, default=5, help="Structuring element size")
    args = parser.parse_args()

    img = cv2.imread(args.input, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise SystemExit(f"Could not load image '{args.input}'")

    kernel = np.ones((args.kernel_size, args.kernel_size), np.uint8)
    eroded = cv2.erode(img, kernel, iterations=1)
    cv2.imwrite(args.output, eroded)
    print(f"Saved eroded image to {args.output}")

if __name__ == '__main__':
    main()
\n# ===== program6.py =====

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
\n# ===== program7.py =====

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
\n# ===== program8.py =====

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
\n# ===== program9.py =====

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
