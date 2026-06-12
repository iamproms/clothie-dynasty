#!/usr/bin/env python3
"""
Clothie Dynasty — Setup Fix Script (Updated for new_pics & Video Download)
Run this from any directory:
  python3 /home/excel/Documents/excel-project/clothie_dynasty/fix_setup.py
"""

import shutil
import os
import subprocess

PROJECT = "/home/excel/Documents/excel-project/clothie_dynasty"
NEW_PICS_SRC = os.path.join(PROJECT, "new_pic")
PUBLIC_DIR = os.path.join(PROJECT, "public")
PUBLIC_IMAGES = os.path.join(PUBLIC_DIR, "images")
PUBLIC_VIDEOS = os.path.join(PUBLIC_DIR, "videos")

def copy_images():
    os.makedirs(PUBLIC_IMAGES, exist_ok=True)
    if not os.path.exists(NEW_PICS_SRC):
        print(f"  ⚠ {NEW_PICS_SRC} does not exist.")
        return
        
    copied = 0
    for fname in os.listdir(NEW_PICS_SRC):
        if fname.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
            src = os.path.join(NEW_PICS_SRC, fname)
            dst = os.path.join(PUBLIC_IMAGES, fname)
            shutil.copy2(src, dst)
            size_kb = os.path.getsize(dst) // 1024
            print(f"  ✓ Copied {fname} ({size_kb}KB)")
            copied += 1
    if copied == 0:
        print("  ⚠ No images found in new_pic/ folder")
    else:
        print(f"\n  {copied} image(s) copied → {PUBLIC_IMAGES}")

def download_video():
    os.makedirs(PUBLIC_VIDEOS, exist_ok=True)
    vid_path = os.path.join(PUBLIC_VIDEOS, "hero.mp4")
    if os.path.exists(vid_path):
        print("  ✓ Video already exists.")
        return

    try:
        print("\n  Downloading Pinterest video (https://pin.it/5C2iaz481)...")
        # Install yt-dlp quietly
        subprocess.run(["pip3", "install", "--quiet", "yt-dlp"], check=True)
        # Download the video
        subprocess.run(["python3", "-m", "yt_dlp", "-o", vid_path, "https://pin.it/5C2iaz481"], check=True)
        print("  ✓ Downloaded hero video!")
    except Exception as e:
        print(f"  ⚠ Could not download video: {e}")

if __name__ == "__main__":
    print("\n── Clothie Dynasty Fix Script ──\n")
    print("Copying images from new_pic to public/images/...")
    copy_images()
    download_video()
    print("\n✅ Done! The dev server will hot-reload automatically.")
