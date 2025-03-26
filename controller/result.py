from .file import File
from .process import DataProcessor
from .utils.result_utils import set_default, save_graph
from typing import List
import matplotlib.pyplot as plt
import matplotlib_fontja
import numpy as np

class Result(File):
    """ 解析データの出力を行うクラス """
    def __init__(self, file_path_dir: str, out_path_dir: str, 
                 processor: DataProcessor, c_lim: List[float], p_lim: List[float]):
        super().__init__(file_path_dir, out_path_dir)
        
        # AnalysisDataPreparerクラスのコンポジション
        self.processor = processor
        
        # インスタンス変数 
        self.c_lim = c_lim
        self.p_lim = p_lim
        
        # グラフ設定の初期値
        set_default()

    def create_SSA_graph(self) -> None:
        """ SSAグラフ(応答マップ)の作成 """
        
        x = self.processor.cd_list / 1e3  # 単位:[kNs/m] -> [kNs/mm]
        y = self.processor.p_list
        
        for i, key in enumerate(self.processor.SSA_params.keys()):
            # 指定keyの場合は単位変換無し
            z = self.processor.SSA_data_list[key][1:]
            
            if i != 8 and i != 10: 
                z *= 1e2  # 単位:[m] -> [cm]
    
            fig, ax = plt.subplots(figsize=(10, 7))
            
            contour = ax.contourf(
                x, y, z, 
                levels=np.linspace(0, self.processor.SSA_params[key][1], 41), 
                cmap="gist_earth", 
                extend="both"
            )
            
            if i <= 1:
                omega = self.processor.RF_data_list[key][1]

                ax.plot(
                    x, omega, 
                    c="red", linestyle="-", linewidth=4, 
                    label="等高線の峰\n (共振振動数)"
                )
                ax.legend()

            # その他設定
            z_label = self.processor.SSA_params[key][0]
            
            fig.colorbar(contour).set_label(z_label)
            ax.set_xlabel("連結ダンパー減衰係数 [kNs/mm]")
            ax.set_ylabel("地動振動数 [rad/s]")
            ax.set_xlim(self.c_lim)
            ax.set_ylim(self.p_lim)

            save_graph(self.out_path_dir, f"SSA_{key}.png")

    def create_MSSA_graph(self) -> None:
        """ MSSAグラフ(定常振幅の最大値グラフ)の作成"""
        
        for i, key in enumerate(self.processor.MSSA_params.keys()):
            fig, ax = plt.subplots(figsize=(9,7))
            
            if i <= 2:
                x_1 = self.processor.MSSA_data_list[key+"1"][0] / 1e3  # 単位:[kNs/m] -> [kNs/mm]
                x_2 = self.processor.MSSA_data_list[key+"2"][0] / 1e3  # 単位:[kNs/m] -> [kNs/mm]
                y_1 = self.processor.MSSA_data_list[key+"1"][1] * 1e2  # 単位:[m] -> [cm]
                y_2 = self.processor.MSSA_data_list[key+"2"][1] * 1e2  # 単位:[m] -> [cm]
                
                ax.plot(
                    x_1, y_1, 
                    c='tab:blue', linestyle=':', linewidth=4, 
                    label=f'主系'
                )
                ax.plot(
                    x_2, y_2, 
                    c='tab:blue', linestyle='-', linewidth=4, 
                    label=f'副系'
                )
            
            else:
                x = self.processor.MSSA_data_list[key][0] / 1e3  # 単位:[kNs/m] -> [kNs/mm]
                y = self.processor.MSSA_data_list[key][1]
                
                if i != 5 and i != 7: 
                    y *= 1e2  # 単位:[m] -> [cm]

                ax.plot(
                    x, y, 
                    c='tab:blue', linestyle='-', linewidth=4, 
                    label=f'ダンパー'
                )
            
            # 最適ダンパー量のプロット 
            c_opt_1 = self.processor.c_opt[0] / 1e3  # 単位:[kNs/m] -> [kNs/mm]
            c_opt_2 = self.processor.c_opt[1] / 1e3  # 単位:[kNs/m] -> [kNs/mm]
            
            ax.axvline(
                x=c_opt_1, 
                c='0.2', linestyle='-.', linewidth=2, 
                label=f'c_opt1={c_opt_1:.3f}'
            )
            ax.axvline(
                x=c_opt_2, 
                c='0.2', linestyle=':', linewidth=2, 
                label=f'c_opt2={c_opt_2:.3f}'
            )
            
            # その他設定
            y_label = self.processor.MSSA_params[key][0]
            y_lim = self.processor.MSSA_params[key][1]
            
            ax.legend()
            ax.set_xlabel('連結ダンパー減衰係数 [kNs/mm]')
            ax.set_ylabel(y_label)
            ax.grid(True, linestyle=":",c="0")
            ax.set_xticks(np.arange(0, 100, 10))
            ax.set_yticks(np.arange(0, y_lim*1.1, y_lim/5))
            ax.set_xlim(self.c_lim)
            ax.set_ylim(0, y_lim*1.1)
            
            save_graph(self.out_path_dir, f"MSSA_{key}.png")

    def create_RF_graph(self) -> None:
        """ RFグラフ(共振振動数のグラフ)の作成 """
        
        x = self.processor.cd_list / 1e3  # 単位:[kNs/m] -> [kNs/mm]
        key_1 = list(self.processor.SSA_data_list.keys())[0]
        key_2 = list(self.processor.SSA_data_list.keys())[1]
        omega_1 = self.processor.RF_data_list[key_1][1]
        omega_2 = self.processor.RF_data_list[key_2][1]
        
        fig, ax = plt.subplots(figsize=(9, 7))

        ax.plot(
            x, omega_1,  
            c='tab:blue', linestyle=':', linewidth=4, 
            label="主系"
        )
        ax.plot(
            x, omega_2, 
            c='tab:blue', linestyle='-', linewidth=4, 
            label="副系"
            )

        ax.legend()
        ax.set_xlim(self.c_lim)
        ax.set_ylim(self.p_lim)
        ax.set_xlabel('連結ダンパー減衰係数 [kNs/mm]')
        ax.set_ylabel('共進周波数 [rad/s]')
        ax.grid(True, linestyle=":",c="0")

        save_graph(self.out_path_dir, f"RF.png")

    def record_response(self) -> None: 
        """ 最適ダンパー時のMSSA応答値の出力 """

        c_opt_1 = self.processor.c_opt[0] / 1e3  # 単位:[kNs/m] -> [kNs/mm]
        c_opt_2 = self.processor.c_opt[1] / 1e3  # 単位:[kNs/m] -> [kNs/mm]
        y_opt_1 = self.processor.y_opt[0] * 1e2  # 単位:[m] -> [cm]
        y_opt_2 = self.processor.y_opt[1] * 1e2  # 単位:[m] -> [cm]

        with open(self.out_path_dir + "/" + "record.txt", "w", encoding="utf-8") as file:
                file.write(f"main-system: (c_opt1, ymin1) = ({c_opt_1:.3f}, {y_opt_1:.3f})\n")
                file.write(f"sub-system : (c_opt2, ymin2) = ({c_opt_2:.3f}, {y_opt_2:.3f})")
