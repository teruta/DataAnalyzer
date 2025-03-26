import matplotlib.pyplot as plt
import os

def set_default() -> None:
    plt.rcParams['font.size'] = 20              # 全体のフォントサイズ
    plt.rcParams['axes.labelsize'] = 28         # 軸ラベルのフォントサイズ
    plt.rcParams['xtick.labelsize'] = 22        # X軸目盛りラベルのフォントサイズ
    plt.rcParams['ytick.labelsize'] = 22        # Y軸目盛りラベルのフォントサイズ
    plt.rcParams["legend.framealpha"] = 1       # 凡例の透明度（不透明）
    plt.rcParams["legend.facecolor"] = "white"  # 凡例の背景の色（白）
    plt.rcParams["legend.edgecolor"] = "black"  # 凡例の枠線の色（黒）
    plt.rcParams["legend.handlelength"] = 2     # 凡例の線の長さを長くする
    plt.rcParams['figure.dpi'] = 300            # グラフの解像度（dots per inch）

def save_graph(out_path_dir, save_name: str) -> None:
    """ グラフの保存 """
    plt.tight_layout(pad=3.0)
    out_path = os.path.join(out_path_dir, save_name)
    plt.savefig(out_path)
    plt.close()
