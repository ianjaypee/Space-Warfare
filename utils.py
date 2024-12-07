import os
import pygame

def load_image(path, use_transparency=False, rect_img=(0, 0)):
    width, height = rect_img

    try:
        image = pygame.image.load(path)
    except (pygame.error):
        print("Could not load the image: ", path)
        raise (SystemExit)

    if use_transparency:
        image = image.convert()
    else:
        image = image.convert_alpha()

 
    if width >= 1 and height >= 1:
        image = scale_image(image, (width, height))
    else: 
        pass

    return image


def scale_image(image, size_required):
    scaled_img = pygame.transform.scale(image, size_required)
    return scaled_img


def load_sound(filename, sound_lvl=1.0):
    class WithoutSound:
        def play(self):
            pass

    if not pygame.mixer or not pygame.mixer.get_init():
        return WithoutSound()

    path = os.path.join('data', 'sounds', filename)
    try:
        sound = pygame.mixer.Sound(path)
    except (pygame.error):
        print("Could not load the sound: ", path)
        raise (SystemExit)
    sound.set_volume(sound_lvl) 
    return sound