# LOTS OF ERRORS NEEDS TESTING

#Usage !IQ <add:remove> <nick> <smart:dumb>
       #!IQ list <dumb:smart>
       #!IQ is <nick> <dumb:smart>

def main(nick, comargvs, chan, send ):
    smart  = list('khofo')
    dumb = list()
    helplist = ['h', '--help', 'help', 'wtf', 'usage', '-h']
    NumArgs = comargvs.strip().split()

    #Admin access to list
    if NumArgs[0].lower() == 'add' or 'remove' and NumArgs[2].lower() == 'smart' or 'dumb':
        if nick.lower() == 'khofo':
            if NumArgs[2].lower() == 'smart' and NumArg[0] == 'add': smart.append(NumArgs[1])
            if NumArgs[2].lower() == 'smart' and NumArgs[0].lower() == 'remove': smart.remove(NumArgs[1])         
            if NumArgs[2].lower() == 'dumb' and NumArgs[0].lower() == 'add': dumb.append(NumArgs[1])
            if NumArgs[2].lower() == 'dumb' and NumArgs[0].lower() == 'remove': dumb.remove(NumArgs[1])
        else: send.put("You don't have permission to do this")
    
    #See if somene is dumb or not
    elif  NumArgs[0].lower() == 'is' and NumArgs[2].lower() == 'smart' or 'dumb':
        if NumArgs[2].lower() == 'smart' and NumArgs[1] in smart: send.put('Yes, ' + str(NumArgs[1]) + ' is smart')
        elif NumArgs[2].lower() == 'dumb' and NumArgs[1] in dumb: send.put('Yes, ' + str(NumArgs[1]) +' is dumb')
        elif NumArgs[2].lower() == 'dumb' or 'smart' and NumArgs[1] not in dumb or smart: send.put('Cant find ' + str(NumArgs[1]) + ' :/, maybe ask khofo to add it, voting option coming soon')
    
    #Returns Lists
    elif NumArgs[0].lower() == 'list' and   NumArgs[1].lower() == 'dumb' or 'smart':
        if NumArgs[1].lower() == 'dumb': send.put(', '.join(dumb))
        if NumArgs[1].lower() == 'smart': send.put(', '.join(smart))

    #Return number of people in List
    elif   NumArgs[0].lower() == 'count' and NumArgs[1].lower() == 'dumb' or 'smart':
        if NumArgs[1].lower() == 'dumb': send.put(len(dumb) - 1)
        if NumArgs[1].lower() == 'smart': send.put(len(smart) - 1)

#Usage Info
    elif lower(comargvs) in helplist:
        send.put(("Usage: !IQ <list/count/is> <nick> <dumb/smart>, Example !IQ is %s dumb" % nick))

    else:
        send.put('Try !IQ help')