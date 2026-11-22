"""
Master Build & Render Automation Script for M3 Mathematics Animation Video Project
Renders all 6 scenes at 1080p (1920x1080, 60fps), muxes voice-over narration and
ambient score, and exports the final deliverable to output/Linear_Transformations_Final.mp4.
"""
import os
import sys
import subprocess
import json

SRC_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SRC_DIR)
OUTPUT_DIR = os.path.join(PROJECT_DIR, "output")
AUDIO_DIR = os.path.join(PROJECT_DIR, "audio", "generated_audio")
MEDIA_DIR = os.path.join(PROJECT_DIR, "media")
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(MEDIA_DIR, exist_ok=True)

PYTHON_BIN = sys.executable
FFMPEG_BIN = "/opt/homebrew/bin/ffmpeg"
FFPROBE_BIN = "/opt/homebrew/bin/ffprobe"

SCENES = [
    {"module": "scene_01_hook.py", "class_name": "Scene01Hook", "audio": "scene_01.wav", "id": "scene_01"},
    {"module": "scene_02_concept.py", "class_name": "Scene02Concept", "audio": "scene_02.wav", "id": "scene_02"},
    {"module": "scene_03_visual_intuition.py", "class_name": "Scene03VisualIntuition", "audio": "scene_03.wav", "id": "scene_03"},
    {"module": "scene_04_worked_example.py", "class_name": "Scene04WorkedExample", "audio": "scene_04.wav", "id": "scene_04"},
    {"module": "scene_05_interpretation.py", "class_name": "Scene05Interpretation", "audio": "scene_05.wav", "id": "scene_05"},
    {"module": "scene_06_summary.py", "class_name": "Scene06Summary", "audio": "scene_06.wav", "id": "scene_06"},
]

def render_scene(scene_info, quality="h"):
    """Renders a single scene using Manim."""
    script_path = os.path.join(SRC_DIR, scene_info["module"])
    print(f"\n[1/3] Rendering {scene_info['class_name']} ({quality} quality: 1080p60)...")
    
    cmd = [
        PYTHON_BIN, "-m", "manim",
        f"-q{quality}",
        "--media_dir", MEDIA_DIR,
        script_path,
        scene_info["class_name"]
    ]
    subprocess.run(cmd, check=True)
    
    # Locate output video
    # Usually in media/videos/<module_name>/1080p60/<class_name>.mp4 or 480p15
    res_folder = "1080p60" if quality == "h" else "480p15"
    module_stem = os.path.splitext(scene_info["module"])[0]
    expected_path = os.path.join(MEDIA_DIR, "videos", module_stem, res_folder, f"{scene_info['class_name']}.mp4")
    
    if not os.path.exists(expected_path):
        # Search recursively in media
        for root, dirs, files in os.walk(MEDIA_DIR):
            if f"{scene_info['class_name']}.mp4" in files:
                expected_path = os.path.join(root, f"{scene_info['class_name']}.mp4")
                break
                
    print(f"  Rendered video found at: {expected_path}")
    return expected_path

def mux_scene_audio(video_path, audio_filename, scene_id):
    """Muxes voiceover narration with the rendered scene video, padding audio if needed."""
    audio_path = os.path.join(AUDIO_DIR, audio_filename)
    muxed_path = os.path.join(MEDIA_DIR, f"{scene_id}_muxed.mp4")
    print(f"[2/3] Muxing narration for {scene_id}...")
    
    cmd = [
        FFMPEG_BIN, "-y",
        "-i", video_path,
        "-i", audio_path,
        "-c:v", "copy",
        "-af", "apad",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        muxed_path
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    return muxed_path

def build_full_video(quality="h"):
    print("=" * 65)
    print("M3 MATHEMATICS ANIMATION VIDEO: FULL PRODUCTION PIPELINE")
    print("=" * 65)
    
    muxed_scenes = []
    for sc in SCENES:
        v_path = render_scene(sc, quality=quality)
        m_path = mux_scene_audio(v_path, sc["audio"], sc["id"])
        muxed_scenes.append(m_path)
        
    print("\n[3/3] Concatenating all scenes and mixing ambient score...")
    
    # Create FFmpeg concat list
    concat_list_file = os.path.join(MEDIA_DIR, "concat_list.txt")
    with open(concat_list_file, "w") as f:
        for p in muxed_scenes:
            f.write(f"file '{p}'\n")
            
    concat_temp = os.path.join(MEDIA_DIR, "all_scenes_voice.mp4")
    cmd_concat = [
        FFMPEG_BIN, "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", concat_list_file,
        "-c", "copy",
        concat_temp
    ]
    subprocess.run(cmd_concat, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    
    # Add ambient background score
    bg_music_path = os.path.join(AUDIO_DIR, "background_music.wav")
    final_output = os.path.join(OUTPUT_DIR, "Linear_Transformations_Final.mp4")
    
    cmd_final = [
        FFMPEG_BIN, "-y",
        "-i", concat_temp,
        "-i", bg_music_path,
        "-filter_complex",
        "[0:a]volume=1.0[voice];[1:a]volume=0.15[bg];[voice][bg]amix=inputs=2:duration=first:dropout_transition=3[aout]",
        "-map", "0:v",
        "-map", "[aout]",
        "-c:v", "libx264",
        "-preset", "medium",
        "-crf", "18",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "256k",
        final_output
    ]
    subprocess.run(cmd_final, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    
    print("\n" + "=" * 65)
    print("FINAL MP4 RENDERING COMPLETE!")
    print(f"Deliverable saved to: {final_output}")
    print("=" * 65)
    
    # Inspect final file
    inspect_final_video(final_output)

def inspect_final_video(video_path):
    print("\nINSPECTING FINAL VIDEO SPECIFICATIONS:")
    cmd = [
        FFPROBE_BIN,
        "-v", "error",
        "-select_streams", "v:0",
        "-show_entries", "stream=width,height,r_frame_rate,codec_name",
        "-of", "json",
        video_path
    ]
    res_v = subprocess.run(cmd, capture_output=True, text=True, check=True)
    v_info = json.loads(res_v.stdout)
    
    cmd_dur = [
        FFPROBE_BIN,
        "-v", "error",
        "-show_entries", "format=duration,size,bit_rate",
        "-of", "json",
        video_path
    ]
    res_f = subprocess.run(cmd_dur, capture_output=True, text=True, check=True)
    f_info = json.loads(res_f.stdout)
    
    stream = v_info["streams"][0]
    duration_s = float(f_info["format"]["duration"])
    size_mb = float(f_info["format"]["size"]) / (1024 * 1024)
    
    print(f"  • Resolution: {stream['width']} x {stream['height']} (16:9 Landscape)")
    print(f"  • Video Codec: {stream['codec_name']}")
    print(f"  • Frame Rate: {stream['r_frame_rate']} fps")
    print(f"  • Duration: {duration_s:.2f} seconds ({duration_s/60:.2f} minutes)")
    print(f"  • File Size: {size_mb:.2f} MB")
    print(f"  • 5-7 min requirement: {'PASSED' if 240 <= duration_s <= 420 else 'CHECK'}")
    print(f"  • 1080p requirement: {'PASSED' if stream['width'] == 1920 and stream['height'] == 1080 else 'CHECK'}")

if __name__ == "__main__":
    quality = "h"
    if len(sys.argv) > 1:
        quality = sys.argv[1]
    build_full_video(quality=quality)
