from enum import Enum
import numpy as np
# from scipy import stats
class Signal:
    # TODO: Define the types of x_vec, y_vec
    def __init__(self, x_vec, y_vec) -> None:
        self.title = "untitled signal"
        self.color = SignalColor.DEFAULT
        self.x_vec = x_vec
        self.y_vec = y_vec
        self.last_drawn_index = 0
        self.hidden = False

    def get_statistics(self, index):
        start = index - 360
        start = int(len(self.x_vec) // self.x_vec[-1])
        self.y_vec = self.y_vec[start:index]
        self.x_vec = self.x_vec[start:index]
        mean = np.mean(self.y_vec)
        median = np.median(self.y_vec)
        std = np.std(self.y_vec)
        # mode = stats.mode(self.y_vec)
        max_value = max(self.y_vec)
        min_value = min(self.x_vec)
        return mean, median, std, max_value, min_value


class SignalColor(Enum):
    DEFAULT = (255,255,255)
    RED = (255, 0, 0)
    BLUE = (30,144,255)
    GREEN = (173,255,47)
    YELLOW = (255,255,0)
    ORANGE = (255,165,0)
    PURPLE = (255,0,255)
    TRANSPARENT = (0, 0, 0)
