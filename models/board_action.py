from uuid import UUID
from models.player_action import PlayerAction
from models.progress import Progress

class BoardAction(PlayerAction):
    uuid: UUID          # uuid of the action
    player: int         # uid of the owning player
    progress: Progress  # progress of the units on the path

    def __init__(self, uuid: UUID, player: int, progress: Progress):
        self.uuid = uuid
        self.player = player
        self.progress = progress

