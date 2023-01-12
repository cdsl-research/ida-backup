# Locustを使った負荷試験とファイルのコピーを同時に発生させた時のRPSを用いたファイルのコピーの中断と再開を行うアプリケーション
## 作成したソフトウェア
### copy.sh
ファイルのコピーとファイルのコピーにかかる時間を計測します．
### ida_backup_ctrl.sh
Flaskサーバの変数をもとにファイルのコピーの中断と再開を行います．
### monitor.py
Locust による WordPressへのHTTPリクエストを行っている時のRPSの取得，取得したRPSが閾値を上回っているか下回っているかどうかを判別する関数を定義しています．
### server.py
Flaskサーバを構築し，monitor.pyの関数を使い判断したRPSの結果をbool型の変数としてFlaskサーバにアップロードします．
### locustfile.py
負荷試験を行います．

## 手順
1\. locustfile.pyをブラウザで実行します
2\. copy.sh，ida_backup_ctrl.sh，server.pyを同時に実行します
