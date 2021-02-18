import random
<<<<<<< HEAD

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
=======
happy_emojis = ["😀", "😃" ,"😄" ,"😁" ,"😆" ,"😊" ,"😇" ,"🙂", "🤗", "🤭"]

sad_emojis = ["😞" ,"😔" ,"😟" ,"😕" ,"🙁" ,"☹️", ,"😣" ,"😖" ,"😫" ,"😩" ,"😢" ,"😭" ,"😨" ,"😰" ,"😥" ,"😓"]

eyeglasses_emojis = ["🤓" ,"😎"]

hand_emojis = [
    "👋" ,"🤚" ,"🖐" ,"✋" ,"🖖" ,"👌" ,"🤏" ,"✌️" ,"🤞" ,"🤟" ,"🤘" ,"🤙" ,"👈" 
    ,"👉" ,"👆" ,"👇" ,"☝️" ,"👍" ,"👎" ,"✊" ,"👊" ,"🤛" 
    ,"🤜" ,"👏" ,"🙌" ,"👐" ,"🤲" ,"🤝" ,"🙏"]



def happy():
    return random.choice(happy_emojis)

def sad():
    return random.choice(sad_emojis)


print(hand_emojis[0])

"""
penggunaan 
import emojis
print(emojis.happy())

"""
>>>>>>> 7075a7a69a6b05109612094521e7f6e80bfb1a9a
