import os
import tempfile
import shutil


class MyLog:
    """サンプルクラスです。"""

    @classmethod
    def insertLog(cls, file: str, log: str) -> None:
        """クラスメソッド
        指定文字をファイルに出力します。
        出力するファイルがすでに存在している場合は、ファイルの前方に指定文字を挿入します。

        Args:
            file (str): 出力するファイルパス
            log (str): ファイルに書き込む内容

        Returns:
            None: なし
        """

        # 一時ファイルの作成
        with tempfile.NamedTemporaryFile("wt+", delete=False) as tempf:
            # 一時ファイルに書き込み
            tempf.write(log + "\n")

            # 既存ファイルから読み込んで一時ファイルに書き込み
            if os.path.exists(file):
                with open(file, "rt") as reader:
                    tempf.write(reader.read())

        # 一時ファイルの移動（上書き）
        shutil.copy(tempf.name, file)

        return None


if __name__ == "__main__":
    # OK このファイル内でクラスを呼び出してみる

    # 普通にインスタンス化して利用
    # myLog = MyLog()
    # myLog.insertLog("test")

    # MyLog.insertLog("foo")
    print("hello")
    pass
