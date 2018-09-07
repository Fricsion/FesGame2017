#!/usr/bin/env python
#coding: utf-8
import urllib
import subprocess
import json
import sys

class Getdata(object):
	def __init__( self, music_id, music_name ):
		self.music_id = music_id
		self.base_url = "https://m.tianyi9.com/"
		self.music_name = music_name

		self.dl_dic()
		self.dl_music()
		self.dl_jacket()
		self.dl_beatmap()

	def dl_dic( self ):
		urllib.urlretrieve(self.base_url+"API/getlive?live_id="+self.music_id, 'data/'+self.music_name)
		file_open = open("data/"+self.music_name, "r")
		self.file_load = json.load( open("data/"+self.music_name, "r" ))

	def dl_music( self ):
#		for dic in open("data/"+self.music_name, "r"):
#			dictionary = dic
#
#			print dictionary
#			music_place = "data/"+self.music_name
#			urllib.urlretrieve( self.base_url+"upload/"+music_file ,music_place+".mp3")
#
#
#			subprocess.call("ffmpeg -i "+music_place+"mp3 -vn -ac 2 -ar 44100 -acodec pcm_s16le -fwav "+music_place+"wav") 
		
		music_file = self.file_load["content"]["bgm_path"]
		music_place = "data/"+self.music_name
		
		urllib.urlretrieve( self.base_url+"upload/"+music_file , music_place+".mp3")

		subprocess.call("ffmpeg -y -i "+music_place+".mp3 -vn -ac 2 -ar 44100 -acodec pcm_s16le -f wav "+music_place+".wav", shell=True ) 


	def dl_jacket( self ):
		
		jacket_file = self.file_load["content"]["cover_path"]
		jacket_place = "data/"+self.music_name

		urllib.urlretrieve( self.base_url+"upload/"+jacket_file, jacket_place+".png")
		

			
			

			
	def dl_beatmap( self ):

		map_file = self.file_load["content"]["map_path"]
		map_place = "data/"+self.music_name

		urllib.urlretrieve( self.base_url+"upload/"+map_file, map_place+".json")

#		fumen_open = open("data/"+self.music_name+".json", "r")
#		self.fumen_load = json.load( fumen_open )
	
		
	
		
		

Getdata("k0Zl8fed4nNTjMaJ", "DataErrOr")
Getdata("HxTWddIwQIbFy1Lv", "Sakura_iro_no_yume")
Getdata("TIO1xeTxuhSWguw6", "Step_by_step_up!!")
Getdata("U7EoVLxKQ2ymp6SR", "Friend_Shitai")
Getdata("6USYf8pLOkuOcabO", "Renai_Circulation")
Getdata("LfvNnEGivv5jRJrS", "Zenryoku_Summer")
Getdata("EU5JfT8vsNdaa88A", "Yokai_Watch")
Getdata("zRQkr3Sft3mFCKSd", "Japalipark")
Getdata("RhCpl4eu9UaQ8tIs", "Wing_of_piano")
Getdata("ChVZvjBU4f6kiu11", "God_save_the_girls")
Getdata("BbgD3HPNhrTewBC3", "Sun_set")
Getdata("Dje99W7wdtlxUwqz", "Love_letter")
Getdata("tBGeNILBfD4Y8HqL", "Anzu_Song")
Getdata("pe5psydLl1fm0qNw", "NO-POI")
Getdata("iI8lBXZ7wTDmBNCO", "Hanakanzashi")
Getdata("O9Lf9HpPXimQ57cE", "Jumping!")
Getdata("Z1sRQ0gWKGhfuXwZ", "Suger_song_and_bitter_step")



		
		

