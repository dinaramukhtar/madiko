from dataclasses import dataclass


@dataclass
class Hero:
    x: int
    y: int
    dx: int = 0
    dy: int = 0

    def update(self):
        self.dy += 1
        if self.dy > 10:
            self.dy = 10
        self.y += self.dy
