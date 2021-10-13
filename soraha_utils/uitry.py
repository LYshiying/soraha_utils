from functools import wraps
from typing import Callable, Union

from .uilog import set_logger

logger = set_logger()


def retry(
    excep: Union[Exception, tuple] = Exception,
    retry_times: int = 3,
    logger: logger = logger,
) -> Callable:
    """retry函数,只要不停尝试就一定会成功！这个函数就是为此而存在的啊kora！简直是人生重来器！麻吉牙白！
    使用也很简单,只需要`@retry()`就可以！真的非常简单了！可恶！人生的重来可没有那么简单啊，大叔！

    Args:
        excep (tuple, Exception): 需要捕获的exception,单个excep或者传入tuple. Defaults to Exception.
        retry_times (int, optional): 重试的次数. Defaults to 3.
        logger (logger, optional): 传入logger记录数据,要不然就用羽衣的默认logger！. Defaults to logger.

    Returns:
        Callable: 把装饰器丢回给你！哈哈！没想到吧！
    """
    excep = (excep,) if isinstance(excep, Exception) else excep

    def deco(func):
        @wraps(func)
        def retrying(*args, **kw):
            nonlocal retry_times
            while retry_times:
                try:
                    return func(*args, **kw)
                except excep as e:
                    logger.info(
                        f"An exception occurred: {e}, retry the function({func.__name__}) again (Remaining retries:{retry_times})"
                    )
                    retry_times -= 1
                    if not retry_times:
                        raise

        return retrying

    return deco
