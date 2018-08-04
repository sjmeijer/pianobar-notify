# Dependencies

This obviously uses pianobar. If you're not using pianobar, why are you here?
> brew install pianobar

To get the notification to work smoothly with OS X, I considered a few options. 
The `ntfy` project seemed pretty good, but it didn't have obvious support for passing an image URL in, so I have left it behind. It isn't hard to add it back in, if you really want.

In the end, I found a small Ruby package called [terminal-notifier](https://github.com/julienXX/terminal-notifier) which you can install with brew as well

```
brew install terminal-notifier
```

Then, I use [a handy python binding](https://github.com/looking-for-a-job/terminal-notifier.py) that sits on top of this:

`pip install terminal-notifier`

Then to get the whole thing to work, clone this repo somewhere, and copy the pianobar-notify.py into `~/.config/pianobar`.

```
cd ~/fun-place
clone github.com/sjmeijer/pianobar-notify
cd pianobar-notify
cp pianobar-notify.py ~/.config/pianobar
```

Then the last thing you should need to do is copy this into your config file (which may not exist if you haven't poked around with pianobar before)
```
echo "event_command = /Users/$USER/.config/pianobar/pianobar-notify.py" >> /Users/$USER/.config/pianobar/config
```

# Future Work
In the future, I could probably add in a script that would do all of this at once, but its easy enough that I'm not really sure its worth it.

This should all work as it sits, but it has only been tested on MacOS 10.11.6. I'd be curious to know if you break it.

# License

This code is somewhat inspired by [pianobar-growl](https://github.com/sorin-ionescu/pianobar-growl), which gave rise to all the constant names I used.