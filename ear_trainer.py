import pygame, random, sys, time
from pygame import midi
from button import Button


DIFF = ['EASY','MED','HARD']
DIFF_I = 0
DIFF_COLOR = 'Green'
CURRENT_NOTE = random.choice([57,59,60,62,64,65,67,69])
SHOW_NOTE = False
MODE = 'INTERVALS'


pygame.init()
pygame.midi.init()
player = pygame.midi.Output(0)
player.set_instrument(24)

WIDTH = 1280
HEIGHT = 720

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def intervals():
    SLEEP_TIME = 0.5
    roots = [57,59,60,62,64,65,67]
    root = 0
    # (enabled, semitones from root)
    m2 = (False, 2)
    m3 = (True, 4)
    p4 = (False, 5)
    p5 = (True,7)
    m6 = (False, 9)
    m7 = (False, 11)
    o = (True, 12)
    named_i = {
        2:"Major 2nd",
        4:"Major 3rd",
        5:"Perfect 4th",
        7:"Perfect 5th",
        9:"Major 6th",
        11:"Major 7th",
        12:"Octave"
    }
    config_pad = 35
    left_pad = 20
    x = 0
    # setup first interval
    possible_int = []
    for i in [m2,m3,p4,p5,m6,m7,o]:
        if i[0] == True:
            possible_int.append(i)
    x = random.choice(possible_int)[1]
    show = False
    while True:
        INT_MOUSE_POS = pygame.mouse.get_pos()

        ROOT_BTN = Button(image=None, pos=(0, 40), text_input=f"ROOT: {midi_to_note(roots[root])}", font=get_font(24), base_color="#d7fcd4", 
            hovering_color="White")

        M2 = Button(image=None, pos=(left_pad, 40), text_input=f"M2: {m2[0]}", font=get_font(16), base_color="#d7fcd4", 
            hovering_color="White")
        M2.text_rect.top = M2.rect.top = ROOT_BTN.rect.move(0, config_pad).top
        M3 = Button(image=None, pos=(left_pad, 40), text_input=f"M3: {m3[0]}", font=get_font(16), base_color="#d7fcd4", 
            hovering_color="White")
        M3.text_rect.top = M3.rect.top = M2.rect.move(0, config_pad).top
        P4 = Button(image=None, pos=(left_pad, 40), text_input=f"P4: {p4[0]}", font=get_font(16), base_color="#d7fcd4", 
            hovering_color="White")
        P4.text_rect.top = P4.rect.top = M3.rect.move(0, config_pad).top
        P5 = Button(image=None, pos=(left_pad, 40), text_input=f"P5: {p5[0]}", font=get_font(16), base_color="#d7fcd4", 
            hovering_color="White")
        P5.text_rect.top = P5.rect.top = P4.rect.move(0, config_pad).top
        M6 = Button(image=None, pos=(left_pad, 40), text_input=f"M6: {m6[0]}", font=get_font(16), base_color="#d7fcd4", 
            hovering_color="White")
        M6.text_rect.top = M6.rect.top = P5.rect.move(0, config_pad).top
        M7 = Button(image=None, pos=(left_pad, 40), text_input=f"M7: {m7[0]}", font=get_font(16), base_color="#d7fcd4", 
            hovering_color="White")
        M7.text_rect.top = M7.rect.top = M6.rect.move(0, config_pad).top
        OCT = Button(image=None, pos=(left_pad, 40), text_input=f"OCTAVE: {o[0]}", font=get_font(16), base_color="#d7fcd4", 
            hovering_color="White")
        OCT.text_rect.top = OCT.rect.top = M7.rect.move(0, config_pad).top

        # left align all these
        for button in [ROOT_BTN, M2, M3, P4, P5, M6, M7, OCT]:
            button.text_rect.left = button.rect.left = left_pad

        PLAY_BTN = Button(image=None, pos=(WIDTH / 5 * 1, HEIGHT - 50), text_input=f"PLAY", font=get_font(50), base_color="#d7fcd4", 
            hovering_color="White")

        NEXT_BTN = Button(image=None, pos=(WIDTH / 5 * 3, HEIGHT - 50), text_input=f"NEXT", font=get_font(50), base_color="#d7fcd4", 
            hovering_color="White")

        SHOW_BTN = Button(image=None, pos=(WIDTH / 5 * 2, HEIGHT - 50), text_input=f"SHOW", font=get_font(50), base_color="#d7fcd4", 
            hovering_color="White")

        SCREEN.blit(BG, (0, 0))
        INT_BACK = Button(image=None, pos=(WIDTH / 5 * 4, HEIGHT - 50), 
                            text_input="BACK", font=get_font(50), base_color="#d7fcd4", hovering_color="White")

        buttons = [INT_BACK, ROOT_BTN, PLAY_BTN, NEXT_BTN, SHOW_BTN, M2, M3, P4, P5, M6, M7, OCT]

        for button in buttons:
            button.changeColor(INT_MOUSE_POS)
            button.update(SCREEN)

        if show:
            SHOW_TEXT = get_font(80).render(named_i[x], True, "#b68f40")
            SHOW_RECT = SHOW_TEXT.get_rect(center=(WIDTH / 2, HEIGHT / 2))
            SCREEN.blit(SHOW_TEXT, SHOW_RECT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.midi.quit()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if INT_BACK.checkForInput(INT_MOUSE_POS):
                    main_menu()
                if ROOT_BTN.checkForInput(INT_MOUSE_POS):
                    if root < len(roots) - 1:
                        root += 1
                    else:
                        root = 0
                if NEXT_BTN.checkForInput(INT_MOUSE_POS):
                    show = False
                    possible_int = []
                    for i in [m2,m3,p4,p5,m6,m7,o]:
                        if i[0] == True:
                            possible_int.append(i)
                    x = random.choice(possible_int)[1]
                if PLAY_BTN.checkForInput(INT_MOUSE_POS):
                    play_midi(roots[root])
                    time.sleep(SLEEP_TIME)
                    play_midi(roots[root] + x)
                if SHOW_BTN.checkForInput(INT_MOUSE_POS):
                    show = True

                if M2.checkForInput(INT_MOUSE_POS):
                    if m2[0] == True:
                        m2 = (False, 2)
                    else:
                        m2 = (True, 2)
                if M3.checkForInput(INT_MOUSE_POS):
                    if m3[0] == True:
                        m3 = (False, 5)
                    else:
                        m3 = (True, 4)
                if P4.checkForInput(INT_MOUSE_POS):
                    if p4[0] == True:
                        p4 = (False, 5)
                    else:
                        p4 = (True, 5)
                if P5.checkForInput(INT_MOUSE_POS):
                    if p5[0] == True:
                        p5 = (False, 7)
                    else:
                        p5 = (True, 7)
                if M6.checkForInput(INT_MOUSE_POS):
                    if m6[0] == True:
                        m6 = (False, 9)
                    else:
                        m6 = (True, 9)
                if M7.checkForInput(INT_MOUSE_POS):
                    if m7[0] == True:
                        m7 = (False, 11)
                    else:
                        m7 = (True, 11)
                if OCT.checkForInput(INT_MOUSE_POS):
                    if o[0] == True:
                        o = (False, 12)
                    else:
                        o = (True, 12)

        pygame.display.update()


def pitch():
    while True:
        global DIFF
        global DIFF_I
        global DIFF_COLOR
        global CURRENT_NOTE
        global SHOW_NOTE

        # notes = []
        # if DIFF[DIFF_I] == 'EASY':
        #     notes = [57,59,60,62,64,65,67,69]
        # elif DIFF[DIFF_I] == 'MEDIUM':
        #     notes = [48,50,52,53,55,57,59,60,62,64,65,67,69,71,72]
        # elif DIFF[DIFF_I] == 'HARD':
        #     notes = [48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,
        #     67,68,69,70,71,72]
        # elif DIFF[DIFF_I] == 'MASTER':
        #     notes = [40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,
        #     59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,
        #     81,82,83,84,85,86,87,88]

        PITCH_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))


        DIFF_BTN = Button(image=None, pos=(WIDTH - 75, 40), text_input=DIFF[DIFF_I], font=get_font(24), base_color=DIFF_COLOR, 
            hovering_color="White")

        if SHOW_NOTE:
            NOTE_TEXT = get_font(250).render(midi_to_note(CURRENT_NOTE), True, "Red")
            NOTE_RECT = NOTE_TEXT.get_rect(center=(WIDTH / 2, HEIGHT / 2))
            SCREEN.blit(NOTE_TEXT, NOTE_RECT)

        PLAY_SOUND = Button(image=None, pos=(WIDTH / 5, HEIGHT - 50), 
                            text_input="PLAY", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        PLAY_SHOW = Button(image=None, pos=(WIDTH / 5 * 2, HEIGHT - 50), 
                            text_input="SHOW", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        PLAY_NEXT = Button(image=None, pos=(WIDTH / 5 * 3, HEIGHT - 50), 
                            text_input="NEXT", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        PLAY_BACK = Button(image=None, pos=(WIDTH / 5 * 4, HEIGHT - 50), 
                            text_input="BACK", font=get_font(50), base_color="#d7fcd4", hovering_color="White")


        for button in [DIFF_BTN, PLAY_SOUND, PLAY_SHOW, PLAY_NEXT, PLAY_BACK]:
            button.changeColor(PITCH_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.midi.quit()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PITCH_MOUSE_POS):
                    SHOW_NOTE = False
                    main_menu()
                if PLAY_SOUND.checkForInput(PITCH_MOUSE_POS):
                    play_midi(CURRENT_NOTE)
                if PLAY_SHOW.checkForInput(PITCH_MOUSE_POS):
                    SHOW_NOTE = True
                if PLAY_NEXT.checkForInput(PITCH_MOUSE_POS):
                    SHOW_NOTE = False
                    CURRENT_NOTE = random.choice([57,59,60,62,64,65,67,69])
                if DIFF_BTN.checkForInput(PITCH_MOUSE_POS):
                    if DIFF_I < 2:
                        DIFF_I += 1
                    else:
                        DIFF_I = 0

        pygame.display.update()

# def options():
#     while True:
#         global DIFF
#         global DIFF_COLOR
#         global MODE
#         OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

#         SCREEN.blit(BG, (0, 0))

#         DIFF_TEXT = get_font(24).render(DIFF, True, DIFF_COLOR)
#         DIFF_RECT = DIFF_TEXT.get_rect(right=WIDTH - 10, top=10)
#         SCREEN.blit(DIFF_TEXT, DIFF_RECT)

#         # MODE_TEXT = get_font(24).render(MODE, True, DIFF_COLOR)
#         # MODE_RECT = MODE_TEXT.get_rect(left=10, top=10)
#         # SCREEN.blit(MODE_TEXT, MODE_RECT)

#         MODE_BTN = Button(image=None, pos=(WIDTH / 5, HEIGHT / 6),
#                             text_input=f'MODE: {MODE}', font=get_font(35), base_color="White", hovering_color="Green")
#         MODE_BTN.changeColor(OPTIONS_MOUSE_POS)
#         MODE_BTN.rect = MODE_BTN.image.get_rect(left=20, top=20)
#         MODE_BTN.text_rect = MODE_BTN.text.get_rect(left=20, top=20)
#         MODE_BTN.update(SCREEN)

#         DIFF_EASY = Button(image=None, pos=(WIDTH / 5, HEIGHT / 4),
#                             text_input="EASY", font=get_font(35), base_color="White", hovering_color="Green")
#         DIFF_EASY.changeColor(OPTIONS_MOUSE_POS)
#         DIFF_EASY.update(SCREEN)

#         DIFF_MED = Button(image=None, pos=(WIDTH / 5 * 2, HEIGHT / 4),
#                             text_input="MEDIUM", font=get_font(35), base_color="White", hovering_color="Blue")
#         DIFF_MED.changeColor(OPTIONS_MOUSE_POS)
#         DIFF_MED.update(SCREEN)

#         DIFF_HARD = Button(image=None, pos=(WIDTH / 5 * 3, HEIGHT / 4),
#                             text_input="HARD", font=get_font(35), base_color="White", hovering_color="Red")
#         DIFF_HARD.changeColor(OPTIONS_MOUSE_POS)
#         DIFF_HARD.update(SCREEN)

#         DIFF_MASTER = Button(image=None, pos=(WIDTH / 5 * 4, HEIGHT / 4),
#                             text_input="MASTER", font=get_font(35), base_color="White", hovering_color="Gold")
#         DIFF_MASTER.changeColor(OPTIONS_MOUSE_POS)
#         DIFF_MASTER.update(SCREEN)

#         OPTIONS_BACK = Button(image=None, pos=(WIDTH / 2, HEIGHT / 5 * 3), 
#                             text_input="BACK", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
#         OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
#         OPTIONS_BACK.update(SCREEN)

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.midi.quit()
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
#                     main_menu()
#                 if MODE_BTN.checkForInput(OPTIONS_MOUSE_POS):
#                     if MODE == 'INTERVALS':
#                         MODE = 'PITCH'
#                     else:
#                         MODE = 'INTERVALS'
#                 if DIFF_EASY.checkForInput(OPTIONS_MOUSE_POS):
#                     DIFF = "EASY"
#                     DIFF_COLOR = "Green"
#                 if DIFF_MED.checkForInput(OPTIONS_MOUSE_POS):
#                     DIFF = "MEDIUM"
#                     DIFF_COLOR = "Blue"
#                 if DIFF_HARD.checkForInput(OPTIONS_MOUSE_POS):
#                     DIFF = "HARD"
#                     DIFF_COLOR = "Red"
#                 if DIFF_MASTER.checkForInput(OPTIONS_MOUSE_POS):
#                     DIFF = "MASTER"
#                     DIFF_COLOR = "Gold"

#         pygame.display.update()

def main_menu():
    while True:
        # global DIFF
        # global DIFF_COLOR

        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("EAR TRAINER", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(WIDTH / 2, HEIGHT / 5))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        # DIFF_TEXT = get_font(24).render(DIFF, True, DIFF_COLOR)
        # DIFF_RECT = DIFF_TEXT.get_rect(right=WIDTH - 10, top=10)
        # SCREEN.blit(DIFF_TEXT, DIFF_RECT)
 
        PITCH_BTN = Button(image=None, pos=(WIDTH / 2, HEIGHT / 5 * 2), text_input="PERFECT PITCH", font=get_font(75), base_color="#d7fcd4", 
            hovering_color="White", surface=SCREEN, bg_color=(100, 100, 100, 90), padx=20, pady=20)
        INTERVALS_BTN = Button(image=None, pos=(WIDTH / 2, HEIGHT / 5 * 3), text_input="INTERVALS", font=get_font(75), base_color="#d7fcd4", 
            hovering_color="White", surface=SCREEN, bg_color=(100, 100, 100, 90), padx=20, pady=20)
        QUIT_BTN = Button(image=None, pos=(WIDTH / 2, HEIGHT / 5 * 4), text_input="QUIT", font=get_font(75), base_color="#d7fcd4", 
            hovering_color="White", surface=SCREEN, bg_color=(100, 100, 100, 90), padx=20, pady=20)

        for button in [PITCH_BTN, INTERVALS_BTN, QUIT_BTN]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.midi.quit()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PITCH_BTN.checkForInput(MENU_MOUSE_POS):
                    pitch()
                if INTERVALS_BTN.checkForInput(MENU_MOUSE_POS):
                    intervals()
                if QUIT_BTN.checkForInput(MENU_MOUSE_POS):
                    pygame.midi.quit()
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

# low E = 40
# high E 24 = 88
# D string, 7th fret = 57
def midi_to_note(value):
    notes = ['C','C#/Db','D','D#/Eb','E','F','F#/Gb','G','G#/Ab','A','A#/Bb','B']
    return notes[value % 12]

def play_midi(note):
    player.note_on(note, 127)

main_menu()