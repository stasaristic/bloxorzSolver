import numpy
import block
import pygame, sys
import numpy as np
import constants
import utils

def get_tile_color(tile_contents):
    tile_color = constants.EMPTY
    if tile_contents == ".":
        tile_color = constants.EMPTY_SPACE
    if tile_contents == "#":
        tile_color = constants.TILE_COLOR
    if tile_contents == "x":
        tile_color = constants.BUTTON_STRONG_COLOR
    if tile_contents == "o":
        tile_color = constants.BUTTON_SOFT_COLOR
    if tile_contents == "@":
        tile_color = constants.BUTTON_SPLIT_COLOR
    if tile_contents == "G":
        tile_color = constants.GOAL
    if tile_contents == "+":
        tile_color = constants.BLOCK_COLOR
    return tile_color

def draw_map(surface, map_tiles):
    for j, tile in enumerate(map_tiles):
        for i, tile_contents in enumerate(tile):
            #proverava da li hvata zasebno
            #print("{},{}: {}".format(i,j,tile_contents))
            myrect = pygame.Rect(i*constants.BLOCK_WIDTH, j*constants.BLOCK_WIDTH, constants.BLOCK_WIDTH, constants.BLOCK_HEIGHT)
            pygame.draw.rect(surface,get_tile_color(tile_contents), myrect)

def draw_grid(col, surface):

    for i in range(col):
        new_height = round(i * constants.BLOCK_HEIGHT)
        new_width = round(i * constants.BLOCK_WIDTH)
        pygame.draw.line(surface, constants.BLACK, (0, new_height), (screen_width, new_height), 2)
        pygame.draw.line(surface, constants.BLACK, (new_width, 0), (new_width, screen_height), 2)

def game_loop(surface, map_view):

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        draw_map(surface, map_view)
        draw_grid(col, surface)
        pygame.display.update()

def initialize_game():
    pygame.init()
    surface = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Bloxorz solver")
    icon = pygame.image.load('block.png')
    pygame.display.set_icon(icon)
    surface.fill(constants.UGLY_PINK)
    return surface

def main():
    global screen_width, screen_height, row, col, xStart, yStart, elements
    current_lvl = './lvl/lvl17.txt'
    row, col, xStart, yStart = utils.read_lvl_info(current_lvl)
    elements = utils.read_lvl_elements(current_lvl, row)
    map_view = utils.read_lvl(current_lvl, row)


    screen_width = col * 40
    screen_height = row * 40
    surface = initialize_game()
    game_loop(surface, map_view)

if __name__ == "__main__":
    main()
