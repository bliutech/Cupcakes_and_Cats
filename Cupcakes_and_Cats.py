#Created by Benson Liu
#Game Name: Cupcakes & Cats (working title)

#Special thanks to Gwyneth Butler for the game sprites artwork (Cupcakes 1 through 5 and the four catsprites)
#"Winding Down" Background music taken from Soundimage.org

#Max Level So far - Level 10


#Need to work on fixing the formating and font of the text as well as the home page. Maybe make an ending screen.


import pygame, random, sys, time
from pygame.locals import *
import os

WINDOWWIDTH = 1153
WINDOWHEIGHT = 692
TEXTCOLOR = (255,102, 153)
TextColor2 = (0,0,0)
BACKGROUNDCOLOR = (0, 0, 0)
FPS = 40

CupcakeMINSIZE = 100
CupcakeMAXSIZE = 150
PLAYERMOVERATE = 5
PLAYERSIZE = 150
Player_Touch = False

#set up pygame and the widow and mouse
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Cupcakes & Cats')
pygame.mouse.set_visible(False)

#os for organizing paths
current_path = os.path.dirname(__file__) # Where your .py file is located
#resource_path = os.path.join(current_path, "Cupcakes_and_Cats") # The resource folder path
image_path = os.path.join(current_path, 'Images') # The image folder path
sound_path = os.path.join(current_path, 'Sounds') # The sound folder path

#paths to all sound files
gameOver = pygame.mixer.Sound(os.path.join(sound_path, 'gameover.wav'))
meow = pygame.mixer.Sound(os.path.join(sound_path, 'Kitten_Meow-SoundBible.com-1295572573.wav'))
splats = pygame.mixer.Sound(os.path.join(sound_path, 'Splat-SoundBible.com-1826190667.wav'))
coinSound = pygame.mixer.Sound(os.path.join(sound_path, 'Mario-coin-sound.wav'))
backgroundMusic = os.path.join(sound_path, 'Winding-Down.wav')

#paths to all image files
cat1 = pygame.image.load(os.path.join(image_path, "BensonCatI.png")).convert_alpha()
cat2 = pygame.image.load(os.path.join(image_path, 'BensonCatII.png')).convert_alpha()
cat3 = pygame.image.load(os.path.join(image_path, 'BensonCatIII.png')).convert_alpha()
cat4 = pygame.image.load(os.path.join(image_path, 'BensonCatIV.png')).convert_alpha()
cupcake1 = pygame.image.load(os.path.join(image_path, 'BensonCupcakeI.png')).convert_alpha()
cupcake2 = pygame.image.load(os.path.join(image_path, 'BensonCupcakeII.png')).convert_alpha()
cupcake3 = pygame.image.load(os.path.join(image_path, 'BensonCupcakeIII.png')).convert_alpha()
cupcake4 = pygame.image.load(os.path.join(image_path, 'BensonCupcakeIV.png')).convert_alpha()
cupcake5 = pygame.image.load(os.path.join(image_path, 'BensonCupcakeV.png')).convert_alpha()
pixelHeart = pygame.image.load(os.path.join(image_path, 'Pixel_Heart.png')).convert_alpha()
candyBackground = os.path.join(image_path, 'Candy_Background.jpg')

def terminate():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # pressing escape quits
                    terminate()
                return

def drawText(text, font, font2, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textobj2 = font2.render(text, 1, TextColor2)
    textrect = textobj.get_rect()
    textrect2 = textobj.get_rect()
    textrect.topleft = (x, y)
    textrect2.topleft = (x-4, y)
    surface.blit(textobj2,textrect2)
    surface.blit(textobj, textrect)

def death():
    if LIVES <= 0:
        return True
    return False

#Function for image backgrounds
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location, size):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.transform.scale(pygame.image.load(image_file),size)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

def playerImage(number):
   while True:
       if number == 0 and Player_Touch == False:
               return pygame.transform.scale(cat3,(PLAYERSIZE,PLAYERSIZE))
       if  number == 1 and Player_Touch == False:
           return pygame.transform.scale(cat1,(PLAYERSIZE,PLAYERSIZE))
       if number == 0 and Player_Touch == True:
           return pygame.transform.scale(cat2,(PLAYERSIZE,PLAYERSIZE))
       if number == 1 and Player_Touch == True:
           return pygame.transform.scale(cat4,(PLAYERSIZE,PLAYERSIZE))
       pygame.display.update()



playerRect = pygame.transform.scale((cat1),(PLAYERSIZE,PLAYERSIZE)).get_rect()

#Have multiple cupcakes so need different cupcake image
def CupcakeImage(number):
    while True:
        if number == 0:
            return cupcake1

        if number == 1:
            return cupcake2

        if number == 2:
            return cupcake3
        
        if number == 3:
            return cupcake4

        if number == 4:
            return cupcake5


GameHeart = pygame.transform.scale(pixelHeart, (30,30))



#pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),pygame.FULLSCREEN)
# set up fonts
font = pygame.font.SysFont(None, 48)
font2 = pygame.font.SysFont(None,49)


# set up sounds
pygame.mixer.init(44100, -16,1,2048)
gameOverSound = gameOver
KatMeow = pygame.mixer.Sound(meow)
KatMeow.set_volume(0.5)
pygame.mixer.music.load(backgroundMusic)
Splat = splats
Splat.set_volume(0.5)
Level_Up = coinSound
Level_Up.set_volume(0.25)



#Background for the game
BackGround = Background(candyBackground, [0,0] , (WINDOWWIDTH,WINDOWHEIGHT))


#Start screen background
StartBackGround = Background(candyBackground, [0,0] , (WINDOWWIDTH,WINDOWHEIGHT))






# show the "Start" screen
windowSurface.blit(StartBackGround.image,StartBackGround.rect)
drawText('Cupcakes & Cats', font, font2, windowSurface, (WINDOWWIDTH / 2)- 150, (WINDOWHEIGHT / 3) + 50)

drawText('Press a key to start.', font, font2, windowSurface, (WINDOWWIDTH / 2) - 160, (WINDOWHEIGHT / 3) + 100)

pygame.display.update()
waitForPlayerToPressKey()



topScore = 0


while True:
    #Set up the start of the game
    Cupcakes = []
    LEVEL = 1
    LIVES = 5
    score = 0
    moveLeft = moveRight = moveUp = moveDown = False
    playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
    cupcakeAddCounter = 0
    Player_Which = 0
    Cupcake_Which = 0
    Player_cycle = 0
    Catch_cycle = 0
    pygame.mixer.music.play(-1, 0.0)

    while True: # the game loop runs while the game part is playing
        CupcakeMINSPEED = 2*LEVEL + 1
        CupcakeMAXSPEED = 2*LEVEL + 2
        ADDNEWCupcakeRATE = 51 - 5*LEVEL


        #movement for lopp for all types of movement
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
                if event.key == K_LEFT or event.key == ord('a'):
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveLeft = False
                    moveRight = True



            if event.type == KEYUP:
                if event.key == K_LEFT or event.key == ord('a'):
                    moveLeft = False
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveRight = False
                if event.key == K_ESCAPE:
                        terminate()


            if event.type == MOUSEMOTION:
                # If the mouse moves, move the player where the cursor is.
                playerRect.move_ip(event.pos[0] - playerRect.centerx, WINDOWHEIGHT-playerRect.centery-(PLAYERSIZE/2))

        # Check if any of the baddies have hit the player.
        for b in Cupcakes:
            if playerRect.colliderect(b['rect']):
                Player_Touch = True
                score += 1
                KatMeow.play()
                Cupcakes.remove(b)

        if Player_Touch == True and Catch_cycle == 1:
            Player_Touch = False

        if Catch_cycle >= 40:
            Catch_cycle = 0

        #This area for game mechanics
        if True:
            cupcakeAddCounter += 1
        
        if cupcakeAddCounter >= ADDNEWCupcakeRATE:
            cupcakeAddCounter = 0
            cupcakeSize = random.randint(CupcakeMINSIZE,CupcakeMAXSIZE)
            newCupcake = {'rect': pygame.Rect(random.randint(0,WINDOWWIDTH-cupcakeSize),0-cupcakeSize,cupcakeSize,cupcakeSize),
                          'speed': random.randint(CupcakeMINSPEED,CupcakeMAXSPEED),
                          'surface': pygame.transform.scale(CupcakeImage(random.randint(0,4)), (cupcakeSize,cupcakeSize)),
                          }

            Cupcakes.append(newCupcake)
            
        # Move the player around.
        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
        if moveRight and playerRect.right < WINDOWWIDTH:
            playerRect.move_ip(PLAYERMOVERATE, 0)

        

        # Move the mouse cursor to match the player.
        pygame.mouse.set_pos(playerRect.centerx, playerRect.centery)


        # Move the Cupcakes down.
        for b in Cupcakes:
                b['rect'].move_ip(0, b['speed'])

        
        # Delete baddies that have fallen past the bottom.
        for b in Cupcakes[:]:
            if b['rect'].top > WINDOWHEIGHT:
                Splat.play()
                score -= 1
                LIVES -= 1
                Cupcakes.remove(b)



        # Draw the game world on the window.
        windowSurface.fill([255, 255, 255]) #Don't think this is neccessary
        windowSurface.blit(BackGround.image, BackGround.rect)
    

        # Draw the score and top score.
        drawText('Score: %s' % (score), font, font2, windowSurface, 10, 0)
        drawText('Top Score: %s' % (topScore), font, font2, windowSurface, 10, 40)
        drawText('Level: %s' % (LEVEL), font, font2, windowSurface, 10, 80)
        drawText('Lives:', font, font2, windowSurface, WINDOWWIDTH-300, 25)

        if LIVES == 5:
            windowSurface.blit(GameHeart, (WINDOWWIDTH - 60, 30))
        if LIVES >= 4 :
            windowSurface.blit(GameHeart, (WINDOWWIDTH - 90, 30))
        if LIVES >= 3:
            windowSurface.blit(GameHeart, (WINDOWWIDTH - 120, 30))
        if LIVES >= 2:
            windowSurface.blit(GameHeart, (WINDOWWIDTH - 150, 30))
        if LIVES >= 1:
            windowSurface.blit(GameHeart, (WINDOWWIDTH - 180, 30))
        
        #Level increaser
        if score > LEVEL * 10:
            LEVEL += 1
            LIVES = 5
            Level_Up.play()

        # Draw the player's rectangle
        if Player_Which == 0:
            windowSurface.blit(playerImage(0), playerRect)
            if Player_cycle > 10:
                Player_Which = 1
                Player_cycle = 0
        elif Player_Which == 1:
            windowSurface.blit(playerImage(1), playerRect)
            if Player_cycle > 10:
                Player_Which = 0
                Player_cycle = 0



        # Draw each baddie
        for b in Cupcakes:
            windowSurface.blit(b['surface'], b['rect'])

        pygame.display.update()

        if death():
            if score > topScore:
                topScore = score

            break

        mainClock.tick(FPS)
        Player_cycle += 1
        Catch_cycle += 1


    # Stop the game and show the "Game Over" screen.
    pygame.mixer.music.stop()
    gameOverSound.play()
    
    drawText('GAME OVER', font, font2, windowSurface,(WINDOWWIDTH / 2)- 100, (WINDOWHEIGHT / 3) + 50)
    drawText('Press a key to play again.', font, font2, windowSurface, (WINDOWWIDTH / 2) - 190, (WINDOWHEIGHT / 3) + 100)
    pygame.display.update()
    waitForPlayerToPressKey()

    gameOverSound.stop()
