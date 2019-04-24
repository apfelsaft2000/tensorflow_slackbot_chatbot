# TensorflowとSlackで日本語雑談チャットbotの実装

## 参照
- 今回tensorflowのseq2seqモデルを実装する上で参考にしたソースコードは[こちら](https://www.tensorflow.org/tutorials/)
- 学習データは[名大会話コーパス](https://mmsrv.ninjal.ac.jp/nucc/)を使用
- slcakの基本操作やbotの設定については[こちら](https://qiita.com/kunitaya/items/690028e33ba5c666f3e2)

## 0.必要ツールおよびモジュール
- [Anaconda3](https://www.anaconda.com/distribution/)
- Python3.6
- TensorFlow-gpu v0.12.1
- MeCab-python3
- slackbot

以下でtensorflow,MeCab-python3,slackbotをインストール

`pip install -r requirements.txt`

MeCab-python3をインストールする前にswigをインストールする必要あり

`conda install -c anaconda swig`

MeCab本体は別でインストールする必要あり。[Mecabの導入方法](http://taku910.github.io/mecab/)

## 1.データの前処理
以下、Neural_seq2seq_Modelディレクトリでの作業
### 1.1 データの取得
[こちらのツール](https://github.com/knok/make-meidai-dialogue)から１対１対応の会話コーパスを取得(ライセンスはオリジナルに従います。)

`mv sequence.txt ./predata/`

以下のスクリプトを実行

`$python data_prepro.py`

コードの関係上、`input.txt` と `output.txt`に入出力となる発話を分ける。

### 1.2 データ整形
訓練用30000と開発用3361に分離

`split -l 30000 input.txt`

`split -l 30000 output.txt`

ファイル名を `{train,dev}_data_{in,out}`にする。

同様に空のファイル`{train,dev}_data_ids_{in,out}.txt`と`{train,dev}_data_vocab_{in,out}.txt`を作成

## 2.モデル訓練
以下のスクリプトでモデルの学習とデータの辞書の作成

`python transrate.py`

100step毎にモデルを保存しているので`ctrl+C`で一旦学習を止めても、止めたところからまた学習することができる。

# Slackボットに学習したモデルを実装
以下、Slack_botディレクトリでの作業
## 1. SlackでBotアカウントの作成
- Slackのワークスペースの新規作成は[こちら](https://slack.com/create#email)

## 2. Botに学習したモデルを実装
- アプリを検索する>カスタムインテグレーション> Bots からBotの名前設定などを行い、発行したAPIトークンを`slackbot_setting.py`の`API_TOKEN`に入力
- `Neural_seq2seq_Model/data`ディレクトリをSlack_bot以下のディレクトリにコピー

`python run.py`で実行


# botと会話してみる
<br>

![screenshot](ttps://user-images.githubusercontent.com/49854447/56628712-c72fe880-6685-11e9-84da-598a155bdea3.png)

# LICENCE
The license of the used data set follows the original.

使用したデータセットのライセンスはオリジナルに従います。
