import pygame, sys, random, os


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.image.load(image_file).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height)) 
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class FISH(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.image.load('data/рыба1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.le = 0


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image
        

pygame.init()
size = width, height = 800, 800
screen = pygame.display.set_mode(size)
da = False
sizesize = [[(25, 25), (50, 50), (100, 75), (150, 125)], [(25, 25), (50, 50), (100, 75), (150, 125)], [(25, 25), (50, 50), (100, 75), (150, 125)],
            [(25, 25), (50, 50), (100, 75), (150, 125)], [(50, 25), (100, 50), (150, 75), (200, 150)], [(50, 25), (100, 50), (150, 75), (200, 100)],
            [(50, 25), (100, 50), (150, 100), (200, 200)], [(50, 25), (100, 50), (150, 100), (200, 200)]]
pygame.mouse.set_visible(False)
color = (0, 255, 0)
color_light = "DarkCyan"
color_dark = "DarkBlue"
pl = 0
smallfont = pygame.font.SysFont('Corbel', 40)
text1 = smallfont.render('Новая игра' , True , color)
#text3 = smallfont.render('Настройки' , True , color)
#list_button = [(300, 240, 250, 50, text1), (300, 440, 250, 50, text3)]
list_button = [(300, 240, 250, 50, text1)]
score = 0
BackGround = Background('data/background.jpg', [0, 0])
BackGround2 = Background('data/back2.jpg', [0, 200])
running = True
running2 = False
life = 3
time_elapsed_since_last_action = 0
time_elapsed_since_last_action2 = 0
time_elapsed_since_last_action3 = 0
clock = pygame.time.Clock()
clock1 = pygame.time.Clock()
fp = 60
level = 1
fish = ['рыба1.png', 'рыба2.png', 'рыба3.png', 'рыба4.png', 'рыба5.png',
        'рыба6.png', 'рыба7.png', 'рыба8.png']
mouse = (0, 0)
coor1 = 1
coor2 = 1
ccur = pygame.image.load('data/cur.png').convert_alpha()
ccur2 = pygame.image.load('data/рыба1.png').convert_alpha()
ccur2 = pygame.transform.scale(ccur2, (50, 50))
zwyk = 1
acoint = 0
acoint2 = 0
pygame.display.set_caption('Рыбка')
while running:  
    screen.fill([255, 255, 255])
    screen.blit(BackGround.image, BackGround.rect)
    mouse2 = mouse
    if 0 <= pygame.mouse.get_pos()[0] <= 750 and 0 <= pygame.mouse.get_pos()[1] <= 750:
        mouse = pygame.mouse.get_pos()
    else:
        mouse = mouse2
    if mouse[1] > mouse2[1] and coor2 == 1:
        ccur = pygame.transform.flip(ccur, False, True)
        coor2 = 0
    elif mouse[1] < mouse2[1] and coor2 == 0:
        ccur = pygame.transform.flip(ccur, False, True)
        coor2 = 1
    
    MANUAL_CURSOR = ccur
    MANUAL_CURSOR = pygame.transform.scale(MANUAL_CURSOR, (50, 50))
    MANUAL_CURSOR.set_colorkey((255, 255, 255))
    for i in list_button:
        if i[0] <= mouse[0] <= i[0] + i[2] and i[1] <= mouse[1] <= i[1] + i[3] and coor2 == 1 or\
           i[0] <= mouse[0] <= i[0] + i[2] and i[1] <= mouse[1] + 50 <= i[1] + i[3] and coor2 == 0:
            pygame.draw.rect(screen, color_dark, [i[0], i[1], i[2], i[3]], 5)
            color = "DarkBlue"
            if list_button.index(i) == 0:
                text = 'Новая игра'
            #elif list_button.index(i) == 1:
                #text = 'Настройки'
            img = pygame.image.load('data/скелет.png')
            img = pygame.transform.scale(img, (80, 40))
            img.set_colorkey((255, 255, 255))
            screen.blit(img,(list_button[list_button.index(i)][0] - 80, list_button[list_button.index(i)][1]))
            list_button[list_button.index(i)] = [list_button[list_button.index(i)][0], list_button[list_button.index(i)][1],
                                                 list_button[list_button.index(i)][2], list_button[list_button.index(i)][3],
                                                 smallfont.render(text, True, color)]
        else:
            color = (0, 255, 0)
            if list_button.index(i) == 0:
                text = 'Новая игра'
            elif list_button.index(i) == 1:
                text = 'Настройки'
            list_button[list_button.index(i)] = [list_button[list_button.index(i)][0], list_button[list_button.index(i)][1],
                                                 list_button[list_button.index(i)][2], list_button[list_button.index(i)][3],
                                                 smallfont.render(text, True, color)]
        screen.blit(i[4], (i[0] + 10, i[1] + 10))
    screen.blit(MANUAL_CURSOR, (mouse)) 
    pygame.display.update()

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
        if ev.type == pygame.MOUSEBUTTONDOWN:
            i = list_button[0]
            if i[0] <= mouse[0] <= i[0] + i[2] and i[1] <= mouse[1] <= i[1] + i[3] and coor2 == 1 or\
               i[0] <= mouse[0] <= i[0] + i[2] and i[1] <= mouse[1] + 50 <= i[1] + i[3] and coor2 == 0:
                level = 1
                life = 3
                coor1 = 1
                acoint = 0
                acoint2 = 0
                score = 0
                pl = 0
                ccur2 = pygame.image.load('data/рыба1.png').convert_alpha()
                ccur2 = pygame.transform.scale(ccur2, (50, 50))
                all_sprites = pygame.sprite.Group()
                all_sprites1 = pygame.sprite.Group()
                all_sprites2 = pygame.sprite.Group()
                all_sprites4 = pygame.sprite.Group()
                ccur2 = pygame.image.load('data/рыба1.png').convert_alpha()
                ccur2 = pygame.transform.scale(ccur2, (50, 50))

                mysprite = FISH()
                n = (50, 50)
                pygame.mixer.music.load("data/Фон для игры.mp3")
                vol = 0.2
                pygame.mixer.music.set_volume(vol)
                s = pygame.mixer.Sound("data/звук.mp3")
                s.set_volume(0.6)
                mysprite.image = ccur2
                mysprite.image = pygame.transform.scale(mysprite.image, n)
                mysprite.image.set_colorkey((255, 255, 255))
                mysprite.rect = mysprite.image.get_rect()
                mysprite.rect.x = -n[0]
                mysprite.rect.y = random.randrange(300, 400)
                all_sprites1.add(mysprite)
                running2 = True
                
    while running2:
        
        if zwyk == 1 and pl == 0:
            pygame.mixer.music.play(-1)
            pl = 1
        if level <= 6:
            gi = 2 + level % 8
        else:
            gi = 8
        if time_elapsed_since_last_action > 2400:
            time_elapsed_since_last_action = 0 
            sprite = FISH()
            a = random.randrange(1, 6, 2)
            
            sprite.speed = a
            ffi = random.choice(fish[0:gi])
            sprite.le = fish.index(ffi) + 1
            sprite.image = load_image(ffi)
            n = sizesize[fish.index(ffi)][random.randrange(0, 4)]
            sprite.image = pygame.transform.scale(sprite.image, n)
            sprite.image.set_colorkey((255, 255, 255))
            sprite.rect = sprite.image.get_rect()
            sprite.rect.x = -n[0]
            sprite.rect.y = random.randrange(200, 800 - n[1])
            all_sprites.add(sprite)

        if time_elapsed_since_last_action2 > 2400:
            time_elapsed_since_last_action2 = 0 
            sprite = FISH()
            a = random.randrange(1, 6, 2)
            
            sprite.speed = a
            ffi = random.choice(fish[0:gi])
            sprite.le = fish.index(ffi) + 1
            sprite.image = load_image(ffi)
            sprite.image = pygame.transform.flip(sprite.image, True, False)
            n = sizesize[fish.index(ffi)][random.randrange(0, 4)]
            sprite.image = pygame.transform.scale(sprite.image, n)
            sprite.image.set_colorkey((255, 255, 255))
            sprite.rect = sprite.image.get_rect()
            sprite.rect.x = 800 - n[0]
            sprite.rect.y = random.randrange(200, 800 - n[1])
            all_sprites2.add(sprite)
            
        screen.fill([255, 255, 255])
        screen.blit(BackGround2.image, BackGround2.rect)
        mouse2 = mouse
        if 0 <= pygame.mouse.get_pos()[0] <= 800 - ccur2.get_rect()[2] and 200 <= pygame.mouse.get_pos()[1] <= 800 - ccur2.get_rect()[3]:
            mouse = pygame.mouse.get_pos()
            da = False
        elif 0 <= pygame.mouse.get_pos()[0] <= 800 - ccur2.get_rect()[2] and 0 <= pygame.mouse.get_pos()[1] <= 200:
            mouse = mouse2
            mouse3 = pygame.mouse.get_pos()
            da = True
        else:
            mouse = mouse2
            da = False

        if mouse[0] > mouse2[0] and coor1 == 0:
            ccur2 = pygame.transform.flip(ccur2, True, False)
            coor1 = 1
        elif mouse[0] < mouse2[0] and coor1 == 1:
            ccur2 = pygame.transform.flip(ccur2, True, False)
            coor1 = 0

        if time_elapsed_since_last_action3 > 20000:
            time_elapsed_since_last_action3 = 0
            
            mysprite1 = pygame.sprite.Sprite()
            mysprite1.image = pygame.image.load('data/жизнь.jpg').convert_alpha()
            mysprite1.image = pygame.transform.scale(mysprite1.image, (50, 50))
            mysprite1.image.set_colorkey((255, 255, 255))
            mysprite1.rect = mysprite.image.get_rect()
            mysprite1.rect.x = -50
            mysprite1.rect.y = random.randrange(300, 750)
            all_sprites4.add(mysprite1)
        for i in all_sprites4:
            i.rect.x += 4
            for a in all_sprites1:
                sp = a
            if i.rect.x <= sp.rect.x <= i.rect.x + i.image.get_rect()[2] and i.rect.y <= sp.rect.y + sp.image.get_rect()[3] * 0.5 <= i.rect.y + i.image.get_rect()[3] and coor1 == 0 or\
               i.rect.x <= sp.rect.x + sp.image.get_rect()[2] <= i.rect.x + i.image.get_rect()[2] and i.rect.y <= sp.rect.y + sp.image.get_rect()[3] * 0.5 <= i.rect.y + i.image.get_rect()[3] and coor1 == 1:
                life += 1
                s.play()
                i.kill()
            if i.rect.x > 800:
                i.kill()
            all_sprites4.update()
        all_sprites4.draw(screen)
         
        img2 = pygame.image.load('data/таблица.png')
        img2 = pygame.transform.scale(img2, (800, 200))
        img2.set_colorkey((255, 255, 255))
        screen.blit(img2, (0, 0))
        #
        smallfont = pygame.font.SysFont('Corbel', 40)
        text4 = smallfont.render(str(level), True, color)
        screen.blit(text4, (100, 135))
        img4 = pygame.image.load('data/скелет.png')
        img4 = pygame.transform.scale(img4, (55, 30))
        img4 = pygame.transform.rotate(img4, 90)
        img4.set_colorkey((255, 255, 255))
        for t in range(acoint2):
            screen.blit(img4, (400 + t * 40, 25))
        text5 = smallfont.render(str(score), True, color)
        screen.blit(text5, (400, 135))
        text6 = smallfont.render(str(life), True, color)
        screen.blit(text6, (600, 135))
        #
        if da:
            ccur1 = pygame.image.load('data\cur.png').convert_alpha()
            MANUAL_CURSOR = ccur1
            MANUAL_CURSOR = pygame.transform.scale(MANUAL_CURSOR, (50, 50))
            MANUAL_CURSOR.set_colorkey((255, 255, 255))
            screen.blit(MANUAL_CURSOR, (mouse3)) 
        
        all_sprites.draw(screen)
        all_sprites2.draw(screen)

        mysprite.image = ccur2
        mysprite.image.set_colorkey((255, 255, 255))
        
        mysprite.rect.x = mouse[0]
        mysprite.rect.y = mouse[1]
        all_sprites1.draw(screen)

        if zwyk == 0:
            pygame.draw.line(screen, (255, 0, 0), (60, 15), (160, 100), 5)
        eat = level % 8
        if eat == 0:
            eat = 9
        for i in all_sprites:
            i.rect.x += i.speed
            for a in all_sprites1:
                sp = a
            
            if (i.rect.x <= mouse[0] <= i.rect.x + i.image.get_rect()[2] and i.rect.y <= mouse[1] + sizesize[level % 8 - 1][sizesize[level % 8 - 1].index((a.image.get_rect()[2], a.image.get_rect()[3]))][1] * 0.5 <= i.rect.y + i.image.get_rect()[3] and coor1 == 0 or\
                i.rect.x <= mouse[0] + sizesize[level % 8 - 1][sizesize[level % 8 - 1].index((a.image.get_rect()[2], a.image.get_rect()[3]))][0] <= i.rect.x + i.image.get_rect()[2] and i.rect.y <= mouse[1] + sizesize[level % 8 - 1][sizesize[level % 8 - 1].index((a.image.get_rect()[2], a.image.get_rect()[3]))][1] * 0.5 <= i.rect.y + i.image.get_rect()[3] and coor1 == 1) and\
               i.le + 8 * sizesize[i.le - 1].index((i.image.get_rect()[2], i.image.get_rect()[3])) <= eat + 8 * (acoint + 1):
                i.kill()
                acoint2 += 1
                s.play()
                score += 5
                if acoint2 == 6:
                    acoint += 1
                    if acoint == 3:
                        all_sprites.clear(screen, pygame.Surface(size))
                        all_sprites.draw(screen)
                        all_sprites1.clear(screen, pygame.Surface(size))
                        all_sprites1.draw(screen)
                        all_sprites2.clear(screen, pygame.Surface(size))
                        all_sprites2.draw(screen)
                        all_sprites4.clear(screen, pygame.Surface(size))
                        all_sprites4.draw(screen)
                        all_sprites = pygame.sprite.Group()
                        all_sprites1 = pygame.sprite.Group()
                        all_sprites2 = pygame.sprite.Group()
                        all_sprites4 = pygame.sprite.Group()
                        mysprite = FISH()
                        n = sizesize[level % 8][1]
                        level += 1
                        ccur2 = pygame.image.load(f'data/{fish[level % 8 - 1]}')
                        ccur2 = pygame.transform.scale(ccur2, n)
                        if coor1 == 0:
                            ccur2 = pygame.transform.flip(ccur2, True, False)
                        mysprite.image = ccur2
                        mysprite.image = pygame.transform.scale(mysprite.image, n)
                        mysprite.image.set_colorkey((255, 255, 255))
                        mysprite.rect = mysprite.image.get_rect()
                        mysprite.rect.x = -n[0]
                        mysprite.rect.y = random.randrange(300, 400)
                        all_sprites1.add(mysprite)
                        acoint = 0
                        acoint2 = 0
                        break
                    for a in all_sprites1:
                        sp = a
                    n = sizesize[level % 8 - 1][sizesize[level % 8 - 1].index((a.image.get_rect()[2], a.image.get_rect()[3])) + 1]
                    
                    all_sprites.clear(screen, pygame.Surface(size))
                    all_sprites.draw(screen)
                    all_sprites1.clear(screen, pygame.Surface(size))
                    all_sprites1.draw(screen)
                    all_sprites2.clear(screen, pygame.Surface(size))
                    all_sprites2.draw(screen)
                    all_sprites4.clear(screen, pygame.Surface(size))
                    all_sprites4.draw(screen)
                    all_sprites = pygame.sprite.Group()
                    all_sprites1 = pygame.sprite.Group()
                    all_sprites2 = pygame.sprite.Group()
                    all_sprites4 = pygame.sprite.Group()
                    mysprite = FISH()
                    ccur2 = load_image(fish[level % 8 - 1])
                    ccur2 = pygame.transform.scale(ccur2, n)
                    if coor1 == 0:
                        ccur2 = pygame.transform.flip(ccur2, True, False)
                    mysprite.image = ccur2
                    mysprite.image = pygame.transform.scale(mysprite.image, n)
                    mysprite.image.set_colorkey((255, 255, 255))
                    mysprite.rect = mysprite.image.get_rect()
                    mysprite.rect.x = -n[0]
                    mysprite.rect.y = random.randrange(300, 400)
                    all_sprites1.add(mysprite)
                    acoint2 = 0
                    break
                
            elif mouse[0] <= i.rect.x + i.image.get_rect()[2] <= mouse[0] + sizesize[level % 8 - 1][sizesize[level % 8 - 1].index((a.image.get_rect()[2], a.image.get_rect()[3]))][0] and mouse[1] <= i.rect.y + i.image.get_rect()[3] * 0.5 <= mouse[1] + sizesize[level % 8 - 1][sizesize[level % 8 - 1].index((a.image.get_rect()[2], a.image.get_rect()[3]))][1] and\
               i.le + 8 * sizesize[i.le - 1].index((i.image.get_rect()[2], i.image.get_rect()[3])) > eat + 8 * (acoint + 1):
                life -= 1
                acoint2 = 0
                s.play()
                all_sprites.clear(screen, pygame.Surface(size))
                all_sprites.draw(screen)
                all_sprites1.clear(screen, pygame.Surface(size))
                all_sprites1.draw(screen)
                all_sprites2.clear(screen, pygame.Surface(size))
                all_sprites2.draw(screen)
                all_sprites4.clear(screen, pygame.Surface(size))
                all_sprites4.draw(screen)
                all_sprites = pygame.sprite.Group()
                all_sprites1 = pygame.sprite.Group()
                all_sprites2 = pygame.sprite.Group()
                all_sprites4 = pygame.sprite.Group()
                mysprite = FISH()                
                mysprite.image = ccur2
                n = sizesize[level % 8 - 1][acoint]
                mysprite.image = pygame.transform.scale(mysprite.image, n)
                mysprite.image.set_colorkey((255, 255, 255))
                mysprite.rect = mysprite.image.get_rect()
                mysprite.rect.x = -n[0]
                mysprite.rect.y = random.randrange(300, 400)
                all_sprites1.add(mysprite)
                if life == 0:
                    pygame.mixer.music.stop()
                    running2 = False

                    imgov = load_image("игра окончена.jpg")
                    imgov = pygame.transform.scale(imgov, (800, 800))
                    screen.blit(imgov, (0, 0))
                    a = 0
                    pygame.display.update()
                    while a < 2400:
                        dt = clock.tick() 
                        a += dt
                    break
            if i.rect.x > 800:
                i.kill()
            all_sprites.update()

        for i in all_sprites2:
            i.rect.x -= i.speed
            for a in all_sprites1:
                sp = a
            if (i.rect.x <= mouse[0] + sizesize[level % 8 - 1][sizesize[level % 8 - 1].index((a.image.get_rect()[2], a.image.get_rect()[3]))][0] <= i.rect.x + i.image.get_rect()[2] and i.rect.y <= mouse[1] + sizesize[level % 8 - 1][sizesize[level % 8 - 1].index((a.image.get_rect()[2], a.image.get_rect()[3]))][1] * 0.5 <= i.rect.y + i.image.get_rect()[3] and coor1 == 1 or\
               i.rect.x <= mouse[0] <= i.rect.x + i.image.get_rect()[2] and i.rect.y <= mouse[1] + sizesize[level % 8 - 1][sizesize[level % 8 - 1].index((a.image.get_rect()[2], a.image.get_rect()[3]))][1] * 0.5 <= i.rect.y + i.image.get_rect()[3] and  coor1 == 0) and\
               i.le + 8 * sizesize[i.le - 1].index((i.image.get_rect()[2], i.image.get_rect()[3])) <= eat + 8 * (acoint + 1):
                i.kill()
                acoint2 += 1
                score += 5
                s.play()
                if acoint2 == 6:
                    acoint += 1
                    if acoint == 3:
                        all_sprites.clear(screen, pygame.Surface(size))
                        all_sprites.draw(screen)
                        all_sprites1.clear(screen, pygame.Surface(size))
                        all_sprites1.draw(screen)
                        all_sprites2.clear(screen, pygame.Surface(size))
                        all_sprites2.draw(screen)
                        all_sprites4.clear(screen, pygame.Surface(size))
                        all_sprites4.draw(screen)
                        all_sprites = pygame.sprite.Group()
                        all_sprites1 = pygame.sprite.Group()
                        all_sprites2 = pygame.sprite.Group()
                        all_sprites4 = pygame.sprite.Group()
                        mysprite = FISH()
                        n = sizesize[level % 8][1]
                        level += 1
                        ccur2 = load_image(fish[level % 8 - 1])
                        ccur2 = pygame.transform.scale(ccur2, n)
                        if coor1 == 0:
                            ccur2 = pygame.transform.flip(ccur2, True, False)
                        mysprite.image = ccur2
                        mysprite.image = pygame.transform.scale(mysprite.image, n)
                        mysprite.image.set_colorkey((255, 255, 255))
                        mysprite.rect = mysprite.image.get_rect()
                        mysprite.rect.x = -n[0]
                        mysprite.rect.y = random.randrange(300, 400)
                        all_sprites1.add(mysprite)
                        acoint = 0
                        acoint2 = 0
                        break
                    for a in all_sprites1:
                        sp = a
                    n = sizesize[level % 8 - 1][sizesize[level % 8 - 1].index((a.image.get_rect()[2], a.image.get_rect()[3])) + 1]
                    
                    all_sprites.clear(screen, pygame.Surface(size))
                    all_sprites.draw(screen)
                    all_sprites1.clear(screen, pygame.Surface(size))
                    all_sprites1.draw(screen)
                    all_sprites2.clear(screen, pygame.Surface(size))
                    all_sprites2.draw(screen)
                    all_sprites4.clear(screen, pygame.Surface(size))
                    all_sprites4.draw(screen)
                    all_sprites = pygame.sprite.Group()
                    all_sprites1 = pygame.sprite.Group()
                    all_sprites2 = pygame.sprite.Group()
                    all_sprites4 = pygame.sprite.Group()
                    mysprite = FISH()
                    ccur2 = load_image(fish[level % 8 - 1])
                    ccur2 = pygame.transform.scale(ccur2, n)
                    if coor1 == 0:
                        ccur2 = pygame.transform.flip(ccur2, True, False)
                    mysprite.image = ccur2
                    mysprite.image = pygame.transform.scale(mysprite.image, n)
                    mysprite.image.set_colorkey((255, 255, 255))
                    mysprite.rect = mysprite.image.get_rect()
                    mysprite.rect.x = -n[0]
                    mysprite.rect.y = random.randrange(300, 400)
                    all_sprites1.add(mysprite)
                    acoint2 = 0
                    break
                
            elif mouse[0] <= i.rect.x <= mouse[0] + sizesize[level % 8 - 1][sizesize[level % 8 - 1].index((a.image.get_rect()[2], a.image.get_rect()[3]))][0] and mouse[1] <= i.rect.y + i.image.get_rect()[3] * 0.5 <= mouse[1] + sizesize[level % 8 - 1][sizesize[level % 8 - 1].index((a.image.get_rect()[2], a.image.get_rect()[3]))][1] and\
                 i.le + 8 * sizesize[i.le - 1].index((i.image.get_rect()[2], i.image.get_rect()[3])) > eat + 8 * (acoint + 1):
                life -= 1
                acoint2 = 0
                s.play()
                all_sprites.clear(screen, pygame.Surface(size))
                all_sprites.draw(screen)
                all_sprites1.clear(screen, pygame.Surface(size))
                all_sprites1.draw(screen)
                all_sprites2.clear(screen, pygame.Surface(size))
                all_sprites2.draw(screen)
                all_sprites4.clear(screen, pygame.Surface(size))
                all_sprites4.draw(screen)
                all_sprites = pygame.sprite.Group()
                all_sprites1 = pygame.sprite.Group()
                all_sprites2 = pygame.sprite.Group()
                all_sprites4 = pygame.sprite.Group()
                mysprite = FISH()                
                mysprite.image = ccur2
                n = sizesize[level % 8 - 1][acoint]
                mysprite.image = pygame.transform.scale(mysprite.image, n)
                mysprite.image.set_colorkey((255, 255, 255))
                mysprite.rect = mysprite.image.get_rect()
                mysprite.rect.x = -n[0]
                mysprite.rect.y = random.randrange(300, 400)
                all_sprites1.add(mysprite)
                if life == 0:
                    running2 = False
                    pygame.mixer.music.stop()
                    
                    imgov = load_image("игра окончена.jpg")
                    imgov = pygame.transform.scale(imgov, (800, 800))
                    screen.blit(imgov, (0, 0))
                    a = 0
                    pygame.display.update()
                    while a < 2400:
                        dt = clock.tick() 
                        a += dt
                    break
            if i.rect.x < 0 - i.image.get_width():
                i.kill()
            all_sprites2.update()
        
        pygame.display.flip()
        clock1.tick(fp)
        pygame.display.update()
        dt = clock.tick() 
        time_elapsed_since_last_action += dt
        time_elapsed_since_last_action2 += dt
        time_elapsed_since_last_action3 += dt

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                level = 1
                life = 3
                coor1 = 1
                acoint = 0
                acoint2 = 0
                score = 0
                pl = 0
                pygame.mixer.music.stop()
                all_sprites.clear(screen, pygame.Surface(size))
                all_sprites.draw(screen)
                all_sprites1.clear(screen, pygame.Surface(size))
                all_sprites1.draw(screen)
                all_sprites2.clear(screen, pygame.Surface(size))
                all_sprites2.draw(screen)
                all_sprites4.clear(screen, pygame.Surface(size))
                all_sprites4.draw(screen)
                running2 = False
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if da:
                    if 60 <= mouse3[0] <= 160 and 15 <= mouse3[1] <= 100:
                        if zwyk == 0:
                            zwyk = 1
                            pygame.mixer.music.play(-1)
                        else:
                            zwyk = 0
                            pygame.mixer.music.pause()
        
pygame.quit()
