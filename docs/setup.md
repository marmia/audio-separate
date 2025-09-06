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


# Github設定

## GitHub に新しいリポジトリを作成
1. GitHub の Web サイトで「New repository」をクリック

2. リポジトリ名を入力（例: audio-separate）

3. Public/Private を選択

4. 「Initialize with README」は オフ（ローカルに README.md があるので）

5. Create Repository をクリック

→ git remote add origin https://github.com/<ユーザー名>/audio-separate.git という案内が出ます。

## ローカル作業

1. `.gitignore`を作成


2. ローカル初回コミット

```
git add .
git commit -m "Initial commit: uv project with audio-separator setup"
```

3. GitHub リポジトリと接続

```
git remote add origin https://github.com/marmia/audio-separate.git
```

4. 初回プッシュ

```
git push -u origin main
```

