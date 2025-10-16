# control.py (inside the same package folder as dynamic.py)
class PD:
    def __init__(self, kp: float = 0.15, kd: float = 0.6):
        self.kp = kp
        self.kd = kd
        self._e_prev = None

    def reset(self):
        self._e_prev = None

    def __call__(self, r_t: float, y_t: float) -> float:
        e = r_t - y_t
        if self._e_prev is None:
            self._e_prev = e
        u = self.kp * e + self.kd * (e - self._e_prev)
        self._e_prev = e
        return float(u)
