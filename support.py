from os import walk
import pygame

def import_folder(path):
    surface_list = []

    for _, __, img_files in walk(path):
        for file in img_files:
            surface_list.append(pygame.image.load(path+'/'+file).convert_alpha())

    return surface_list