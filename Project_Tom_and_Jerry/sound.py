from class_file import*
from global_variable import *
# Function to toggle sound
pygame.mixer.init()
mixer.music.load('Menu_sound.mp3')
mixer.music.play(-1)
 #biến flag_sound_game lưu trữ cờ bật âm trong lúc chơi

# WinSound
Win_sound = mixer.Sound('WIN.wav')

# transistion
transition_sound = mixer.Sound('transition.wav')

# Main game loop starts here...
# game loop
# Khởi tạo biến global để lưu trạng thái âm thanh
sound_enabled = True
inMenu = True
# Hàm để bật hoặc tắt âm thanh
def toggle_sound():
    global sound_enabled
    sound_enabled = not sound_enabled
    print(sound_enabled)
    if sound_enabled:
        optionsettings[4] ="SoundOn"
        if inMenu:
            
            pygame.mixer.unpause()  # Bật âm thanh
            mixer.music.load('Menu_sound.mp3')
            mixer.music.play(-1)
        else:
            pygame.mixer.unpause()  # Bật âm thanh
            mixer.music.load('Background.ogg')
            mixer.music.play(-1)
        
    else:
        optionsettings[4] ="Soundoff"
        mixer.music.stop()
        pygame.mixer.pause()
def playSound(n: int):
    sound_files=["Background.ogg","Menu_sound.mp3","Intro.mp3","WIN.wav","move.mp3","lose.mp3"]
    sound = pygame.mixer.Sound(sound_files[n])
    global sound_enabled
    if sound_enabled:
        if n!=3 and n != 5:
            sound.play()
        else:
            mixer.music.stop()
            sound.play()

        
