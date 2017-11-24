#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os
import StringIO
import Image, ImageFont, ImageDraw
import pygame
pygame.init()
f = open('output.txt','r')
text = f.readlines()
print text
im = Image.new("RGB", (1024, 800), (255, 255, 255))
font = pygame.font.Font(os.path.join('fonts','simsun.ttc'),12)
rtext = font.render(text, True, (0, 0, 0), (255, 255, 255))
sio = StringIO.StringIO()
pygame.image.save(rtext, sio)
sio.seek(0)
line = Image.open(sio)
im.paste(line,(10, 5))
im.show()
im.save("t.png")

