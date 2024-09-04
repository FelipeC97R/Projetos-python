import pygame

# Inicializa o Pygame
pygame.init()

# Inicializa o mixer do Pygame
pygame.mixer.init()

# Carrega a música (substitua 'sua_musica.wav' pelo seu arquivo de música)
pygame.mixer.music.load('C:/Users/FelipeCr/Documents/Projetos programação/PYTHON/Marília_Mendonça.mp3')

# Toca a música
pygame.mixer.music.play()

# Espera até que a música terminecls
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
