from os import walk
import pygame

# # =========== TEST IMPORT FOLDER FUNCTION FOR TROUBLE SHOOTING ===========
# character_path = '../Graphics/Character/Run'
# def import_folder(path):
#     for x,y,z in walk(path):
#         print(x,y,z)

# import_folder(character_path)
# # =========== END TEST IMPORT FOLDER FUNCTION FOR TROUBLE SHOOTING ===========


# ========== DELETE ABOVE CODE WHEN GAME IS COMPLETE ==========
def import_folder(path):
    surface_list = []

    for _,__,img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image 
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)

    return surface_list