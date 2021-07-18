from random import randrange


class ScrambleGenerator:

    scramble = []

    UMoves = []
    DMoves = []
    RMoves = []
    LMoves = []
    FMoves = []
    BMoves = []

    xMoves = []
    yMoves = []
    zMoves = []
    allMoves = []

    initialized = False

    cube = [
        # U 0
        ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
        # L 1
        ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
        # F 2
        ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'],
        # R 3
        ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r'],
        # B 4
        ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
        # D 5
        ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y']
    ]

    def __init__(self):

        pass

    def initialize(self):
        if not self.initialized:
            self.UMoves.extend(['U', 'U\'', 'U2'])
            self.DMoves.extend(['D', 'D\'', 'D2'])
            self.RMoves.extend(['R', 'R\'', 'R2'])
            self.LMoves.extend(['L', 'L\'', 'L2'])
            self.FMoves.extend(['F', 'F\'', 'F2'])
            self.BMoves.extend(['B', 'B\'', 'B2'])

            self.xMoves.extend([self.UMoves, self.DMoves])
            self.yMoves.extend([self.RMoves, self.LMoves])
            self.zMoves.extend([self.FMoves, self.BMoves])

            self.allMoves.extend([self.xMoves, self.yMoves, self.zMoves])
            self.initialized = True

    def generateScramble(self, movesCount):
        self.scramble = []

        lastMoveGroupXYZ = -1
        preLastMoveGroupXYZ = -1
        lastMoveGroupUDRLFB = -1
        preLastMoveGroupUDRLFB = -1

        continueLoop = True

        while(continueLoop):
            randXYZ = randrange(len(self.allMoves))
            randUDRLFB = randrange(len(self.allMoves[0]))
            randMove = randrange(len(self.allMoves[0][0]))
            if preLastMoveGroupXYZ != randXYZ:
                if lastMoveGroupUDRLFB != randUDRLFB:
                    move = self.allMoves[randXYZ][randUDRLFB][randMove]
                    self.scramble.append(move)
                    preLastMoveGroupXYZ = lastMoveGroupXYZ
                    preLastMoveGroupUDRLFB = lastMoveGroupUDRLFB
                    lastMoveGroupXYZ = randXYZ
                    lastMoveGroupUDRLFB = randUDRLFB

            if len(self.scramble) == movesCount:
                continueLoop = False

    def getScramble(self, movesCount):
        self.initialize(self)
        self.generateScramble(self, movesCount)
        return self.scramble

    def faceMove(self, x):
        self.cube[x][0], self.cube[x][6], self.cube[x][4], self.cube[x][2] = self.cube[x][6], self.cube[x][4], \
                                                                             self.cube[x][2], self.cube[x][0]
        self.cube[x][1], self.cube[x][7], self.cube[x][5], self.cube[x][3] = self.cube[x][7], self.cube[x][5], \
                                                                             self.cube[x][3], self.cube[x][1]
        return

    def faceMovePrime(self, x):
        self.cube[x][0], self.cube[x][2], self.cube[x][4], self.cube[x][6] = self.cube[x][2], self.cube[x][4], \
                                                                             self.cube[x][6], self.cube[x][0]
        self.cube[x][1], self.cube[x][3], self.cube[x][5], self.cube[x][7] = self.cube[x][3], self.cube[x][5], \
                                                                             self.cube[x][7], self.cube[x][1]
        return

    def swap(self, x1, x2, x3, x4, y1, y2, y3, y4):
        self.cube[x1][y1], self.cube[x2][y2], self.cube[x3][y3], self.cube[x4][y4] = self.cube[x2][y2], self.cube[x3][
            y3], self.cube[x4][y4], self.cube[x1][y1]

    def resetCube(self):
        self.cube = [
            # U 0
            ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
            # L 1
            ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
            # F 2
            ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'],
            # R 3
            ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r'],
            # B 4
            ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
            # D 5
            ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y']
        ]

    def drawImage(self, scramble: list):
        self.resetCube(self)

        for x in scramble:
            pass

            if x[0] == 'U':
                if x == 'U':
                    self.faceMove(self, 0)
                    self.swap(self, 1, 2, 3, 4, 0, 0, 0, 0)
                    self.swap(self, 1, 2, 3, 4, 1, 1, 1, 1)
                    self.swap(self, 1, 2, 3, 4, 2, 2, 2, 2)
                elif x == 'U\'':
                    self.faceMovePrime(self, 0)
                    self.swap(self, 1, 4, 3, 2, 0, 0, 0, 0)
                    self.swap(self, 1, 4, 3, 2, 1, 1, 1, 1)
                    self.swap(self, 1, 4, 3, 2, 2, 2, 2, 2)
                elif x == 'U2':
                    self.faceMove(self, 0)
                    self.swap(self, 1, 2, 3, 4, 0, 0, 0, 0)
                    self.swap(self, 1, 2, 3, 4, 1, 1, 1, 1)
                    self.swap(self, 1, 2, 3, 4, 2, 2, 2, 2)
                    self.faceMove(self, 0)
                    self.swap(self, 1, 2, 3, 4, 0, 0, 0, 0)
                    self.swap(self, 1, 2, 3, 4, 1, 1, 1, 1)
                    self.swap(self, 1, 2, 3, 4, 2, 2, 2, 2)

            elif x[0] == 'D':
                if x == 'D':
                    self.faceMove(self, 5)
                    self.swap(self, 1, 4, 3, 2, 4, 4, 4, 4)
                    self.swap(self, 1, 4, 3, 2, 5, 5, 5, 5)
                    self.swap(self, 1, 4, 3, 2, 6, 6, 6, 6)
                elif x == 'D\'':
                    self.faceMovePrime(self, 5)
                    self.swap(self, 1, 2, 3, 4, 4, 4, 4, 4)
                    self.swap(self, 1, 2, 3, 4, 5, 5, 5, 5)
                    self.swap(self, 1, 2, 3, 4, 6, 6, 6, 6)
                elif x == 'D2':
                    self.faceMove(self, 5)
                    self.swap(self, 1, 4, 3, 2, 4, 4, 4, 4)
                    self.swap(self, 1, 4, 3, 2, 5, 5, 5, 5)
                    self.swap(self, 1, 4, 3, 2, 6, 6, 6, 6)
                    self.faceMove(self, 5)
                    self.swap(self, 1, 4, 3, 2, 4, 4, 4, 4)
                    self.swap(self, 1, 4, 3, 2, 5, 5, 5, 5)
                    self.swap(self, 1, 4, 3, 2, 6, 6, 6, 6)

            elif x[0] == 'R':
                if x == 'R':
                    self.faceMove(self, 3)
                    self.swap(self, 0, 2, 5, 4, 2, 2, 2, 6)
                    self.swap(self, 0, 2, 5, 4, 3, 3, 3, 7)
                    self.swap(self, 0, 2, 5, 4, 4, 4, 4, 0)
                elif x == 'R\'':
                    self.faceMovePrime(self, 3)
                    self.swap(self, 0, 4, 5, 2, 2, 6, 2, 2)
                    self.swap(self, 0, 4, 5, 2, 3, 7, 3, 3)
                    self.swap(self, 0, 4, 5, 2, 4, 0, 4, 4)
                elif x == 'R2':
                    self.faceMove(self, 3)
                    self.swap(self, 0, 2, 5, 4, 2, 2, 2, 6)
                    self.swap(self, 0, 2, 5, 4, 3, 3, 3, 7)
                    self.swap(self, 0, 2, 5, 4, 4, 4, 4, 0)
                    self.faceMove(self, 3)
                    self.swap(self, 0, 2, 5, 4, 2, 2, 2, 6)
                    self.swap(self, 0, 2, 5, 4, 3, 3, 3, 7)
                    self.swap(self, 0, 2, 5, 4, 4, 4, 4, 0)

            elif x[0] == 'L':
                if x == 'L':
                    self.faceMove(self, 1)
                    self.swap(self, 0, 4, 5, 2, 6, 2, 6, 6)
                    self.swap(self, 0, 4, 5, 2, 7, 3, 7, 7)
                    self.swap(self, 0, 4, 5, 2, 0, 4, 0, 0)
                elif x == 'L\'':
                    self.faceMovePrime(self, 1)
                    self.swap(self, 0, 2, 5, 4, 6, 6, 6, 2)
                    self.swap(self, 0, 2, 5, 4, 7, 7, 7, 3)
                    self.swap(self, 0, 2, 5, 4, 0, 0, 0, 4)
                elif x == 'L2':
                    self.faceMove(self, 1)
                    self.swap(self, 0, 4, 5, 2, 6, 2, 6, 6)
                    self.swap(self, 0, 4, 5, 2, 7, 3, 7, 7)
                    self.swap(self, 0, 4, 5, 2, 0, 4, 0, 0)
                    self.faceMove(self, 1)
                    self.swap(self, 0, 4, 5, 2, 6, 2, 6, 6)
                    self.swap(self, 0, 4, 5, 2, 7, 3, 7, 7)
                    self.swap(self, 0, 4, 5, 2, 0, 4, 0, 0)

            elif x[0] == 'F':
                if x == 'F':
                    self.faceMove(self, 2)
                    self.swap(self, 0, 1, 5, 3, 4, 2, 0, 6)
                    self.swap(self, 0, 1, 5, 3, 5, 3, 1, 7)
                    self.swap(self, 0, 1, 5, 3, 6, 4, 2, 0)
                elif x == 'F\'':
                    self.faceMovePrime(self, 2)
                    self.swap(self, 0, 3, 5, 1, 4, 6, 0, 2)
                    self.swap(self, 0, 3, 5, 1, 5, 7, 1, 3)
                    self.swap(self, 0, 3, 5, 1, 6, 0, 2, 4)
                elif x == 'F2':
                    self.faceMove(self, 2)
                    self.swap(self, 0, 1, 5, 3, 4, 2, 0, 6)
                    self.swap(self, 0, 1, 5, 3, 5, 3, 1, 7)
                    self.swap(self, 0, 1, 5, 3, 6, 4, 2, 0)
                    self.faceMove(self, 2)
                    self.swap(self, 0, 1, 5, 3, 4, 2, 0, 6)
                    self.swap(self, 0, 1, 5, 3, 5, 3, 1, 7)
                    self.swap(self, 0, 1, 5, 3, 6, 4, 2, 0)

            elif x[0] == 'B':
                if x == 'B':
                    self.faceMove(self, 4)
                    self.swap(self, 0, 3, 5, 1, 0, 2, 4, 6)
                    self.swap(self, 0, 3, 5, 1, 1, 3, 5, 7)
                    self.swap(self, 0, 3, 5, 1, 2, 4, 6, 0)
                elif x == 'B\'':
                    self.faceMovePrime(self, 4)
                    self.swap(self, 0, 1, 5, 3, 0, 6, 4, 2)
                    self.swap(self, 0, 1, 5, 3, 1, 7, 5, 3)
                    self.swap(self, 0, 1, 5, 3, 2, 0, 6, 4)
                elif x == 'B2':
                    self.faceMove(self, 4)
                    self.swap(self, 0, 3, 5, 1, 0, 2, 4, 6)
                    self.swap(self, 0, 3, 5, 1, 1, 3, 5, 7)
                    self.swap(self, 0, 3, 5, 1, 2, 4, 6, 0)
                    self.faceMove(self, 4)
                    self.swap(self, 0, 3, 5, 1, 0, 2, 4, 6)
                    self.swap(self, 0, 3, 5, 1, 1, 3, 5, 7)
                    self.swap(self, 0, 3, 5, 1, 2, 4, 6, 0)
