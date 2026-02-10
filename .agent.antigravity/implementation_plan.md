# Implementation Plan - MP4 Video Trimming Script

I will create a CLI tool using Python to trim MP4 files. The tool will accept a file path, a start time, and an end time.

## Proposed Changes

### [NEW] [trim_video.py](file:///d:/SIDE_PROJ/Video_Cut/trim_video.py)
This script will:
- Use `argparse` to handle command-line arguments.
- Use `moviepy` to perform the trimming.
- Generate high-quality output in MP4 format.
- Automatically name the output file as `outputYYYYMMDD_HHmiSS.mp4` based on the execution time.
- **Support flexible time formats**: `hh:mm:ss`, `mm:ss`, and total seconds (`ss`).
- **[NEW] .gitignore**: Ignore `input/` directory and files starting with `output`.
- **[NEW] README.md**: Vietnamese user guide for the script.

## Verification Plan

### Manual Verification
- Run the script with the provided sample file: `input\2025-12-03 09-38-07.mp4`.
- Parameters to test:
    - `0 5` (seconds)
    - `00:05` (mm:ss)
    - `00:00:05` (hh:mm:ss)
- Check if all formats produce the same 5-second trimmed video.
