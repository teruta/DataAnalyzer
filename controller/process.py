from .file import File
from .types import GraphParamsConfig, AnalysisDataConfig
from .utils.process_utils import quadratic_fitting
import numpy.typing as npt
import numpy as np
import pandas as pd 
import os
import copy

class DataProcessor(File):
    """ Fortran解析データを編集するクラス """
    def __init__(self, file_path_dir: str, out_path_dir: str, 
                 SSA_params: GraphParamsConfig, MSSA_params: GraphParamsConfig):
        super().__init__(file_path_dir, out_path_dir)
        
        # 出力の表示フォーマットの設定  
        np.set_printoptions(precision=6, suppress=True) 

        # インスタンス変数      
        self.SSA_params = SSA_params                          # SSAグラフパラメータ
        self.MSSA_params = MSSA_params                        # MSSAグラフパラメータ
        self.SSA_data_list: AnalysisDataConfig = {}           # SSAデータ辞書{key: [[cd_list], [p_12.00], [p_12.10], ...]}
        self.MSSA_data_list: AnalysisDataConfig= {}           # MSSAデータ辞書{key: [[cd_list], [MSSA_data]]}
        self.RF_data_list: AnalysisDataConfig = {}            # RF(ResonantFrequency)データ辞書
        self.cd_list: npt.NDArray[np.float64] = np.array([])  # 減衰係数リスト
        self.p_list: npt.NDArray[np.float64] = np.array([])   # 地動振動数リスト
        self.c_opt: npt.NDArray[np.float64] = np.array([])    # 最適ダンパーのリスト
        self.y_opt: npt.NDArray[np.float64] = np.array([])    # 最適ダンパー応答値のリスト

    def create_SSA_data(self, start_p: float, dp: float) -> None:
        """ SSA(StadeyStateAmplitude)データリストの作成
        
        SSAデータ形式(2次元配列の辞書)
        ----------
        columns: pの値
        rows: cdの値
        
        """

        p_value = start_p

        # SSAデータをp毎に取得
        while True:
            file_path = os.path.join(self.file_path_dir, f'AnalysisData_p_{p_value:.2f}.csv')

            if not os.path.exists(file_path):
                print(f'{file_path} is not found.\n Finish "read" action.')
                break

            df = pd.read_csv(file_path)
            self.cd_list = df.iloc[:, 0].to_numpy()

            # SSAデータをkey毎に格納
            for column in df.columns[1:]:
                key = column.split("[")[0].strip()
                data_list = df[column].to_numpy()

                # 辞書の初期値をcd_listに設定
                if key not in self.SSA_data_list:
                    self.SSA_data_list[key] = self.cd_list

                self.SSA_data_list[key] = np.vstack((self.SSA_data_list[key], data_list))
    
            self.p_list = np.append(self.p_list, p_value)
            
            p_value += dp

    def create_MSSA_data(self) -> None:
        """ MSSA(MaxStedyStateAmplitude)データリストの作成
        
        MSSAデータ形式(1次元配列の辞書)
        ----------
        columns: cdの値
        
        """

        # MSSAデータをkey毎に格納
        for i, key in enumerate(self.SSA_data_list.keys()):
            
            cd_list_copy = copy.copy(self.cd_list)

            SSA_data = self.SSA_data_list[key][1:]
            MSSA_data = np.max(SSA_data, axis=0)

            if i <= 1:  # key = "u1", "u2" の場合は極値の推定を行う
                # 多項式(2次関数)近似による極値の推定
                min_index, x_ext, y_ext = quadratic_fitting(cd_list_copy, MSSA_data)
                
                cd_list_copy = np.insert(cd_list_copy, min_index+1, x_ext)
                MSSA_data = np.insert(MSSA_data, min_index+1, y_ext)
                
                self.c_opt = np.append(self.c_opt, x_ext)
                self.y_opt = np.append(self.y_opt, y_ext)

                # RFデータの取得
                max_y_index = np.argmax(SSA_data, axis=0)
                self.RF_data_list[key] = [self.cd_list, self.p_list[max_y_index]]

            self.MSSA_data_list[key] = [cd_list_copy, MSSA_data]
        