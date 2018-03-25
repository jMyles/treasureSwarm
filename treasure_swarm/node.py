class TreasureKeeper:
    """
    A node which keeps treasure.
    """
    def __init__(self, signature_stamp):
        self.keeper_stamp = signature_stamp

    def start_keeping_treasure(self, reactor=None):
        pass


class TreasureGuide:
    """
    A node which helps find nodes who keep treasure.
    """


class TreasureSteward(TreasureKeeper, TreasureGuide):
    """
    A node which both keeps treasure and helps find it.
    """


class TreasureSeeker:
    """
    An actor seeking something in the swarm.
    """