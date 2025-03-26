from typing import Tuple
import numpy.typing as npt
import numpy as np

def quadratic_fitting(x_list: npt.NDArray[np.float64], y_list: npt.NDArray[np.float64]) -> Tuple[int, float, float]:
    """ 多項式近似(2次関数)による極値の推定 """

    # 最小値インデックス
    p = np.argmin(y_list)

    try:
        # 最小値近傍のデータ(3点)を取得
        u_list = x_list[p-1:p+2]
        v_list = y_list[p-1:p+2]
        
        # 係数行列の作成
        A = np.array([[u**2, u, 1] for u in u_list])
        b = np.array(v_list)
        
        # 多項式係数を計算
        params = np.linalg.solve(A, b)
        a1, a2, a3 = params
        
        # 極値の計算
        x_ext = -a2 / (2*a1)
        y_ext = (-a2**2 + 4*a1*a3) / (4*a1)
        
        return p, x_ext, y_ext
    
    except IndexError:
        print("Extremum is out of range")
    except ZeroDivisionError:
        print("Division by zero is not allowed")
    except np.linalg.LinAlgError:
        print("Matrix is singular, cannot compute inverse matrix")
    
    return 0, 0, 0  # エラー時のデフォルト値を返す