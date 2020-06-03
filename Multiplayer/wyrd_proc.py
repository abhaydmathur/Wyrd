class Proc:
    def __init__(self, id, num_players = 2):

        self.whowent = [i==-10 for i in range(num_players)] # Init with all false
        self.ready  = None # TODO
        self.id = id
        self.score = 0
        self.something = None # TODO

    def get_player_move(self, p):
        #
        return None

    """
    Per game
    """
