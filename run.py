from controller.main import AnalysisAPI
import numpy as np
import os

# モデル設定
model_num = 5  # モデル番号
Fr = 1200      # リリーフ荷重[kN]
gamma = 0.186    # 減衰係数比
Av = 50        # 入力基準化速度[cm/s]

# グラフの描画範囲
c_lim = [0, 60]
p_lim = [12, 42]

# パラメータ設定
start_p = 12
dp = 0.1

# グラフパラメータの設定
# {key: (ZLabel, ZLim)} (応答MAP用)
SSA_params = {
    "u1": ("主系変位定常振幅 [cm]", Av/2),
    "u2": ("副系変位定常振幅 [cm]", Av/2),
    "v1": ("主系速度定常振幅 [cm/s]", Av*20/2),
    "v2": ("副系速度定常振幅 [cm/s]", Av*20/2),
    "a1": ("主系加速度定常振幅 \n [cm/s²]", Av*20*20/2),
    "a2": ("副系加速度定常振幅 \n [cm/s²]", Av*20*20/2),
    "ud": ("ダンパー変位定常振幅 \n [cm]", Av/4),  
    "vd": ("ダンパー速度定常振幅 \n [cm/s]", Av*20/4),  
    "Fd": ("ダンパー減衰力定常振幅 \n [kN]", Av*20*20*2),
    "Ed": ("ダンパー消費エネルギー量 \n [kNcm]", Av**2*20**2), 
    "theta": ("位相差 [rad]", np.pi)
}

# {key: (YLabel, YLim)} (共振応答用)
MSSA_params = {
    "u" : ("定常振幅の最大値 [cm]", Av),
    "v" : ("定常振幅の最大値", Av*20),
    "a" : ("定常振幅の最大値 [cm/c]", Av*20*20),
    "ud": ("定常振幅の最大値 [cm]", Av),
    "vd": ("定常振幅の最大値 [cm/s]", Av*20),
    "Fd": ("定常振幅の最大値 [kN]", Av*20*20*2),
    "Ed": ("消費エネルギー量の最大値 \n[kNcm]", Av**2*20**2),
    "theta": ("位相差 [rad]", np.pi)
}

# 入出力ファイルの指定
base_dir = os.path.dirname(os.path.abspath(__file__))  # 現在のスクリプトの絶対パス

if gamma == 1.0:
    file_path_dir = os.path.join(base_dir, 'AnalysisData(MaxResponse)', f'model_{model_num}', f'{Av}kine', 'Linear')
    out_path_dir = os.path.join(base_dir, 'AnalyzeGraphs', f'model_{model_num}', f'{Av}kine', 'Linear')
else:
    file_path_dir = os.path.join(base_dir, 'AnalysisData(MaxResponse)', f'model_{model_num}', f'{Av}kine', f'Fr_{Fr},gamma_{gamma}')
    out_path_dir = os.path.join(base_dir, 'AnalyzeGraphs', f'model_{model_num}', f'{Av}kine', f'Fr_{Fr},gamma_{gamma}')
  
# プログラムの実行
API = AnalysisAPI(file_path_dir, out_path_dir, SSA_params, MSSA_params, c_lim, p_lim)
API.run(start_p, dp)