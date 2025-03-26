# FortranDataAnalyzer
## 概要
　このAPIは特定の形式で作成されたFortranの解析データを編集し、グラフ作成・保存をするプログラムです。
グラフ出力の際には、応答値を最小化する最適値も同時に出力します。

## API
| ファイル名　| 機能　|
| - | - |
| utils | 補助関数の定義　|
| types | Configの型定義　|
| file | ファイルの管理 |
| process | 解析データの編集・最適値の計算 |
| result | 解析データのグラフ作成・保存　|
| main | APIの実行　|

## 使い方
　run.pyに使用例を示しています。run.py内の引数は以下の通りです。

| 引数　| 機能　|
| - | - |
| model_num | 補助関数の定義　|
| Fr | Configの型定義　|
| gamma | ファイルの管理 |
| Av | 解析データの編集・最適値の計算 |
| c_lim | 解析データのグラフ作成・保存　|
| p_lim | APIの実行　|
| SSA_graph_params | 補助関数の定義　|
| MSSA_graph_params | Configの型定義　|
| file_path_dir | ファイルの管理 |
| out_path_dir | 解析データの編集・最適値の計算 |

