from csv import reader
from os import walk
import pygame

def import_csv_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter=',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map

def import_folder(path):
    surfaces = []
    for _, __, images in walk(path):
        for image in images:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surfaces.append(image_surf)
    return surfaces