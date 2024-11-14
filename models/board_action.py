from uuid import UUID
from models.progress import Progress

class BoardAction:
    def __init__(self, uuid: UUID, player: int, src: int, dest: int, amount: int, progress: Progress):
        self.uuid: UUID = uuid
        self.player: int = player
        self.src: int = src
        self.dest: int = dest
        self.amount: int = amount
        self.progress: Progress = progress

