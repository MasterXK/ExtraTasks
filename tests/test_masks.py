from src.masks import *
from data import PATH_DATA

print(os.path.dirname('.'))
def test_get_dir_content():
    assert get_dir_content(os.path.join(os.path.dirname(PATH_DATA))) == {"files": 4, "folders": 5}
    assert get_dir_content(os.path.join(os.path.dirname(PATH_DATA)), count_all=True) == {"files": 76, "folders": 32}
