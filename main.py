from roblox_api_wrapper import login, message

recipient = "targetsusername"
sender = "ROBLOX"

messagesubject = f"Critical Security Alert for {recipient}"
messagecontent = '''
Official Support Message.

Your Roblox account has been compromised and a password reset is needed.
You can reset your password with the link below.

"yourlinkhere"
'''

messagecontent = {"subject": messagesubject, "content": messagecontent}

user = login.userpasslogin(sender, None)
message = message.send(user, recipient, messagecontent)
