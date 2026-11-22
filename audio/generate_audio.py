"""
Voice-over Audio Generator and Audio-Visual Synchronization Master
Synthesizes narration for all 6 scenes using macOS Daniel voice,
generates a soft ambient harmonic background track,
and computes exact scene durations for Manim visual synchronization.
"""
import os
import subprocess
import json
import numpy as np

AUDIO_DIR = os.path.dirname(os.path.abspath(__file__))
GEN_DIR = os.path.join(AUDIO_DIR, "generated_audio")
os.makedirs(GEN_DIR, exist_ok=True)

SCENE_SCRIPTS = {
    "scene_01": (
        "Welcome to M-3 Linear Algebra. What if a small table of just four numbers "
        "could tilt, stretch, and reshape an entire infinite coordinate plane? "
        "From three-dimensional computer graphics and robotic kinematics to quantum mechanics "
        "and neural networks, linear transformations are the fundamental language of space. "
        "Today, we explore the central question: How does a simple matrix transform every vector in a coordinate plane? "
        "Join me as we unlock the geometry behind the algebra."
    ),
    "scene_02": (
        "In mathematics, a transformation T from R-two to R-two is a function that takes an input vector "
        "and produces an output vector. For a transformation to be linear, it must satisfy two strict conditions. "
        "First, additivity. Transforming the sum of two vectors, u plus v, must equal T of u plus T of v. "
        "Whether you add before transforming or transform before adding, the result is identical. "
        "Second, homogeneity. Scaling an input vector by a scalar c must scale the output vector by that exact same scalar: "
        "T of c-u equals c times T of u. "
        "Notice a crucial consequence: if the scalar c is zero, T of the zero vector must equal zero! "
        "The origin remains permanently anchored at the center. "
        "A spatial translation shifts the origin, which is why pure shifts are affine transformations, not linear ones."
    ),
    "scene_03": (
        "Here is the great secret of linear algebra: to know where every single vector in the plane lands, "
        "you only need to know where two special vectors go: the standard basis vectors! "
        "In two-dimensional space, these are e-one, pointing one unit along the x-axis, and e-two, pointing one unit along the y-axis. "
        "Now, consider our transformation matrix: A equals row one, two, one; row two, one, two. "
        "Look closely at the columns of this matrix. The first column, two, one, is exactly where basis vector e-one lands! "
        "The second column, one, two, is where basis vector e-two lands! "
        "As we apply the matrix continuously across the plane, watch how the coordinate grid behaves. "
        "Grid lines remain perfectly straight and parallel, while our original unit square deforms smoothly into a parallelogram."
    ),
    "scene_04": (
        "Now, let's calculate the transformation of general vectors algebraically and verify them on our coordinate plane. "
        "Take our first test vector: v equals (1, 1). To find its transformed position, we multiply matrix A by vector v. "
        "For the first component, we take the dot product of the top row with v: two times one, plus one times one, which equals three. "
        "For the second component, the bottom row: one times one, plus two times one, which also equals three! "
        "Thus, T of (1, 1) equals (3, 3). Notice how the vector stretches outwards along the line y equals x. "
        "Next, consider vector w equals (2, -1). Multiplying row one: two times two plus one times negative one gives three. "
        "Row two: one times two plus two times negative one gives zero! "
        "Vector w lands squarely on the positive x-axis at (3, 0). "
        "Now let's examine the geometric area. The determinant of matrix A is two times two minus one times one, giving four minus one, which equals three. "
        "The absolute value of the determinant is the area scaling factor! "
        "Since our original unit square had an area of one, our transformed parallelogram has an area of exactly three square units."
    ),
    "scene_05": (
        "Let's step back and understand what this means geometrically. "
        "A linear transformation can alter vector lengths and change directions. "
        "Notice: length changes depend on direction! "
        "Vector (1, 1) was scaled by a factor of three, while vector (1, -1) was completely unchanged in length. "
        "However, area scaling is constant throughout the entire plane, governed universally by the determinant. "
        "Crucially, a determinant of one means area and orientation are preserved, but the transformation is not necessarily a rigid rotation! "
        "For example, consider the matrix with diagonal entries two and zero-point-five. "
        "Its determinant is two times zero-point-five, which equals one. "
        "It stretches the horizontal direction by two and compresses the vertical direction by half. "
        "Area is preserved, but vector lengths change! "
        "In contrast, rigid rotations preserve both area and all vector lengths. "
        "Furthermore, our main matrix has determinant positive three, so area triples and orientation is preserved. "
        "If the determinant were negative, space would be reflected like a mirror image. "
        "And if the determinant were zero, space collapses into a flat line or single point!"
    ),
    "scene_06": (
        "To summarize our journey, here are the three essential things to remember: "
        "One: A linear transformation preserves vector addition and scalar multiplication, keeping the origin strictly fixed. "
        "Two: A matrix is simply a compact package encoding the destination of the basis vectors. "
        "And three: The determinant gives the exact factor by which areas scale, and tells us whether spatial orientation is preserved. "
        "One matrix. Infinite vectors. A transformed space. "
        "Thank you for watching."
    )
}

def get_audio_duration(file_path):
    cmd = [
        "/opt/homebrew/bin/ffprobe",
        "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        file_path
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return float(res.stdout.strip())

def generate_voiceover():
    timings = {}
    total_voice_dur = 0.0
    print("Generating voice-over narration...")
    for scene_id, text in SCENE_SCRIPTS.items():
        aiff_path = os.path.join(GEN_DIR, f"{scene_id}_raw.aiff")
        wav_path = os.path.join(GEN_DIR, f"{scene_id}.wav")
        
        # Synthesize via macOS 'say' with Daniel voice at 165 wpm
        cmd_say = ["say", "-v", "Daniel", "-r", "165", text, "-o", aiff_path]
        subprocess.run(cmd_say, check=True)
        
        # Convert and normalize audio with high quality 44.1kHz stereo
        cmd_conv = [
            "/opt/homebrew/bin/ffmpeg", "-y",
            "-i", aiff_path,
            "-ar", "44100",
            "-ac", "2",
            "-af", "loudnorm=I=-16:LRA=11:TP=-1.5",
            wav_path
        ]
        subprocess.run(cmd_conv, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        
        dur = get_audio_duration(wav_path)
        # Add 1.5s padding at the end of each scene for graceful animation buffer
        scene_dur = dur + 1.5
        timings[scene_id] = {
            "speech_duration": dur,
            "scene_duration": scene_dur
        }
        total_voice_dur += scene_dur
        print(f"  {scene_id}: voice = {dur:.2f}s -> allocated scene duration = {scene_dur:.2f}s")
        if os.path.exists(aiff_path):
            os.remove(aiff_path)
            
    print(f"Total Video Duration across all 6 scenes: {total_voice_dur:.2f}s (~{total_voice_dur/60:.2f} minutes)")
    
    # Save timings to JSON for Manim scenes
    timing_file = os.path.join(AUDIO_DIR, "scene_timings.json")
    with open(timing_file, "w") as f:
        json.dump(timings, f, indent=2)
    print(f"Saved timings to {timing_file}")
    
    # Generate Ambient Background Score (Soft warm acoustic chord progression)
    generate_ambient_score(total_voice_dur + 5.0)
    return timings

def generate_ambient_score(total_duration, sample_rate=44100):
    """
    Synthesizes an elegant, low-level warm ambient background pad.
    Chords: Cmaj7 - Am7 - Fmaj7 - Gsus4 (warm low harmonics, no harsh transients).
    """
    print(f"Synthesizing ambient background music track ({total_duration:.1f}s)...")
    t = np.linspace(0, total_duration, int(sample_rate * total_duration), endpoint=False)
    
    # Base drone frequencies for an ambient educational chord progression (C - G - A - F)
    # Slow gentle LFO oscillation
    lfo = 0.5 * (1.0 + np.sin(2 * np.pi * 0.15 * t))
    
    # Chord frequencies: C (130.81 Hz), E (164.81 Hz), G (196.00 Hz), B (246.94 Hz), D (293.66 Hz)
    sig = (
        0.25 * np.sin(2 * np.pi * 130.81 * t) +
        0.18 * np.sin(2 * np.pi * 164.81 * t) +
        0.20 * np.sin(2 * np.pi * 196.00 * t) +
        0.12 * np.sin(2 * np.pi * 246.94 * t) +
        0.08 * np.sin(2 * np.pi * 293.66 * t) +
        0.15 * np.sin(2 * np.pi * 65.41 * t) # deep sub warmth
    ) * (0.8 + 0.2 * lfo)
    
    # Apply soft master envelope (fade in 2s, fade out 3s)
    fade_in_len = int(sample_rate * 2.0)
    fade_out_len = int(sample_rate * 3.0)
    env = np.ones_like(sig)
    env[:fade_in_len] = np.linspace(0, 1, fade_in_len)
    env[-fade_out_len:] = np.linspace(1, 0, fade_out_len)
    
    sig = sig * env
    # Normalize and convert to 16-bit PCM
    sig = sig / np.max(np.abs(sig)) * 0.15 # soft -18dB relative level
    audio_int16 = (sig * 32767).astype(np.int16)
    
    raw_wav = os.path.join(GEN_DIR, "ambient_raw.wav")
    bg_music_wav = os.path.join(GEN_DIR, "background_music.wav")
    
    import wave
    with wave.open(raw_wav, "w") as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        # Interleave stereo
        stereo_data = np.column_stack((audio_int16, audio_int16)).flatten()
        wf.writeframes(stereo_data.tobytes())
        
    # Apply warm lowpass filter at 1200Hz and volume leveling using ffmpeg
    cmd_bg = [
        "/opt/homebrew/bin/ffmpeg", "-y",
        "-i", raw_wav,
        "-af", "lowpass=f=1200,volume=-24dB",
        bg_music_wav
    ]
    subprocess.run(cmd_bg, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    if os.path.exists(raw_wav):
        os.remove(raw_wav)
    print(f"Background score ready: {bg_music_wav}")

if __name__ == "__main__":
    generate_voiceover()

