# 作成背景
モールス信号に興味を持ち、聞き取り練習をするために開発

# 構成
```
/
┝main.py            全処理記述
```
# 利用ライブラリと用途
- ## tkinter
  - PythonのGUIフレームワーク
  - [公式リファレンス](https://docs.python.org/ja/3/library/tkinter.html)
- ## pyaudio
  - オーディオIOライブラリ
  - [公式リファレンス](https://people.csail.mit.edu/hubert/pyaudio/docs/)
- ## numpy
  - 数値計算を効率的に行える
  - オーディオのサンプリングに使用
  - [公式リファレンス](https://numpy.org/doc/stable/)
- ## threading
  - マルチスレッド実装
  - 信号再生中にスライドでスピードを変更する際にスレッド使用
  - [公式リファレンス](https://docs.python.org/ja/3/library/threading.html)