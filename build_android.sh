#!/bin/bash
# ==========================================
#  Restaurant POS - Android Builder
#  Designed by A7MED ASHRAF
#  📞 01080343968
# ==========================================

echo "[1/5] Checking dependencies..."
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python3 is not installed!"
    exit 1
fi

echo "[2/5] Installing buildozer..."
pip3 install buildozer cython

echo "[3/5] Installing Android dependencies..."
sudo apt-get update
sudo apt-get install -y python3-pip build-essential git ffmpeg \
    libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \
    libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev \
    libfreetype6-dev libgl1-mesa-dev libgles2-mesa-dev

echo "[4/5] Building APK..."
cd Android
buildozer android debug

echo "[5/5] Done!"
echo "=========================================="
echo "APK file: bin/restaurantpos-1.0-arm64-v8a_debug.apk"
echo "=========================================="
