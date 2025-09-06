#!/usr/bin/env bash
# ---
# audio-separatorテストスクリプト
# ---

set -euo pipefail

# 任意: シェルトレース（デバッグ用途）
# set -x

# audio-separator の詳細ログを有効化（scripts/test.py で -d を付与）
export AS_DEBUG=1

# モデル保存ディレクトリの明示指定（未設定時は scripts/test.py が 'models' を使用）
#export AS_MODEL_DIR="models"

# OpenMP のスレッド上限（CPU使用量の制御。1 で最小）
#export OMP_NUM_THREADS=1

# Intel MKL のスレッド上限（CPU使用量の制御。1 で最小）
#export MKL_NUM_THREADS=1

# 任意: モデルを切り替える場合は以下を有効化（拡張子まで含める）
# 使用モデル（MDX-Net 2stemの軽量モデル）
# export AS_MODEL="UVR-MDX-NET-Inst_HQ_3.onnx"
# 使用モデル（MDX23C 2stem。初回はckptと関連yamlを取得）
# export AS_MODEL="MDX23C-8KFFT-InstVoc_HQ.ckpt"

cd ~/Documents/Projects/audio-separate
uv run python scripts/test.py
