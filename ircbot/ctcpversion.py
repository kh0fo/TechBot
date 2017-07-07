
def main(nick, comargs, chan, send):
    '''nick is who sent the command, type string
    comargvs is anything after the command, such as a website or other supporting args, type string
    chan is either the channel to send to, or our own nick in which case is a private message
    send is now a queue. So we need to 'put' things into it.'''

    # example on sending a simple string to the default channel the bot is on
    send.put(("\001VERSION\001", comargs))
