# create a black and white 2D map as an jpg
from PIL import Image
import numpy as np

PIXELS_PER_GRID = 20

with Image.open("1.jpg") as im:
    px = im.load()
    grid = np.array([[0] * (int)(im.width / PIXELS_PER_GRID)] * (int)(im.height / PIXELS_PER_GRID))
    for y in range(im.height):
        for x in range(im.width):
            grid[(int)(x / PIXELS_PER_GRID)][(int)(y / PIXELS_PER_GRID)] += (int) (0.05 * (255 - np.mean(px[x, y])))
    np.savetxt("occ_grid.txt", grid, fmt="%s", delimiter=" ", newline=" \n")
    norm_grid = grid / np.max(grid)
    image_grid = Image.new(mode="RGB", size=norm_grid.shape)
    gpx = image_grid.load()
    for y in range(image_grid.height):
        for x in range(image_grid.width):
            gpx[x, y] = ((int)(255 - 255 * norm_grid[x][y]), (int)(255 - 255 * norm_grid[x][y]), (int)(255 - 255 * norm_grid[x][y]))
    image_grid.show()
    image_grid.save("Image_grid.png")
