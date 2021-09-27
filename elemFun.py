import block

global elements, map_view, row, col
previous = []  # koristi ovo da cuvas prethodna stanja

# -----------------------------------------------------------
#                      functions Soft Button
# -----------------------------------------------------------

# type of buttons
typeInv = (0, 0)
typeClose = (0, 1)
typeOpen = (1, 0)


def isSBPressed(block, x, y):
    if block.pos == "STOJI" and map_view[x][y] == 'o':
        for elem in elements:
            if (block.x, block.y) == (elem[0], elem[1]):
                return True
    elif block.pos == "LEZI_PO_X" and map_view[x][y] == 'o':
        for elem in elements:
            if (block.x, block.y) == (elem[0], elem[1]) \
                    or (block.x - 1, block.y) == (elem[0], elem[1]) \
                    or (block.x + 1, block.y) == (elem[0], elem[1]):
                return True
    elif block.pos == "LEZI_PO_Y" and map_view[x][y] == 'o':
        for elem in elements:
            if (block.x, block.y) == (elem[0], elem[1]) \
                    or (block.x, block.y - 1) == (elem[0], elem[1]) \
                    or (block.x, block.y + 1) == (elem[0], elem[1]):
                return True
    elif block.pos == "POLA" and map_view[x][y] == 'o':
        for elem in elements:
            if (block.x_split, block.y_split) == (elem[0], elem[1]) \
                    or (block.x, block.y) == (elem[0], elem[1]):
                return True
    else:
        return False


def isSoftButton(x, y):
    for elem in elements:
        if (x, y) == (elem[0], elem[1]):  # pronadje element po koordinatama
            numTilesForSwitching = elem[2]

            for i in range(numTilesForSwitching):
                tile_x = elem[2 * i + 3]  # 3, 5, 7 ...
                tile_y = elem[2 * i + 4]  # 4, 6, 8...
                if (elem[-2], elem[-1]) == (typeInv):
                    if map_view[tile_x][tile_y] == '.':
                        map_view[tile_x][tile_y] = '#'
                    else:
                        map_view[tile_x][tile_y] = '.'
                elif (elem[-2], elem[-1]) == (typeClose):
                    map_view[tile_x][tile_y] = '#'
                elif (elem[-2], elem[-1]) == (typeOpen):
                    map_view[tile_x][tile_y] = '.'
                else:
                    print("Doslo je do greske kod Soft Buttona.")


# -----------------------------------------------------------
#                      functions Hard Button
# -----------------------------------------------------------

def isHBPressed(block):
    if block.pos == "STOJI" and map_view[block.x][block.y] == "x":
        for elem in elements:
            if (block.x, block.y) == (elem[0], elem[1]):
                return True
    else:
        return False


def isHardButton(block, x, y):
    for elem in elements:
        if (x, y) == (elem[0], elem[1]):  # pronadje element po koordinatama
            numTilesForSwitching = elem[2]

            for i in range(numTilesForSwitching):
                tile_x = elem[2 * i + 3]  # 3, 5, 7 ...
                tile_y = elem[2 * i + 4]  # 4, 6, 8...
                if (elem[-2], elem[-1]) == (typeInv):
                    if map_view[tile_x][tile_y] == '.':
                        map_view[tile_x][tile_y] = '#'
                    else:
                        map_view[tile_x][tile_y] = '.'
                elif (elem[-2], elem[-1]) == (typeClose):
                    map_view[tile_x][tile_y] = '#'
                elif (elem[-2], elem[-1]) == (typeOpen):
                    map_view[tile_x][tile_y] = '.'
                else:
                    print("Doslo je do greske kod Hard Buttona.")


# -----------------------------------------------------------
#                      functions Split Button
# -----------------------------------------------------------
def isSplitPressed(block):
    if block.pos != "SPLIT" and map_view[block.x][block.y] == "@":
        for elem in elements:
            if (block.x, block.y) == (elem[0], elem[1]):
                return True
    else:
        return False


def isSplitButton(block, x, y):
    array = []
    for elem in elements:
        if (x, y) == (elem[0], elem[1]):
            num = elem[2]
            for i in range(num):
                b_x = elem[2 * i + 3]
                b_y = elem[2 * i + 4]
                array.append([b_x, b_y])

    (block.x, block.y, block.x_split, block.y_split) = (array[0][0], array[0][1], array[1][0], array[1][1])
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

    if 0 <= x < col and 0 <= y < row and map_view[x][y] != '.':
        if pos == "STOJI":
            return True
        elif pos == "LEZI_PO_Y":
            if y + 1 < row and map_view[x][y + 1] != '.':
                return True
        elif pos == "LEZI_PO_X":
            if x + 1 < map_view[x + 1][y] != '.':
                return True
        else:
            x_split = block.x_split
            y_split = block.y_split

            if x_split >= 0 and y_split >= 0 and x_split < row and y_split < col and map_view[x_split][y_split] != '.':
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
        map_view = block.map_view

        # ako je soft tile ne moze da se stoji
        if pos == "STOJI" and map_view[x][y] == "=":
            return False

        # ako je pritisnuto HardButton
        if isHBPressed(block):
            isHardButton(block, x, y)

        # ako je pritisnuto SoftButton
        if isSBPressed(block):
            isSoftButton(x, y)

        # ako je pritisnuto SplitButton
        if isSplitPressed(block):
            isSplitButton(block, x, y)

        if mergeWait(block):
            willMerge(block)

        return True
    else:
        return False


def isGoal(block):
    x = block.x
    y = block.y
    pos = block.pos
    map_print = block.map_print

    if pos == "STOJI" and map_print[x][y] == "G":
        return True
    else:
        return False


def isVisited(block):
    if block.pos != "SPLIT":
        for i in previous:
            if i.x == block.x and i.y == block.y \
                    and i.pos == block.pos and i.map_view == i.map_view:
                return True
    else:
        for i in previous:
            if i.x == block.x and i.y == block.y \
                    and i.x_split == block.x_split and i.y_split == block.y_split \
                    and i.pos == block.pos:
                return True
    return False

def move(Stack, block, flag):
    if isValidTile(block):
        if isVisited(block):
            return None

        Stack.append(block)
        previous.append(block)
        return True

    return False

def solution2d(block):
    print("LEVEL SOLUTION\n")

    solutionPath = [block]
    temp = block.prev

    while temp != None:
        if temp.pos != "SPLIT":
            newBlock = block.Block(temp.x, temp.y, temp.pos, temp.prev, temp.map_print)
        else:
            newBlock =block.Block(temp.x, temp.y, temp.pos, temp.prev.temp.map_print, temp.x_split, temp.y_split)

        solutionPath = [newBlock] + solutionPath

        temp = temp.parent

    cnt = 0
    for i in solutionPath:
        cnt += 1
        print("\nStep:", cnt, end=' >>>   ')
        i.map_view2D()
        print("=============================")
        i.map_view2D()

    print("COMSUME", cnt, "STEP!!!!")

def BFS(block):
    map_print = block.map_print
    Queue = []
    Queue.append(block)
    previous.append(block)

    virtualStep = 0

    while Queue:
        current = Queue.pop(0)

        if isGoal(current):
            solution2d(current)
            print("Success\nConsume", virtualStep, "virtual step")
            return True

        if current.pos != "SPLIT":
            virtualStep += 4

            move(Queue, current.move_up(), "up")
            move(Queue, current.move_down(), "down")
            move(Queue, current.move_right(), "right")
            move(Queue, current.move_left(), "left")

        else:
            virtualStep += 8
            move(Queue, current.split_move_up(), "up main split part")
            move(Queue, current.split_move_down(), "down main split part")
            move(Queue, current.split_move_right(), "right main split part")
            move(Queue, current.split_move_left(), "left main split part")

            move(Queue, current.split_move_up_other(), "up other split part")
            move(Queue, current.split_move_down_other(), "down other split part")
            move(Queue, current.split_move_right_other(), "right other split part")
            move(Queue, current.split_move_left_other(), "left other split part")

    return False

