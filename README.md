
# 192511030-ITA0510

This repository contains 40 OpenCV Python programs for basic image and video processing experiments.

## Setup

1. Create a Python virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running a program

Each program accepts input file arguments and saves output files.

Example:
```bash
python3 program1.py --input input.jpg --output program1_gray.jpg
python3 program6.py --input input.mp4
python3 program7.py --device 0
```

## Notes

- Replace `input.jpg` and `input.mp4` with your own image and video files.
- Program 36 expects a watch template image with `--template watch_template.jpg`.
- Most programs write files into the repository root.
