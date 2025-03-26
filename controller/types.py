from typing import Tuple, TypedDict
import numpy.typing as npt
import numpy as np

class GraphParamsConfig(TypedDict):
    """ グラフパラメータ用辞書のコンフィグタイプ"""
    key: str
    params: Tuple[str, float]

class AnalysisDataConfig(TypedDict):
    """ 解析データ格納用辞書のコンフィグタイプ"""
    key: str
    datalist: npt.NDArray[np.float64]