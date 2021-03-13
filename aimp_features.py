import pyaimp as aimp
import os
import pp
from time import sleep

base_path = ''
path_title = 'song_playing.txt'
path = os.path.join(base_path, path_title)


def export_file(file_path, text):
    with open(file_path, 'w') as f:
        f.write(text)
        print(text)


def song_title_sleep(client):
    song_duration = client.get_current_track_info()['duration']/1000
    how_far_into_song = client.get_player_position()/1000
    return song_duration - how_far_into_song


while True:
    try:
        client = aimp.Client()
        state = client.get_playback_state()
        client_states = [aimp.PlayBackState.Playing, 
                         aimp.PlayBackState.Paused]

        if state in client_states:
            time_to_sleep = song_title_sleep(client) + 1
            print(time_to_sleep)
            export_file(path, client.get_current_track_info()['title'])
            sleep(time_to_sleep)
    except RuntimeError as re: # AIMP instance not found
        print(re)
    except Exception as e:
        print(e)