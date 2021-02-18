import random

# --------------- LIST EMOJIS/EMOTICONS ---------------
happy_emojis = ["😀", "😃" ,"😄" ,"😁" ,"😆" ,"😊" ,"😇" ,"🙂", "🤗", "🤭"]

sad_emojis = ["😞" ,"😔" ,"😟" ,"😕" ,"🙁" ,"☹️", "😣" ,"😖" ,"😫" ,"😩" ,"😢" ,"😭" ,"😨" ,"😰" ,"😥" ,"😓"]

eyeglasses_emojis = ["🤓" ,"😎"]

waving_hands = ["👋" ,"🤚" ,"🖐" ,"✋", "🙌", "🤟"]

pointing_hands = ["🤙" ,"👈" ,"👉" ,"👆" ,"👇" ,"☝️" ,"👍"]


# --------------- FUNCTIONS --------------- 
# function untuk generate random happy emoji
def happy():
	return random.choice(happy_emojis)

# function untuk generate random sad emoji
def sad():
	return random.choice(sad_emojis)

# function untuk generate random waving hands emoji
def handWaves():
	return random.choice(waving_hands)
