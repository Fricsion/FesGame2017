#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys
import math
import random
import json
import sys

NOTE_VISIBLE = 1000
JUDGE_RANGE = (50, 100, 150)
R = 280
S = 40
KEYCODE = (K_q,K_w,K_e,K_r,K_t,K_y,K_u,K_i,K_o)


class Otoge(object):
	def __init__(self):
		pygame.mixer.pre_init(frequency=44100, size=-16, channels=2)
		pygame.init()
		pygame.mixer.set_num_channels(16)
		self.SCR_RECT = Rect(0, 0, 640, 480)
		self.screen = pygame.display.set_mode((640, 480))
		pygame.display.set_caption("Otoge")
		self.sysfont = pygame.font.SysFont(None, 40)
		self.frame = 0
		self.clock = pygame.time.Clock()
		self.x = 0
		self.t = -3000
		#great, good, bad, miss
		self.judged = [0, 0, 0, 0]
		self.combo = 0
		self.judge_show = None

		# Load SE
		pushed_great = pygame.mixer.Sound("great.wav")
		pushed_good = pygame.mixer.Sound("good.wav")
		pushed_bad = pygame.mixer.Sound("bad.wav")
		self.pushed_sound = [ pushed_great, pushed_good, pushed_bad ]

		# Load Images
		self.note_hop = self.load_image("hop.png")
		self.note = self.load_image("note.png")
		tget_q = self.load_image("target_q.png")
		tget_w = self.load_image("target_w.png")
		tget_e = self.load_image("target_e.png")
		tget_r = self.load_image("target_r.png")
		tget_t = self.load_image("target_t.png")
		tget_y = self.load_image("target_y.png")
		tget_u = self.load_image("target_u.png")
		tget_i = self.load_image("target_i.png")
		tget_o = self.load_image("target_o.png")

		self.targets = [tget_q, tget_w, tget_e, tget_r, tget_t, tget_y, tget_u, tget_i, tget_o]

		self.music_flag = 0

		self.music_names = ["DataErrOr","Sakura_iro_no_yume","Step_by_step_up!!","Friend_shitai","Renai_Circulation","Zenryoku_Summer","Yokai_Watch","Japalipark","Wing_of_piano","Sun_set","Love_letter","Anzu_Song","No-POI","Hanakanzashi","Jumping!","Suger_song_and_bitter_step"]


		self.gamemode = 0
		# 0 => Select,  1 => Play

		self.play_image = pygame.image.load("back_image.png").convert()
		self.menu_image = pygame.image.load("select.png").convert()
		self.result_image = pygame.image.load("result.png").convert()

		self.main()

	def select_menu( self ):

		self.screen.blit( self.menu_image, (0, 0))

		jacket_image = self.load_image( "data/"+self.music_names[self.music_flag]+".png" )
		jacket_image = pygame.transform.scale( jacket_image, (200, 200))

		self.screen.blit( jacket_image, (320, 240))
		self.screen.blit(self.sysfont.render(str(self.music_names[self.music_flag]), False, (0, 0, 0)), (250, 220))

		pygame.display.update()

		for event in pygame.event.get():
			if event.type == QUIT: sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_LEFT:
					if self.music_flag > 0:
						self.music_flag = self.music_flag - 1

				if event.key == K_RIGHT:
					if self.music_flag < len(self.music_names)-1:
						self.music_flag = self.music_flag + 1

				if event.key == K_SPACE:
					self.music_name = self.music_names[ self.music_flag ]
					self.gamemode = 1
					self.load()

				elif event.key == K_ESCAPE:
					sys.exit()

	def play_screen( self ):

		self.screen.blit( self.play_image, (0, -16))
		self.update()
		self.getkey()
		self.draw()

		#self.screen.blit(self.sysfont.render("t="+str(self.frame), False, (0,0,0)), (0,0))
		#self.screen.blit(self.sysfont.render("dt="+str(self.dt), False, (0,0,0)), (0,30))


		self.dt = self.clock.get_time()
		self.t += self.dt

		now = pygame.mixer.music.get_pos()
		if now < 0:
			self.gamemode = 2




		self.screen.blit(self.combo_text, self.combo_text.get_rect(center=(320,310)))
		self.screen.blit(self.judge_text, (320, 210))
		#self.screen.blit(self.sysfont.render("judged="+str(self.judged), False, (0,0,0)), (0,450))
		pygame.display.update()
		self.frame += 1

		#if self.notes

	def result_screen( self ):

		self.screen.blit(self.result_image, (0, 0))

		self.screen.blit(self.sysfont.render( str(self.music_name), False, (0, 0, 0)), (150, 160))



		self.screen.blit(self.sysfont.render( str(self.judged[0]), False, (0, 0, 0)), (380, 230))
		self.screen.blit(self.sysfont.render( str(self.judged[1]), False, (0, 0, 0)), (380, 300))
		self.screen.blit(self.sysfont.render( str(self.judged[2]), False, (0, 0, 0)), (380, 370))
		self.screen.blit(self.sysfont.render( str(self.judged[3]), False, (0, 0, 0)), (380, 420))

		pygame.display.update()
		for event in pygame.event.get():
			if event.type == QUIT: sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_SPACE:
		#			self.t = 0
		#			self.judged = [0, 0, 0, 0]
		#			self.
					self.__init__()
					self.gamemode = 0


	def load(self):
		fumen_open = open("data/"+self.music_name+".json", "r" )
		self.fumen_load = json.load( fumen_open )
		self.notes = [[] for i in xrange(9)]

		self.music_file = self.music_name+".wav"

		pygame.mixer.music.load( "data/"+self.music_file )
		pygame.mixer.music.play()

		for i in self.fumen_load["lane"]:

			for j in i:
				note = {}
				note["sec"] = j["starttime"] - 3000

				note["exist"] = False

				lane_num = j["lane"]
				self.notes[lane_num].append(note)



	def update(self):
		#Append
		for i in xrange(9):
			for j in xrange(len(self.notes[i])):
				if self.notes[i][j]["sec"] - NOTE_VISIBLE <= self.t:
					if not self.notes[i][j]["exist"]:
						self.notes[i][j]["exist"] = True
				else:
					break

		#Delete
		for i in xrange(9):
			for j in xrange(len(self.notes[i])):
				if j + 1 <= len(self.notes[i]) and self.notes[i][j]["sec"] + JUDGE_RANGE[2] <= self.t:
					del self.notes[i][j]
					#print "MISS", i
					self.judged[3] += 1
					self.combo = 0
				else:

					break

	def draw(self):
		#center
		self.screen.blit( self.note_hop, ( 320-50, 100-50))

		for i in xrange(9):
			self.screen.blit( self.targets[i], (int(320 + R * math.cos(math.radians(180-22.5*i)))-50,int(100 + R * math.sin(math.radians(180-22.5*i)))-50))
			for j in xrange(len(self.notes[i])):
				if not self.notes[i][j]["exist"]:
					break
				r = (-self.notes[i][j]["sec"] + self.t + NOTE_VISIBLE) * R / NOTE_VISIBLE
				s = 10 + (-self.notes[i][j]["sec"] + self.t + NOTE_VISIBLE) * (S-8) / NOTE_VISIBLE
				#notes
				pygame.draw.circle(self.screen, (125,128,72), (int(320 + r * math.cos(math.radians(180-22.5*i))),int(100 + r * math.sin(math.radians(180-22.5*i)))), int(s))



	def getkey(self):
		for event in pygame.event.get():
			if event.type == QUIT:
					sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					sys.exit()
				if event.key == K_RETURN:
					pygame.mixer.music.stop()
					self.gamemode = 2

				for i in xrange(9):
					if event.key == KEYCODE[i]:

						self.judge(i)

	def judge(self, i):
		note = None
		for j in xrange(len(self.notes[i])):
			if self.notes[i][j]["exist"] and self.notes[i][j]["sec"] - JUDGE_RANGE[2] <= self.t:
				note = self.notes[i][j]
				del self.notes[i][j]
				break

		if not note:
			return
		diff = abs(note["sec"] - self.t)
		for k in xrange(3):
			if diff <= JUDGE_RANGE[k]:
				self.judged[k] += 1
				if 0 <= k <= 1:
					self.combo += 1
				else:
					self.combo = 0
				self.pushed_sound[k].play()
				#print ["GREAT", "GOOD", "BAD"][k], i
				self.judge_show = ["Great!!", "Good!", "Bad..."][k]
				return

	def load_image( self,filename ):
		image = pygame.image.load( filename ).convert_alpha()
		return image

	def main(self):
		while True:
			self.combo_text = self.sysfont.render("Combo:"+str(self.combo), False, (0,0,0))
			self.judge_text = self.sysfont.render(str(self.judge_show), False, ( 120, 120, 120 ))
			self.clock.tick()
#			self.screen.fill((255,255,255))

			if self.gamemode == 0:
				self.select_menu()
			if self.gamemode == 1:
				self.play_screen()
			if self.gamemode == 2:
				self.result_screen()

Otoge()
