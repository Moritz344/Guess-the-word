import random
import os
from termcolor import cprint
os.system("cls" if os.name == "nt" else "clear")
print("+---------------------------------------------+")
cprint("Welcome to the 'Guess the word' Game!","green")
print("+---------------------------------------------+")
print()
word_list = [
    "abacus", "abalone", "abandon", "abdomen", "abiding", "ability", "abolish", "abridge", "absence", "absolve",
    "absorbs", "abstain", "absurd", "academy", "account", "accused", "accrue", "acerbic", "acetone", "achieve",
    "acquire", "acrobat", "activate", "adapted", "addicted", "address", "adeptly", "adhesive", "adjourn", "admiral",
    "admonish", "adrenal", "advance", "adverse", "advise", "aerial", "aerobic", "affable", "affirm", "afflict",
    "affront", "aflame", "afloat", "afraid", "against", "agenda", "aggravate", "agilely", "agitate", "agonize",
    "aground", "ailment", "aimless", "airport", "alarmed", "alcohol", "alertly", "algebra", "alias", "alibi",
    "alienate", "alleged", "allergic", "alliance", "allocate", "allude", "almanac", "aloof", "alphabet", "already",
    "alright", "altruism", "amazing", "ambiance", "ambition", "ambulance", "amend", "amiable", "amnesty", "amplify",
    "amputate", "amused", "anaconda", "anagram", "anatomical", "anchovy", "ancient", "android", "anecdote", "angelic",
    "angered", "angrily", "anguish", "animated", "annotate", "annually", "annuity", "anomaly", "anonymous", "answer",
    "antelope", "anxiety", "anybody", "apart", "apex", "apnea", "apology", "apostle", "apparel", "appealing",
    "appendix", "applause", "appraisal", "apricot", "aquarium", "arbiter", "arbitrary", "arcade", "archery",
    "ardently", "arena", "argument", "aristocrat", "armadillo", "armchair", "aromatic", "arouse", "arrogant", "arsenic",
    "artichoke", "artificial", "artisan", "ascend", "ashtray", "aside", "askew", "asleep", "asparagus", "assemble",
    "assured", "asthma", "athlete", "atomize", "atrium", "attire", "auburn", "auction", "auditor", "augmented",
    "auspicious", "authentic", "autumn", "avalanche", "avenue", "aviator", "avocado", "awaken", "awesome",
    "awhile", "awkward", "awning", "awoke", "axially", "azimuth", "babbling", "backbone", "backfield", "backfire",
    "backhand", "backlash", "backlog", "backpack", "backpedal", "backrest", "backroom", "backshift", "backside",
    "backtrack", "backup", "backward", "backwash", "backyard", "bacteria", "badass", "bagpipe", "bakery", "balance",
    "balloon", "bamboo", "banana", "bandage", "bankable", "banshee", "banter", "barbecue", "bargain", "barge",
    "barkless", "barley", "barmaid", "barometer", "baron", "barrel", "barrette", "barricade", "barstool", "bartender",
    "baseboard", "baseline", "basement", "bashful", "basic", "basket", "batboy", "bathrobe", "baton", "battalion",
    "battered", "battery", "battle", "bauble", "bazooka", "beaming", "bedrock", "beehive", "beeswax", "befriend",
    "beggar", "begonia", "behavior", "beige", "belittle", "bellhop", "belly", "beloved", "bench", "beneath",
    "benefit", "beside", "betray", "better", "bewildered", "bewitched", "bicycle", "bifocals", "bigfoot", "bikini",
    "bilingual", "biloxi", "bimonthly", "binocular", "biology", "biplane", "birth", "biscuit", "bite", "biweekly",
    "bizarre", "blatant", "blazer", "bleach", "blessing", "blimp", "blink", "blissful", "blizzard", "blowfish",
    "bluebird", "blunt", "blurred", "boatyard", "bobcat", "bogus", "bohemian", "boiler", "boldness", "bologna",
    "bolster", "bombshell", "bonanza", "bonded", "bonehead", "bonfire", "bookcase", "bookmark", "border", "borough",
    "bossiness", "bottle", "bottom", "bounce", "boxcar", "breeder", "brevity", "brickyard", "bridge", "briefcase",
    "brilliant", "brisket", "broadcast", "broken", "bronze", "broom", "brushes", "bubble", "buckle", "buddhist",
    "buffalo", "bullfrog", "bunny", "burrito", "busboy", "butterfly", "buying", "buzzard", "cable", "cadet",
    "caesarean", "cahoots", "cajoling", "cakewalk", "calculator", "calibrate", "calmness", "camera", "campaign",
    "canister", "cannon", "canopy", "capably", "capitol", "caramel", "caravan", "carbon", "carpet", "carport",
    "cartel", "cartridge", "carve", "cascade", "cassette", "casually", "catapult", "catch", "causeway", "caution",
    "cavalier", "cavernous", "caviar", "ceasefire", "cedar", "ceiling", "celery", "cement", "census", "ceramics",
    "cesspool", "champion", "chance", "changeable", "chaos", "chaplain", "charcoal", "charger", "chase",]

word = random.choice(word_list)
word_length = len(word)
guessed_letters = ['*' for _ in range(word_length)]
empty = []
tries = 15
print(" ".join(guessed_letters))

while '*' in guessed_letters:
     player_guess = str(input("Your guess: "))
     if player_guess in empty:
          cprint("Try a different letter!","red",attrs=["bold"])
     empty.append(player_guess)

     if tries == 1:
          cprint("You have no tries left!","red",attrs=["bold"])
          break

     if player_guess in word:
          for char in range(word_length):
               if word[char] == player_guess:
                    guessed_letters[char] = player_guess
          print(" ".join(guessed_letters))
     else:
          tries -= 1
          print("Incorrect guess. Tries left:",tries)
          

     if ''.join(guessed_letters) == word:
        cprint("Congratulations! You won. ","green", attrs=["bold"])
        break


