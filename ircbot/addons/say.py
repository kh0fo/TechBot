# # Bug Module for TechBot
# # By: Khofo
# # Version: 1.2
# # Last Modified: 20/10/2016

# #Format .bug <target> <number of times to send the message> <delay between each message> <message>  

# count = 0
# process_c = 100
# process_id = None
# args = None


# def main(nick, chan, comargvs, send):
# 	parse(comargs)

# def process_log(nick, chan, comargs, process_c):
# 	process_c = process_c + 1
# 	process_id = process_id_ + str(count)
#     process_id = str(nick)+str(chan)+str(process_c)
#     count = count + 1
#     p rint(str(process_id_))
# 	print(process_id)


# def parse(comargs):
#     args = comargs.split()
#     try:
#         len(args) >= 4
#         args[0].strip() = t_nick 
#         args[1].strip() = int(msg_count)
#         args[2].strip() = int(dl)
#         args[3:].strip() = msg

#         process_log(nick, chan, comargs)
#         print(str(t_nick) + str(msg_count) + str(dl) + str(msg))
#     except:
#     	help = ("help","h")
#     	if str(args[0]).lower() in help:
#     	    print("Usage: .bug <target> <number of times to send the message> <delay between each message> <message>")
#     	else:
#     		print("""Bad input, check ".bug help" for usage information""")