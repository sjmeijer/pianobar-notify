import ntfy

# Notify when a song starts.
NOTIFY_SONG_START = True

# Notify when a song ends.
NOTIFY_SONG_END = False

# Notify when a song is loved.
NOTIFY_SONG_LOVE = True

# Notify when a song is banned.
NOTIFY_SONG_BAN = True

# Notify when a song is shelved.
NOTIFY_SONG_SHELVE = True

# Notify when a song is bookmarked.
NOTIFY_SONG_BOOKMARK = True

# Notify when an artist is bookmarked.
NOTIFY_ARTIST_BOOKMARK = True

# Notify on program error.
NOTIFY_PROGRAM_ERROR = True

# Notify on network error.
NOTIFY_NETWORK_ERROR = True


def main():
    pass

def send_notification(title="",body=""):
    """
    This part actually pushes the notification to the notification center thing.
    I sanitize the title and body because a weird song name could probably mess things up.
    """
    try:
        ntfy.notify(message=sanitize(body),title=sanitize(title))
    except Exception as e:
        print(e)
    
def sanitize(string):
    """
    Remove some things that might be a bad idea
    """
    return string.encode("utf8","ignore")

if __name__=="__main__":
    print(argv)
    exit()
    main()
