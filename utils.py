import numpy as np
import copy
import block

def is_int(mystring):
    try:
        temp = int(mystring)
        return True
    except:
        return False

def read_lvl_info(lvl_name):
    map_lvl = open(lvl_name,'r')
    row, col, xStart, yStart = [int(x) for x in next(map_lvl).split()]

    print(row, " ", col, " ", xStart, " ", yStart)
    map_lvl.close()
    return row, col, xStart, yStart

def read_lvl_elements(lvl_name, row):
    map_lvl = open(lvl_name,'r')
    #row, col, xStart, yStart = read_lvl_info(lvl_name)
    #print(row)
    lineCount = 1
    elem_read = []
    for line in map_lvl:
        lineCount += 1
        if (lineCount > row+2):
            stripped_line = line.strip()
            line_list = stripped_line.split()
            elem_read.append(line_list)

    elements = np.array(copy.deepcopy(elem_read), dtype=object)
    int_elements = []
    if len(elements) == 0:
        print('nema elemenata')
        return elem_read
    else:
        for i in elements:
            for j in elements:
                int_elements = [[int(i) for i in j] for j in elements]
    print(np.matrix(int_elements))
    map_lvl.close()
    return int_elements

def read_lvl(lvl_name, row):
    map_lvl = open(lvl_name, 'r')

    # print(row, col, xStart, yStart)
    # print(map_lvl.read())
    map_view = []

    content = map_lvl.readlines()

    for line in content[1:row+1]:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        map_view.append(line_list)

    print(np.matrix(map_view))
    map_lvl.close()
    return map_view

def get_block_position(lvl_name):
    x,y = -1, -1
    map_lvl = open(lvl_name, 'r')

def get_current_lvl():
    new_lvl = './lvl/lvl'
    current_lvl = './lvl/lvl01.txt'
    lvl_cnt = 1
    if block.is_Goal():
        lvl_cnt += 1
        if lvl_cnt < 10:
            new_lvl = new_lvl + '0' + str(lvl_cnt) + '.txt'
        elif lvl_cnt >= 10:
            new_lvl = new_lvl + '0' + str(lvl_cnt) + '.txt'
        else:
            new_lvl = new_lvl+'01.txt'
        return new_lvl
    return current_lvl



def check_elem(elem_read):
    # print(elem_read[-1][-1]) ovo je oznaka elementa
    pass
