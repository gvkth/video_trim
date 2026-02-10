# Walkthrough - MP4 Video Trimming Script

I have implemented a Python script to trim MP4 files based on your requirements.

## Changes Made
- Created `trim_video.py` using `moviepy`.
- Implemented CLI argument parsing for file path, start time, and end time.
- Implemented automatic output filename generation in the format `outputYYYYMMDD_HHmiSS.mp4`.

## Verification Results

### Manual Verification
I ran the script with the following command:
```powershell
python trim_video.py "input\2025-12-03 09-38-07.mp4" 0 5
```

**Output:**
```
Trimming 'input\2025-12-03 09-38-07.mp4' from 0.0s to 5.0s...
Saving to 'output20260210_105549.mp4'...
...
MoviePy - video ready output20260210_105549.mp4
Trimming complete!
```

The file `output20260210_105549.mp4` was successfully created.

## Usage
To use the script, run:
```powershell
python trim_video.py <file_path> <start_time> <end_time>
```

### Supported Time Formats
- **Total Seconds**: `15` or `15.5`
- **Minutes and Seconds**: `01:30` (1 minute 30 seconds)
- **Hours, Minutes, and Seconds**: `01:02:03` (1 hour, 2 minutes, 3 seconds)

### Examples
```powershell
# Using seconds
python trim_video.py "input\video.mp4" 0 5

# Using mm:ss
python trim_video.py "input\video.mp4" 00:01 00:06

# Using hh:mm:ss
python trim_video.py "input\video.mp4" 00:00:10 00:00:20
```
