#!/usr/bin/python3

from board_util import GoBoardUtil
from gtp_connection import GtpConnection

class PolicyPlayer(object):
    version = 0.1
    name = "PolicyPlayer"
    def __init__(self):
        pass

    def get_move(self, board, toplay):
        return GoBoardUtil.generate_rand_max(board, True, True)

    def get_properties(self):
        return dict(
            version=self.version,
            name=self.__class__.__name__,
        )

def createPolicyPlayer():
    con = GtpConnection(PolicyPlayer())
    con.start_connection()

if __name__=='__main__':
    createPolicyPlayer()