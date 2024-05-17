from uuid import UUID
from models.player_action import PlayerAction
from models.progress import Progress

class BoardAction(PlayerAction):
    uuid: UUID          # uuid of the action
    player: int         # uid of the owning player
    progress: Progress  # progress of the units on the path

    @classmethod
    def fromAttributes(cls, uuid: UUID, player: int, progress: Progress):
        boardaction = {
            'uuid': uuid,
            'player': player,
            'progress': progress
        }
        return cls(boardaction)

    def __init__(self, boardaction: dict): 
        self.uuid = boardaction['uuid']
        self.player = boardaction['player']
        self.progress = Progress(boardaction['progress'])

