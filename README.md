# DataAnalyzer
## 概要
　特定の形式で作成されたFortranの解析データを編集し、グラフ作成・保存をするライブラリです。
グラフ出力の際には、応答値を最小化する最適値も同時に出力します。

## API
| ファイル名　| 機能　|
| - | - |
| utils | 補助関数の定義　|
| types | 辞書の型定義　|
| file | ファイルの管理 |
| process | 解析データの編集・最適値の計算 |
| result | 解析データのグラフ作成・保存　|
| main | APIの実行クラス定義　|

## 使い方
　run.pyに使用例を示しています。
以下の引数を定義し、実行してください。

| 引数　| 型　| 機能　|
| - | - | - |
| model_num | int | モデル番号　|
| Fr | flaot | リリーフ荷重[kN]　|
| gamma | float | 減衰係数比 |
| Av | flaot | 地動規準化最大速度 |
| c_lim | List | 減衰係数のグラフ描画範囲　|
| p_lim | List | 地動振動数のグラフ描画範囲　|
| start_p | flaot | 地動振動数の初期値　|
| dp | flaot | 地動振動数の増分　|
| SSA_params | Dict | SSAグラフのパラメータ(ファイル名:z軸ラベル,z軸描画範囲)　|
| MSSA_params | Dict | MSSAグラフのパラメータ(ファイル名:y軸ラベル,y軸描画範囲)　|
| file_path_dir | str | 読み込みファイルのディレクトリパス |
| out_path_dir | str | 保存先ファイルのディレクトリパス |

