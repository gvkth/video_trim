import sys
import os
import argparse
from datetime import datetime
from moviepy import VideoFileClip

def parse_time_string(time_str):
    """Parses a time string in format hh:mm:ss, mm:ss, or ss (float) into total seconds."""
    try:
        # Check if it's just a number (total seconds)
        return float(time_str)
    except ValueError:
        # Try parsing as hh:mm:ss or mm:ss
        parts = time_str.split(':')
        if len(parts) == 3:  # hh:mm:ss
            h, m, s = map(float, parts)
            return h * 3600 + m * 60 + s
        elif len(parts) == 2:  # mm:ss
            m, s = map(float, parts)
            return m * 60 + s
        else:
            raise ValueError(f"Invalid time format: {time_str}")

def trim_video(input_path, start_time_str, end_time_str):
    # Check if input file exists
    if not os.path.exists(input_path):
        print(f"Error: File '{input_path}' not found.")
        return

    try:
        # Parse time strings
        start_time = parse_time_string(start_time_str)
        end_time = parse_time_string(end_time_str)

        # Load the video clip
        clip = VideoFileClip(input_path)
        
        # Ensure end_time does not exceed video duration
        if end_time > clip.duration:
            print(f"Warning: End time ({end_time}s) exceeds video duration ({clip.duration:.2f}s). Trimming to end.")
            end_time = clip.duration
            
        if start_time >= end_time:
            print(f"Error: Start time ({start_time}s) must be less than end time ({end_time}s).")
            clip.close()
            return

        # Perform trimming
        trimmed_clip = clip.subclipped(start_time, end_time)
        
        # Generate output filename: outputYYYYMMDD_HHmiSS.mp4
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d_%H%M%S")
        output_filename = f"output{timestamp}.mp4"
        
        print(f"Trimming '{input_path}' from {start_time}s to {end_time}s...")
        print(f"Saving to '{output_filename}'...")
        
        # Write the result to a file
        trimmed_clip.write_videofile(output_filename, codec="libx264", audio_codec="aac")
        
        # Close the clips to release memory
        trimmed_clip.close()
        clip.close()
        
        print("Trimming complete!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Trim an MP4 video file.")
    parser.add_argument("file", help="Path to the input MP4 file")
    parser.add_argument("start", help="Start time (hh:mm:ss, mm:ss, or ss)")
    parser.add_argument("end", help="End time (hh:mm:ss, mm:ss, or ss)")
    
    args = parser.parse_args()
    
    trim_video(args.file, args.start, args.end)
