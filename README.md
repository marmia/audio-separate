# プロジェクト概要：UVR系モデルを用いた無料CLI分離パイプライン

本プロジェクトは、UVR（Ultimate Vocal Remover）系モデル（特に **MDX/MDX23C**）に対応した
CLIツール **audio-separator** を採用し、**uv** で環境を再現可能にした分離パイプラインです。


## 目的
- **Demucs だけでは分離が難しいパート（ピアノ、ギター、その他：エレピ・シンセ等）の聴き取り性向上**にフォーカスします。
- 無料ツールのみを使用し、**バッチ処理**で効率よく大量の音源を分離可能にします。
- 分離結果は耳コピ・素材抽出用の下処理として活用します。

## 採用技術・要件
- パッケージマネージャ：**uv**
- 主要ライブラリ：**audio-separator**（UVRのMDX/MDX23C系モデル対応CLI）
- OS：macOS（Linuxも概ね同様）
- 追加費用：**不要（無償ツールのみ）**

## 分離戦略（要点）
1. **MDX23C 系モデルを第一候補**に使用  
   - 例：`MDX23C-InstVoc_HQ` / `MDX23C-8KFFT-InstVoc_HQ`
   - ボーカル vs インストの分離でも、鍵盤/ギター/シンセの聴き取りが相対的に改善するケースが多い
2. 必要に応じて **TTA（--tta）** や **セグメント長（--segments）** を調整  
3. 目的のパートが抜き出しづらい場合は、**後段でEQ/NR等の軽微なポスト処理**を検討
4. ドラム/ベースが欲しい場合は、**Demucs結果を併用**して素材再構成（本プロジェクトの主眼は鍵盤/ギター/シンセの聞き取り改善）

## 参照
- [nomadkaraoke/python\-audio\-separator: Easy to use stem \(e\.g\. instrumental/vocals\) separation from CLI or as a python package, using a variety of amazing pre\-trained models \(primarily from UVR\)](https://github.com/nomadkaraoke/python-audio-separator)

