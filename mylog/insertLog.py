import os
import tempfile
import shutil


class MyLog:
    """サンプルクラスです。"""

    @classmethod
    def insertLog(cls, log: str = "") -> None:
        """クラスメソッド　指定文字をファイルに出力します。

        Args:
            log (str, optional): 出力したい文字列. Defaults to "".

        Returns:
            None: なし
        """

        # 出力するパスの組み立て
        dirpath: str = os.getcwd()
        filename: str = __file__ + ".output.txt"
        path: str = os.path.join(dirpath, filename)

        # 一時ファイルの作成
        with tempfile.NamedTemporaryFile("wt+", delete=False) as tempf:
            # 一時ファイルに書き込み
            tempf.write(log + "\n")

            # 既存ファイルから読み込んで一時ファイルに書き込み
            if os.path.exists(path):
                with open(path, "rt") as reader:
                    tempf.write(reader.read())

        # 一時ファイルの移動（上書き）
        shutil.copy(tempf.name, path)

        return None


# OK このファイル内でクラスを呼び出してみる

# 普通にインスタンス化して利用
# myLog = MyLog()
# myLog.insertLog("test")

# MyLog.insertLog("foo")
