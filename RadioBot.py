import requests
import json

class RadioBot:

	def __init__(self, room_id='572b753701726223009ec534', sid= "s%3ARBB9d-vOmWyhVO9Kgza5rpjCODIKwOkb.D0o%2FFoRlZPjFCESQGX9lMvSQi6wnfWW7O06KER32rrU"):
		self.room_id = room_id
		self.cookies = {'connect.sid':sid}

	def get_active(self):
		#Request for now playing
		now_playing = ''
		r = requests.get('https://api.dubtrack.fm/room/'+self.room_id+'/playlist/active')
		try: 
			now_playing = r.json()['data']['songInfo']['name']
		except KeyError:
			now_playing = 'Empty'
		now_playing = '<b>NOW PLAYING:</b> \n'+ now_playing + '\n'
		return now_playing

	def get_playlist(self):
		playlist_songs = ''
		r = requests.get('https://api.dubtrack.fm/room/'+self.room_id+'/playlist/details', cookies=self.cookies)
		for song in r.json()['data']:
			playlist_songs += song['_song']['name'] + '\n'
		if playlist_songs=='':
			playlist_songs = 'Empty'
		playlist = '<b>PLAYLIST:</b> \n'+ playlist_songs + '\n'
		return playlist
		
	def get_message(self):
		return self.get_active() + self.get_playlist() + '\n' + 'https://www.dubtrack.fm/join/knifechicken'