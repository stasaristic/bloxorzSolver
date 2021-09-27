import copy
import utils
import elemFun
import queue as Q


class Block():

    def __init__(self, x, y, pos, prev, map_print, x_split=None, y_split=None):
        self.x = x
        self.y = y
        self.pos = pos
        self.prev = prev
        self.map_print = copy.deepcopy(map_print)
        self.x_split = x_split
        self.y_split = y_split
        # Za iscrtavanja u pygame-u
        '''
        self.x = -1
        self.y = -1
        self.pos = "STOJI"
        self.x_split = -1
        self.y_split = -1
        self.lvl_name = ''
        #----------------------------------------------------------------
        lvl_name = utils.get_current_lvl()
        x, y = utils.get_block_position(utils.read_lvl_info(lvl_name))
        self.x = x
        self.y = y
        self.lvl_name = lvl_name
        #gde treba da se pojavi na ekranu
        self.rect = pygame.Rect(x*constants.BLOCK_WIDTH, y*constants.BLOCK_WIDTH, constants.BLOCK_WIDTH, 
        constants.BLOCK_HEIGHT)
        self.prev = prev
        '''

    def move_up(self):
        newBlock = Block(self.x, self.y, self.pos, self, self.map_print)

        if self.pos == "STOJI":
            newBlock.y -= 2
            newBlock.pos = "LEZI_PO_Y"

        if self.pos == "LEZI_PO_Y":
            newBlock.y -= 1
            newBlock.pos = "STOJI"

        if self.pos == "LEZI_PO_X":
            newBlock.y -= 1

        return newBlock

    def move_right(self):
        newBlock = Block(self.x, self.y, self.pos, self, self.map_print)

        if self.pos == "STOJI":
            newBlock.x += 1
            newBlock.pos = "LEZI_PO_X"

        if self.pos == "LEZI_PO_Y":
            newBlock.x += 1

        if self.pos == "LEZI_PO_X":
            newBlock.x += 2
            newBlock.pos = "STOJI"

        return newBlock

    def move_left(self):
        newBlock = Block(self.x, self.y, self.pos, self, self.map_print)

        if self.pos == "STOJI":
            newBlock.x -= 2
            newBlock.pos = "LEZI_PO_X"

        if self.pos == "LEZI_PO_X":
            newBlock.x -= 1
            newBlock.pos = "STOJI"

        if self.pos == "LEZI_PO_Y":
            newBlock.x -= 1

        return newBlock

    def move_down(self):
        newBlock = Block(self.x, self.y, self.pos, self, self.map_print)

        if self.pos == "STOJI":
            newBlock.y += 1
            newBlock.pos = "LEZI_PO_Y"

        if self.pos == "LEZI_PO_Y":
            newBlock.y += 2
            newBlock.pos = "STOJI"

        if self.pos == "LEZI_PO_X":
            newBlock.x += 1

        return newBlock

    # split kretanje
    # nije bitno u kom polozaju se nalazi
    def split_move_up(self):
        newBlock = Block(self.x, self.y, self.pos, self, self.map_print, self.x_split, self.y_split)
        newBlock.y -= 1

        return newBlock

    def split_move_right(self):
        newBlock = Block(self.x, self.y, self.pos, self, self.map_print, self.x_split, self.y_split)
        newBlock.x += 1

        return newBlock

    def split_move_left(self):
        newBlock = Block(self.x, self.y, self.pos, self, self.map_print, self.x_split, self.y_split)
        newBlock.x -= 1

        return newBlock

    def split_move_down(self):
        newBlock = Block(self.x, self.y, self.pos, self, self.map_print, self.x_split, self.y_split)
        newBlock.y += 1

        return newBlock

    # split other
    def split_move_up_other(self):
        newBlock = Block(self.x, self.y, self.pos, self, self.map_print, self.x_split, self.y_split)
        newBlock.y_split -= 1

        return newBlock

    def split_move_right_other(self):
        newBlock = Block(self.x, self.y, self.pos, self, self.map_print, self.x_split, self.y_split)
        newBlock.x_split += 1

        return newBlock

    def split_move_left_other(self):
        newBlock = Block(self.x, self.y, self.pos, self, self.map_print, self.x_split, self.y_split)
        newBlock.x_split -= 1

        return newBlock

    def split_move_down_other(self):
        newBlock = Block(self.x, self.y, self.pos, self, self.map_print, self.x_split, self.y_split)
        newBlock.y_split += 1

        return newBlock

    def map_view2D_block(self):
        if self.pos != "SPLIT":
            print(self.pos, self.x, self.y)
        else:
            print(self.pos, self.x, self.y, self.x_split, self.y_split)

    def map_view2D(self):
        x = self.x
        y = self.y
        x_split = self.x_split
        y_split = self.y_split
        pos = self.pos
        map_print = self.map_print
        if pos != "SPLIT":
            for i in range(len(map_print)):
                print("", end='  ')
                for j in range(len(map_print[i])):
                    if (i == y and j == x and pos == "STOJI") \
                            or ((i == y and j == x) or (i == y and j == x + 1) and pos == "LEZI_PO_X") \
                            or ((i == y and j == x) or (i == y + 1 and j == x) and pos == "LEZI_PO_Y"):

                        print("+", end=' ')

                    elif map_print[i][j] == '.':
                        print(" ", end=' ')
                    else:
                        print(map_print[i][j], end=' ')
                print("")
        else:
            for i in range(len(map_print)):
                print("", end='  ')
                for j in range(len(map_print[i])):
                    if (i == y and j == x) or (i == y_split and j == x_split):
                        print("+", end=' ')
                    elif map_print[i][j] == ".":
                        print(" ", end=' ')
                    else:
                        print(map_print[i][j], end=' ')
                print("")


  # koristi ovo da cuvas prethodna stanja

# -----------------------------------------------------------
#                      functions Soft Button
# -----------------------------------------------------------

'''
def isSBPressed(block, x, y):
    if block.pos == "STOJI" and block.map_print[y][x] == 'o':
        for elem in elements:
            if (block.x, block.y) == (elem[0], elem[1]):
                return True
    elif block.pos == "LEZI_PO_X" and block.map_print[y][x] == 'o':
        for elem in elements:
            if (block.x, block.y) == (elem[0], elem[1]) \
                    or (block.x - 1, block.y) == (elem[0], elem[1]) \
                    or (block.x + 1, block.y) == (elem[0], elem[1]):
                return True
    elif block.pos == "LEZI_PO_Y" and block.map_print[y][x] == 'o':
        for elem in elements:
            if (block.x, block.y) == (elem[0], elem[1]) \
                    or (block.x, block.y - 1) == (elem[0], elem[1]) \
                    or (block.x, block.y + 1) == (elem[0], elem[1]):
                return True
    elif block.pos == "SPLIT" and block.map_print[y][x] == 'o':
        for elem in elements:
            if (block.x_split, block.y_split) == (elem[0], elem[1]) \
                    or (block.x, block.y) == (elem[0], elem[1]):
                return True
    else:
        return False
'''


def isSoftButton(block, x, y):
    typeInv = (0, 0)
    typeClose = (0, 1)
    typeOpen = (1, 0)
    map_print = block.map_print
    for elem in elements:
        if (x, y) == (elem[0], elem[1]):  # pronadje element po koordinatama
            numTilesForSwitching = elem[2]
            #print('javi da si prosao if')
            for i in range(numTilesForSwitching):
                tile_x = elem[2 * i + 3]  # 3, 5, 7 ...
                tile_y = elem[2 * i + 4]  # 4, 6, 8...
                #print('javi da si prosao if')
                if (elem[-2], elem[-1]) == (typeInv):
                    if map_print[tile_x][tile_y] == '.':
                        map_print[tile_x][tile_y] = '#'
                        #block.map_view2D()
                    else:
                        map_print[tile_x][tile_y] = '.'
                elif (elem[-2], elem[-1]) == (typeClose):
                    map_print[tile_x][tile_y] = '#'

                elif (elem[-2], elem[-1]) == (typeOpen):
                    map_print[tile_x][tile_y] = '.'

                else:
                    print("Doslo je do greske kod Soft Buttona.")


# -----------------------------------------------------------
#                      functions Hard Button
# -----------------------------------------------------------
'''
def isHBPressed(block):
    if block.pos == "STOJI" and block.map_print[block.y][block.x] == "x":
        for elem in elements:
            if (block.x, block.y) == (elem[0], elem[1]):
                return True
    else:
        return False
'''


def isHardButton(block, x, y):
    typeInv = (0, 0)
    typeClose = (0, 1)
    typeOpen = (1, 0)
    map_print = block.map_print
    for elem in elements:
        if (x, y) == (elem[0], elem[1]):  # pronadje element po koordinatama
            numTilesForSwitching = elem[2]
            for i in range(numTilesForSwitching):
                tile_x = elem[2 * i + 3]  # 3, 5, 7 ...
                tile_y = elem[2 * i + 4]  # 4, 6, 8...
                if (elem[-2], elem[-1]) == typeInv:
                    if map_print[tile_x][tile_y] == '.':
                        map_print[tile_x][tile_y] = '#'
                    else:
                        map_print[tile_x][tile_y] = '.'

                elif (elem[-2], elem[-1]) == typeClose:
                    map_print[tile_x][tile_y] = '#'
                elif (elem[-2], elem[-1]) == typeOpen:
                    map_print[tile_x][tile_y] = '.'
                else:
                    print("Doslo je do greske kod Hard Buttona.")


# -----------------------------------------------------------
#                      functions Split Button
# -----------------------------------------------------------
'''
def isSplitPressed(block):
    if block.pos != "SPLIT" and block.map_print[block.y][block.x] == "@":
        for elem in elements:
            if (block.x, block.y) == (elem[0], elem[1]):
                return True
    else:
        return False
'''


def isSplitButton(block, x, y):
    array = []
    for elem in elements:
        if (x, y) == (elem[0], elem[1]):
            num = elem[2]
            for i in range(num):
                b_x = elem[2 * i + 3]
                b_y = elem[2 * i + 4]
                array.append([b_x, b_y])

    (block.y, block.x, block.y_split, block.x_split) = \
        (array[0][0], array[0][1], array[1][0], array[1][1])

    block.pos = "SPLIT"


def mergeWait(block):
    if block.pos == "SPLIT":
        return True
    else:
        return False


def willMerge(block):
    if block.y == block.y_split and block.x == block.x_split - 1:
        block.pos = "LEZI_PO_X"
    if block.y == block.y_split and block.x == block.x_split + 1:
        block.pos = "LEZI_PO_X"
        block.x = block.x_split

    if block.x == block.x_split and block.y == block.y_split - 1:
        block.pos = "LEZI_PO_Y"
    if block.x == block.x_split and block.y == block.y_split + 1:
        block.pos = "LEZI_PO_Y"
        block.y = block.y_split


# -----------------------------------------------------------
#                      functions Floor
# -----------------------------------------------------------

def isSteppable(block):
    x = block.x
    y = block.y
    pos = block.pos
    map_print = block.map_print

    if 0 <= x < col and 0 <= y < row and map_print[y][x] != '.':
        if pos == "STOJI":
            return True
        elif pos == "LEZI_PO_Y":
            if y + 1 < row and map_print[y + 1][x] != '.':
                return True
        elif pos == "LEZI_PO_X":
            if x + 1 < col and map_print[y][x + 1] != '.':
                return True
        else:
            x_split = block.x_split
            y_split = block.y_split

            if 0 <= x_split < col and 0 <= y_split < row and map_print[y_split][x_split] != '.':
                return True
    else:
        return False


def isValidTile(block):
    if isSteppable(block):

        x = block.x
        y = block.y
        x_split = block.x_split
        y_split = block.y_split
        pos = block.pos
        map_print = block.map_print

        # ako je soft tile ne moze da se stoji
        if pos == "STOJI" and map_print[y][x] == "=":
            return False

        # ako je pritisnuto HardButton
        if pos == "STOJI" and map_print[y][x] == "x":
            isHardButton(block, x, y)

        # ako je pritisnuto SoftButton
        # if map_print[y][x] == "o":
        # isSoftButton(block, x, y)
        if pos == "STOJI" and map_print[y][x] == 'o':
            isSoftButton(block, x, y)
        if pos == "LEZI_PO_X" and map_print[y][x + 1] == 'o':
            isSoftButton(block, x + 1, y)
        if pos == "LEZI_PO_Y" and map_print[y + 1][x] == 'o':
            isSoftButton(block, x, y + 1)
        if pos == "SPLIT" and map_print[y_split][x_split] == 'o':
            isSoftButton(block, x_split, y_split)

        # ako je pritisnuto SplitButton
        if pos == "STOJI" and map_print[y][x] == "@":
            isSplitButton(block, x_split, y_split)

        if pos == "SPLIT":

            if y == y_split and x == x_split - 1:
                block.pos = "LEZI_PO_X"
            if y == y_split and x == x_split + 1:
                block.pos = "LEZI_PO_X"
                block.x = x_split

            if y == y_split-1 and x == x_split:
                block.pos = "LEZI_PO_Y"
            if y == y_split+1 and x == x_split:
                block.pos = "LEZI_PO_Y"
                block.y = y_split


        return True
    else:
        return False


def isGoal(block):
    x = block.x
    y = block.y
    pos = block.pos
    map_print = block.map_print

    if pos == "STOJI" and map_print[y][x] == "G":
        return True
    else:
        return False


def isVisited(block):
    if block.pos != "SPLIT":
        for i in previous:
            if i.x == block.x and i.y == block.y \
                    and i.pos == block.pos and i.map_print == block.map_print:
                return True
    else:
        for i in previous:
            if i.x == block.x and i.y == block.y \
                    and i.x_split == block.x_split and i.y_split == block.y_split \
                    and i.pos == block.pos and i.map_print == block.map_print:
                return True
    return False


def move(Stack, block, flag):
    if isValidTile(block):
        if isVisited(block):
            return None

        Stack.append(block)
        previous.append(block)
        #print(flag)
        return True

    return False


def solution2d(block):
    print("Resenje:\n")

    solutionPath = [block]
    temp = block.prev

    while temp != None:
        if temp.pos != "SPLIT":
            newBlock = Block(temp.x, temp.y, temp.pos, temp.prev, temp.map_print)
        else:
            newBlock = Block(temp.x, temp.y, temp.pos, temp.prev.temp.map_print, temp.x_split, temp.y_split)

        solutionPath = [newBlock] + solutionPath

        temp = temp.prev

    cnt = 0
    for i in solutionPath:
        cnt += 1
        print("\nKorak:", cnt, end=' >>>   ')
        i.map_view2D_block()
        print("=============================")
        i.map_view2D()

    print("U", cnt, "koraka")


def BFS(block):
    map_print = block.map_print
    Queue = []
    Queue.append(block)
    previous.append(block)

    calculateStep = 0

    while Queue:
        current = Queue.pop(0)

        if isGoal(current):
            solution2d(current)
            print("Uspeh!\nKoraka preracuna:", calculateStep)
            return True

        if current.pos != "SPLIT":
            calculateStep += 4

            move(Queue, current.move_up(), "up")
            move(Queue, current.move_right(), "right")
            move(Queue, current.move_down(), "down")
            move(Queue, current.move_left(), "left")

        else:
            calculateStep += 8
            move(Queue, current.split_move_up(), "up main split part")
            move(Queue, current.split_move_right(), "right main split part")
            move(Queue, current.split_move_down(), "down main split part")
            move(Queue, current.split_move_left(), "left main split part")

            move(Queue, current.split_move_up_other(), "up other split part")
            move(Queue, current.split_move_right_other(), "right other split part")
            move(Queue, current.split_move_down_other(), "down other split part")
            move(Queue, current.split_move_left_other(), "left other split part")

    return False




def main():
    global row, col, xStart, yStart, elements, previous
    previous = []
    current_lvl = './lvl/lvl03.txt'
    row, col, xStart, yStart = utils.read_lvl_info(current_lvl)
    elements = utils.read_lvl_elements(current_lvl, row)
    map_view = utils.read_lvl(current_lvl, row)
    block = Block(xStart, yStart, "STOJI", None, map_view)

    BFS(block)


if __name__ == "__main__":
    main()
