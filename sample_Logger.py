import os
import logging

logger = logging.getLogger("logger")  # logger名loggerを取得
logger.setLevel(logging.DEBUG)  # loggerとしてはDEBUGで

# handler1を作成
handler1 = logging.StreamHandler()
handler1.setFormatter(logging.Formatter("%(asctime)s %(levelname)8s %(message)s"))


# ファイル名組み立て
filename = __file__ + ".output.txt"

# handler2を作成
handler2 = logging.FileHandler(filename=filename)  # handler2はファイル出力
handler2.setLevel(logging.WARN)  # handler2はLevel.WARN以上
handler2.setFormatter(logging.Formatter("%(asctime)s %(levelname)8s %(message)s"))

# loggerに2つのハンドラを設定
logger.addHandler(handler1)
logger.addHandler(handler2)

# 出力処理
logger.debug("debug message")
logger.info("info message")
logger.warning("warning message")
logger.error("error message")
