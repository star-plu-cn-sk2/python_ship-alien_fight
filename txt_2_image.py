#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os
import StringIO
import Image, ImageFont, ImageDraw
import pygame
pygame.init()
#text = u'this is test txt, test 123.'
f = open('output.txt','r')
text = f.read()
#im = Image.new("RGB", (300, 50), (255, 255, 255))
im = Image.new("RGB", (400, 400), (255, 255, 255))
#font = pygame.font.Font(os.path.join('fonts','simsun.ttc'),14)
font = pygame.font.Font(os.path.join('fonts','simsun.ttc'),9)
rtext = font.render(text, True, (0, 0, 0), (255, 255, 255))
sio = StringIO.StringIO()
pygame.image.save(rtext, sio)
sio.seek(0)
line = Image.open(sio)
im.paste(line,(10, 5))
im.show()
im.save("t.png") 
