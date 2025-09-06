#!/usr/bin/env python
"""
audio-separator の動作確認用シンプルスクリプト（2stem: Vocals/Instrumental）

実行例:
  uv run python scripts/test.py

環境変数でモデルを変更可能（既定は軽量2stem系）:
  AS_MODEL="UVR-MDX-NET-Inst_HQ_1" uv run python scripts/test.py

注意:
- 初回実行時は対象モデルのダウンロードが走る場合があります。
- CPU環境でのテスト想定（`audio-separator[cpu]` を前提）。
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path


def main() -> int:
    # 入出力パス
    input_path = Path("inputs/test.wav")
    output_dir = Path("outputs")
    # モデル保存先（永続化したいので /tmp ではなくプロジェクト配下に）
    model_dir = Path(os.getenv("AS_MODEL_DIR") or "models")

    # 低負荷な2stemモデルを既定に設定（必要に応じて環境変数で上書き）
    # audio-separator 0.24.1 のサポート例に合わせ、拡張子まで含めた正式名を利用
    # 例: MDX-Net系の2stem: "UVR-MDX-NET-Inst_HQ_3.onnx"
    #    もしくは Roformer系の設定YAML: "model_bs_roformer_ep_317_sdr_12.9755.yaml"（デフォルト）
    model = os.getenv("AS_MODEL") or "UVR-MDX-NET-Inst_HQ_3.onnx"

    # CLI が見つかるか確認
    exe = shutil.which("audio-separator")
    if not exe:
        # venv 直下を探索（例: .venv/bin/audio-separator）
        cand = Path(sys.executable).with_name("audio-separator")
        if cand.exists():
            exe = str(cand)
        else:
            print(
                "error: 'audio-separator' コマンドが見つかりません。\n"
                "uv 環境にインストール済みであることを確認し、\n"
                "'uv run python scripts/test.py' で実行してください。",
                file=sys.stderr,
            )
            return 127

    # 入力の存在チェック
    if not input_path.exists():
        print(f"error: 入力ファイルが見つかりません: {input_path}", file=sys.stderr)
        return 1

    # 出力ディレクトリ・モデル保存先を作成
    output_dir.mkdir(parents=True, exist_ok=True)
    model_dir.mkdir(parents=True, exist_ok=True)

    # コマンド組み立て（audio-separator の正式な引数名に合わせる）
    # - 入力は位置引数
    # - 出力ディレクトリは --output_dir
    # - モデルは -m/--model_filename（省略時はパッケージ既定モデルを使用）
    cmd = [exe, "--output_dir", str(output_dir), "--model_file_dir", str(model_dir)]

    # 環境変数でデバッグを有効化
    if os.getenv("AS_DEBUG") in {"1", "true", "TRUE", "True"}:
        cmd.append("-d")
    if model:
        cmd.extend(["-m", model])
    cmd.append(str(input_path))

    print("[info] 実行コマンド:", " ".join(map(str, cmd)))
    # 実行（出力を取得して簡易リトライ判定に使う）
    result = subprocess.run(cmd, text=True, capture_output=True)
    if result.returncode == 0:
        return 0

    # モデル名の不一致っぽい場合は、モデル指定を外して既定モデルで再実行
    stderr = getattr(result, "stderr", "") or ""
    stdout = getattr(result, "stdout", "") or ""
    output_text = (stdout + "\n" + stderr).lower()
    if "model file" in output_text and "not found" in output_text:
        print(
            "[warn] 指定モデルがサポート外のため、既定モデルで再実行します。",
            file=sys.stderr,
        )
        fallback_cmd = [exe, "--output_dir", str(output_dir), "--model_file_dir", str(model_dir), str(input_path)]
        print("[info] 再実行コマンド:", " ".join(map(str, fallback_cmd)))
        fallback = subprocess.run(fallback_cmd)
        return fallback.returncode

    # 失敗時の詳細出力
    if stdout.strip():
        print("\n---- audio-separator stdout ----\n" + stdout)
    if stderr.strip():
        print("\n---- audio-separator stderr ----\n" + stderr, file=sys.stderr)

    print(
        f"error: audio-separator の実行に失敗しました (code={result.returncode})",
        file=sys.stderr,
    )
    return result.returncode or 1


if __name__ == "__main__":
    raise SystemExit(main())
