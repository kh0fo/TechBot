#!/usr/bin/python3

#LMGTFY module
#khofo

def main(nick, comargvs, chan, send):
    terms = '+'.join(comargvs.strip().split())
    base = 'https://lmgtfy.com/?q='
    link = base + terms
    send.put(link)
    if comargvs == 'help': send.put('Usage: !lmgtfy <word>')
