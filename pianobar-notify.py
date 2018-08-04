#!/usr/bin/env python
# -*- coding: utf-8 -*-

import terminal_notifier as tn
import ntfy
import os, sys

# Notify when a song starts.
NOTIFY_SONG_START = True

# Notify when a song ends.
NOTIFY_SONG_END = False

# Notify when a song is loved.
NOTIFY_SONG_LOVE = True

# Notify when a song is banned.
NOTIFY_SONG_BAN = True

# Notify when a song is shelved.
NOTIFY_SONG_SHELF = True

# Notify when a song is bookmarked.
NOTIFY_SONG_BOOKMARK = True

# Notify when an artist is bookmarked.
NOTIFY_ARTIST_BOOKMARK = True

# Notify on program error.
NOTIFY_PROGRAM_ERROR = True

# Notify on network error.
NOTIFY_NETWORK_ERROR = True


def main():

    os.system("echo \"{}\" > /Users/smeijer/.config/pianobar/test.txt\n".format(sys.argv))

    notification_type = parse_input_type()

    pbn = Pianobar_Notifier()
    pbn.get_info()
    pbn.parse_info()

    # Here I handle all the different types of notications differently
    # If it is `pass`-ing, I haven't decided what I want to do yet

    if(notification_type=='songstart' and NOTIFY_SONG_START):
        pbn.send_notification(
            title       = pbn.title,
            subtitle    = 'By: "{}"'.format(pbn.artist),
            message     = 'On: "{}" @ {}'.format(pbn.album, pbn.station),
            image_url   = pbn.image_url)
    elif(notification_type=='songfinish' and NOTIFY_SONG_END):
        pbn.send_notification(
            title       = pbn.title,
            subtitle    = 'By: "{}"'.format(pbn.artist),
            message     = 'On: "{}" @ {}'.format(pbn.album, pbn.station),
            image_url   = pbn.image_url)
    elif(notification_type=='songlove' and NOTIFY_SONG_LOVE):
        pbn.send_notification(
            title       = "Loving song...",
            subtitle    = pbn.title,
            message     = "By \"{}\" on \"{}\"".format(pbn.artist, pbn.album),
            image_url   = pbn.image_url)
    elif(notification_type=='songban' and NOTIFY_SONG_BAN):
        pbn.send_notification("Banning song...","{}, by {}".format(pbn.title,pbn.artist))
    elif(notification_type=='songshelf' and NOTIFY_SONG_SHELF):
        pass
    elif(notification_type=='songbookmark' and NOTIFY_SONG_BOOKMARK):
        pass
    elif(notification_type=='artistbookmark' and NOTIFY_ARTIST_BOOKMARK):
        pass

    if(pbn.info[u'pRet'] != 1 and NOTIFY_PROGRAM_ERROR):
        pass
    if(pbn.info[u'wRet'] != 0 and NOTIFY_NETWORK_ERROR):
        pbn.send_notification("Network Error","")

    exit()


def parse_input_type():
    input_vals = sys.argv
    input_type = input_vals[1]

    return input_type

class Pianobar_Notifier():

    def __init__(self):
        self.info = {}

    def parse_info(self):
        """
            Get the important details out and store them in class variables.
        """

        # The info dict contains, among other things:
        # 'artist': 'Joe Pass', 
        # 'title': 'By Myself', 
        # 'album': 'Blues For Fred', 
        # 'coverArt': 'http://cont-1.p-cdn.us/images/public/rovi/albumart/5/2/1/3/025218093125_500W_500H.jpg', 
        # 'stationName': 'QuickMix', 
        # 'songStationName': 'Jazz Guitar Radio', 
        # 'pRet': 1, 
        # 'pRetStr': 'Everything is fine :)', 
        # 'wRet': 0, 
        # 'wRetStr': 'No error',
        # 'songDuration': 262,
        # ...

        self.artist = self.info['artist']
        self.title = self.info['title']
        self.album = self.info['album']
        self.image_url = self.info['coverArt']
        try:
            self.station = self.info['songStationName']
        except KeyError:
            self.station = self.info['stationName']
        
        try:
            self.duration = self.info['duration']
        except KeyError as e:
            pass

    def get_info(self):
        """
        The pianobar app just dumps all the info into stdin
        This parses the pile of stuff in stdin into a dictionary
        """

        for line in sys.stdin:
            os.system("echo \"{}\" >> /Users/smeijer/.config/pianobar/test3.txt\n".format(line))
            key, delimiter, value = str(line).strip().partition(u'=')
            if value.isdigit():
                self.info[key] = int(value)
            else:
                self.info[key] = value
        
        os.system("echo \"{}\" > /Users/smeijer/.config/pianobar/test2.txt\n".format(self.info))
        return self.info

    def send_notification(self,title="", body="", subtitle=None, message=None, image_url=None):
        """
        This part actually pushes the notification to the notification center thing.
        It uses terminal_notifier if you pass it an image and a message
        Otherwise it just uses ntfy
        I sanitize the title and body because a weird song name could probably mess things up.
        """

        if image_url is not None and message is not None:
            try:
                tn.notify(
                    title=title, 
                    subtitle=subtitle, 
                    message=message,
                    appIcon=image_url
                    )
            except:
                pass
        else:
            try:
                ntfy.notify(message=body,title=title)
                # ntfy.notify(message=self.sanitize(body),title=self.sanitize(title))
            except Exception as e:
                print(e)
        
    def sanitize(self,string):
        """
        Remove some things that might be bad?
        This probably isn't really necessary, but good to have it around.
        """
        return string.encode("utf8","ignore")

if __name__=="__main__":
    main()
