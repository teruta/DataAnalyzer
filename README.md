# DataAnalyzer
## 概要
　特定の形式で作成されたFortranの解析データを編集し、グラフ作成・保存をするライブラリです。  
グラフ出力の際には、応答値を最小化する最適値も同時に出力します。  
  
## API
### ライブラリ概要
- DataAnalyzer
    - types
    - file
    - process
    - result
    - main
    - utils
        - process_utils
        - result_utils
- run
  
### ファイル説明
| ファイル名　| 機能　|
| - | - |
| types | 辞書の型定義　|
| file | ファイルの管理 |
| process | 解析データの編集・最適値の計算 |
| result | 解析データのグラフ作成・保存　|
| main | APIの実行クラス定義　|
| utils | 補助関数の定義　|
| run | APIの実行　|

## 使い方
　run.pyに使用例を示しています。  
引数を定義し、次の形式でプログラムを実行してください。  
  
```
from DataAnalyzer.main import AnalysisAPI

API = AnalysisAPI(file_path_dir, out_path_dir, SSA_params, MSSA_params, c_lim, p_lim)
API.run(start_p, dp)
```
  
| 引数　| 機能　| 型　|
| - | - | - |
| file_path_dir | 読み込みファイルのディレクトリパス | str |
| out_path_dir | 保存先ファイルのディレクトリパス | str |
| SSA_params | SSAグラフのパラメータ {名前: z軸ラベル, z軸描画範囲}　| Dict |
| MSSA_params | MSSAグラフのパラメータ {名前: y軸ラベル, y軸描画範囲}　| Dict |
| c_lim | 減衰係数のグラフ描画範囲　| List |
| p_lim | 地動振動数のグラフ描画範囲　| List |
| start_p | 地動振動数の初期値　| float |
| dp | 地動振動数の増分　| float |

