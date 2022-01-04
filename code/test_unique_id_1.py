import pytest
import tasks


# 跳过测试，添加skip装饰器
@pytest.mark.skip
def test_unique_id():
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2


# 给跳过的测试添加理由
@pytest.mark.skipif(tasks.__version__ < '0.2.0', reason='not support in this version')
def test_unique_id_2():
    ids = []

