# create a black and white 2D map as an jpg
import sys
from PIL import Image
import numpy as np

PIXELS_PER_GRID = (int) (sys.argv[2])

with Image.open(sys.argv[1]) as im:
    px = im.load()
    grid = np.array([[0] * (int)(im.height / PIXELS_PER_GRID + 1)] * (int)(im.width / PIXELS_PER_GRID + 1))
    for y in range(im.height):
        for x in range(im.width):
            grid[(int)(y / PIXELS_PER_GRID)][(int)(x / PIXELS_PER_GRID)] += (int) (0.1 * (255 - np.mean(px[x, y])))
    np.savetxt("occ_grid.txt", grid, fmt="%s", delimiter=" ", newline=" \n")
    norm_grid = grid / np.max(grid)
    np.savetxt("norm_occ_grid.txt", norm_grid, fmt="%s", delimiter=" ", newline=" \n")
    image_grid = Image.new(mode="RGB", size=norm_grid.shape)
    hard_line_grid = grid
    gpx = image_grid.load()
    for y in range(image_grid.height):
        for x in range(image_grid.width):
            gpx[x, y] = ((int)(255 - 255 * norm_grid[y][x]), (int)(255 - 255 * norm_grid[y][x]), (int)(255 - 255 * norm_grid[y][x]))
            if norm_grid[y][x] >= 0.15: 
                hard_line_grid[y][x] = 1
            else:
                hard_line_grid[y][x] = 0
    image_grid.save("Image_grid.png")
    np.savetxt("hard_line_grid.txt", hard_line_grid, fmt="%s", delimiter=" ", newline=" \n")
    gpx = image_grid.load()
    for y in range(image_grid.height):
        for x in range(image_grid.width):
            gpx[x, y] = ((int)(255 - 255 * hard_line_grid[y][x]), (int)(255 - 255 * hard_line_grid[y][x]), (int)(255 - 255 * hard_line_grid[y][x]))
    image_grid.save("Hard_Line_Image_grid.png")
