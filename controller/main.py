from .process import DataProcessor
from .result import Result
from .types import GraphParamsConfig
from typing import List

class AnalysisAPI:
    """ 解析・グラフ出力・最適化を一括で実行するAPIクラス """
    def __init__(self, file_path_dir: str, out_path_dir: str,
                 SSA_params: GraphParamsConfig, MSSA_params: GraphParamsConfig,
                 c_lim: List[float], p_lim: List[float]):
        
        # データ編集クラス
        self.processor = DataProcessor(file_path_dir, out_path_dir, SSA_params, MSSA_params)
        # データ出力クラス
        self.result = Result(file_path_dir, out_path_dir, self.processor, c_lim, p_lim)

    def run(self, start_p: float, dp: float) -> None:
        """ 解析の実行 """
        # SSA/MSSAデータ作成
        self.processor.create_SSA_data(start_p, dp)
        self.processor.create_MSSA_data()

        # SSA/MSSA/RFグラフの作成と保存
        self.result.create_SSA_graph()
        self.result.create_MSSA_graph()
        self.result.create_RF_graph()
        # 最適応答値の保存
        self.result.record_response()
