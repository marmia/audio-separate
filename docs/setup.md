# Pythonバージョンをプロジェクトに固定

```
uv python pin 3.11
```

# プロジェクト初期化

```
uv init
```

# 依存パッケージの導入

```
uv add "torch==2.2.2" "audio-separator[cpu]"
```

Note:
PyTorch は 2.3.0 以降、**macOS x86_64 を非対応（配布停止）**にしており、Intel Mac で入れられるのは 2.2系までです。

