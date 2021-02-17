import random
happy_emojis = ["😀", "😃" ,"😄" ,"😁" ,"😆"]

sad_emojis = ["😞" ,"😔" ,"😟" ,"😕" ,"🙁" ,"☹️"]

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