from pathlib import Path
from uuv_mission.dynamic import Mission


def test_from_csv_with_path():
    p = Path('data/mission.csv')
    m = Mission.from_csv(p)
    assert len(m.reference) == len(m.cave_height) == len(m.cave_depth)
