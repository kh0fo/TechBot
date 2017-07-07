# #!/bin/python3
# #NOT WORKING

# # Bug Module for TechBot
# # By: Khofo
# # Version: 1.3
# # Last Modified: 28/10/2016

# #Format .bug <target> <number of times to send the message> <delay between each message> <message>
# import time
# from time import gmtime, strftime

# process_c = 100
# process_id = None
# args = None  
# count = 0
# process_tuple = []

# def main(nick, chan, comargs, send):
#     parse(comargs)

# def process_log(process_tuple, nick, chan, comargs, process_c, count, process_id):
#     process_c = process_c + 1
#     time = strftime("%H%M%S", gmtime())
#     process_id = str(time)+str(nick)+str(chan)+str(process_c)
#     send.put("%s, this is you process ID: %s" % nick, process_id)
#     process_tuple.append(process_id)


# def parse(comargs, process_id, process_tuple, nick):
#     args = comargs.split()
#     try:
#         len(args) >= 4
#         args[0].strip() = t_nick 
#         args[1].strip() = int(msg_count)
#         args[2].strip() = int(dl)
#         args[3:].strip() = msg

#         process_log(process_tuple, nick, chan, comargs, process_c, count, process_id)
#         print(str(t_nick) + str(msg_count) + str(dl) + str(msg))
#     except:
#         arg1 = str(args[0]).lower()

#         if arg1 in ["help","h"]:
#     	    send.put(("Usage: .bug <target> <number of times to send the message> <delay between each message> <message>"), nick)
        
#         elif arg1 == "stop":
#             stop(t_nick, send, nick)
        
#         elif arg1 == "tuple":
#             send.put((process_tuple, nick))

#     	else:
#     		send.put("""Bad input, check ".bug help" for usage information""")

# def bug(t_nick, msg_count, dl, msg, send):
#     for i in range(msg_count):
#         send.put((msg, t_nick))
#         time.sleep(dl)


# def stop(t_nick, send, nick):
#     for process in process_tuple:
#         if process[]
#     send.put(("The process with process ID: %s will abort in 10s", % to_abort_process, nick)
#     time.sleep(10)
#     send.put(("Stopped bugging %s" % t_nick, nick))
#     send.put(("THE BOT WILL NOW CRASH %s" %t_nick, nick))
#     sys.exit()