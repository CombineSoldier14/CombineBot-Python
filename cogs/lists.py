import discord
from discord.ext import commands
import os
statuses = [
    {
        "type":"PLAYING",
        "status":"https://combinebot.blogspot.com"
    },
    {
        "type":"WATCHING",
        "status":"you :)"
    },
    {
        "type":"PLAYING",
        "status":"Half-Life"
    },
    {
        "type":"PLAYING",
        "status":"inside Combine's Raspberry Pi",
    },
    {
        "type":"PLAYING",
        "status":"in the Python CMD",
    },
    {
        "type":"PLAYING",
        "status":"Ace Attorney: Dual Destinies",
    }

]




aaquotes = [
                       """
                       > *"Almost Christmas means it wasn't christmas!"* 
                       - Phoenix Wright, *Phoenix Wright: Ace Attorney*
                       """,
"""
> *"You are not just a clown. You are the entire circus"* 
- Miles Edgeworth, *Ace Attorney: Justice for All*
""",
"""
> *"Let's see those molars, Wright."*
- Miles Edgeworth
""",
"""
> *"That's it! I'm not doing a single cent of my taxes!"*
- Ema Skye, *Ace Attorney: Spirit of Justice*
""",
"""
> *"If you mess with The Best you will fall like the rest!"*
- Sebastian Debeste, *Ace Attorney: Investigations 2*
""",
"""
> *"If the pee ain't clear, death is near!"*
- Sebastian Debeste, *Ace Attorney: Investigations 2*
""",
"""
> *"Let's be scientific about this, please! Just put it in your pocket"*
- Ema Skye, *Phoenix Wright: Ace Attorney*
""",
"""
> *"You are the most foolishly foolish fool of a fool I have ever seen, Mr. Phoenix Wright!"*
- Franziska von Karma, *Ace Attorney: Justice for All*
""",
"""
> *"Blacker than a moonless night, hotter and more bitter than hell itself, that is coffee."*
- Godot *Ace Attorney: Trials and Tribulations*
""",
"""
> *"I'm Apollo Justice and I'm FINE!!!!"*
- Apollo Justice, *Ace Attorney: Dual Destinies*
""",
"""
> *"Apollo, tie me up in a new pose! Wait, you're not into this kinda thing, are you...?"*
- Athena Cykes, *Ace Attorney: Dual Destinies*
""",
"""
> *"You've come to the Wright place!"*
- Trucy Wright, *Apollo Justice: Ace Attorney*
""",
"""
> *"It appears the witness had several... sugar daddies."*
- Winston Payne, *Phoenix Wright: Ace Attorney*
""",
"""
> *"When something smells, it's usually the Butz*"
- Phoenix Wright, *Phoenix Wright: Ace Attorney*
""",
"""
> *"In justice we TRUST!"*
- Bobby Fulbright, *Ace Attorney: Dual Destinies*
""",
"""
> *"You asked for the enlargement, you got the enlargement."*
- Manfred von Karma, *Phoenix Wright: Ace Attorney*
""",
"""
> *"Say \"Hi\", for me, ok? Oh, and '/screw you'/."*
- Daryan Crescend, *Apollo Justice, Ace Attorney*
""",
"""
> *"The miracle never happen."*
- Phoenix Wright, *Ace Attorney: Justice for All*
""",
"""
> *"Oh, I assure you, it's quite based."*
- Phoenix Wright, *Apollo Justice: Ace Attorney*
""",
"""
> *"Why can't we have a normal, straightforward killing once in a while in this country?"*
- Ema Skye, *Apollo Justice: Ace Attorney*
""",
"""
> *"A lawyer only cries once it's all over."*
- Diego Armando/||Godot||
""",
"""
> *"This place is so fruity!"*
- Maya Fey, *Ace Attorney: Trials and Tribulations*
""",
"""
> *"I must say I'm used to being inspected by the ladies, but this is the first time I've felt this way with a man."*
- Klavier Gavin, *Apollo Justice: Ace Attorney*]
"""]    

suntzuquotes = [
            "It is the rule in war, if our forces are ten to the enemy's one, to surround him; if five to one, to attack him; if twice as numerous, to divide our army into two.",
            "There are five essentials for victory",
            "The art of war is of vital importance to the State.",
            "All warfare is based on deception.",
            "If your opponent is secure at all points, be prepared for him. If he is in superior strength, evade him.",
            "If the campaign is protracted, the resources of the State will not be equal to the strain.",
            "Attack him where he is unprepared, appear where you are not expected.",
            "There is no instance of a country having benefited from prolonged warfare.",
            "The skillful soldier does not raise a second levy, neither are his supply-wagons loaded more than twice.",
            "Bring war material with you from home, but forage on the enemy.",
            "In war, then, let your great object be victory, not lengthy campaigns.",
            "To fight and conquer in all your battles is not supreme excellence; supreme excellence consists in breaking the enemy's resistance without fighting.",
            "Heaven signifies night and day, cold and heat, times and seasons.",
            "The good fighters of old first put themselves beyond the possibility of defeat, and then waited for an opportunity of defeating the enemy.",
            "One may know how to conquer without being able to do it.",
            "There are three ways in which a ruler can bring misfortune upon his army.",
            "By commanding the army to advance or to retreat, being ignorant of the fact that it cannot obey. This is called hobbling the army.",
            "By attempting to govern an army in the same way as he administers a kingdom, being ignorant of the conditions which obtain in an army. This causes restlessness in the soldier's minds.",
            "By employing the officers of his army without discrimination, through ignorance of the military principle of adaptation to circumstances. This shakes the confidence of the soldiers.",
            "He will win who knows when to fight and when not to fight.",
            "He will win who knows how to handle both superior and inferior forces.",
            "He will win whose army is animated by the same spirit throughout all its ranks.",
            "He will win who, prepared himself, waits to take the enemy unprepared.",
            "He will win who has military capacity and is not interfered with by the sovereign.",
            "If you know the enemy and know yourself, you need not fear the result of a hundred battles.",
            "If you know yourself but not the enemy, for every victory gained you will also suffer a defeat.",
            "If you know neither the enemy nor yourself, you will succumb in every battle.",
            "The control of a large force is the same principle as the control of a few men: it is merely a question of dividing up their numbers.",
            "Security against defeat implies defensive tactics; ability to defeat the enemy means taking the offensive.",
            "Standing on the defensive indicates insufficient strength; attacking, a superabundance of strength.",
            "He wins his battles by making no mistakes. Making no mistakes is what establishes the certainty of victory, for it means conquering an enemy that is already defeated.",
            "A victorious army opposed to a routed one, is as a pound's weight placed in the scale against a single grain.",
            "The onrush of a conquering force is like the bursting of pent-up waters into a chasm a thousand fathoms deep.",
            "What the ancients called a clever fighter is one who not only wins, but excels in winning with ease.",
            "Hence his victories bring him neither reputation for wisdom nor credit for courage.",
            "Hence the skillful fighter puts himself into a position which makes defeat impossible, and does not miss the moment for defeating the enemy.",
            "In war the victorious strategist only seeks battle after the victory has been won, whereas he who is destined to defeat first fights and afterwards looks for victory.",
            "There are not more than five musical notes, yet the combinations of these five give rise to more melodies than can ever be heard.",
            "Appear at points which the enemy must hasten to defend; march swiftly to places where you are not expected.",
            "It is a matter of life and death, a road either to safety or to ruin.",
            "Hold out baits to entice the enemy. Feign disorder, and crush him.",
            "All men can see the tactics whereby I conquer, but what none can see is the strategy out of which victory is evolved.",
            "Do not repeat the tactics which have gained you one victory, but let your methods be regulated by the infinite variety of circumstances.",
            "So in war, the way is to avoid what is strong and to strike at what is weak.",
            "Just as water retains no constant shape, so in warfare there are no constant conditions."
        ]


ytvalues = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
mbtilist = ["INTJ", "ENTJ", "INTP", "ENTP", "INFJ", "INFP", "ENFJ", "ENFP", "ISTJ", "ESTJ", "ISFJ", "ESFJ", "ISTP", "ESTP", "ISFP", "ESFP"]
mbtifuncs = [
{
    "mbti":"ISTP",
    "dom":"Ti",
    "sec":"Se",
    "stack":"Ti-Se-Ni-Fe"
},
{
    "mbti":"INTP",
    "dom":"Ti",
    "sec":"Ne",
    "stack":"Ti-Ne-Si-Fe"
},
{
    "mbti":"ESTJ",
    "dom":"Te",
    "sec":"Si",
    "stack":"Te-Si-Ne-Fi"
},
{
    "mbti":"ENTJ",
    "dom":"Te",
    "sec":"Ni",
    "stack":"Te-Ni-Se-Fi"
},
{
    "mbti":"INFP",
    "dom":"Fi",
    "sec":"Ne",
    "stack":"Fi-Ne-Si-Te"
},
{
    "mbti":"ISFP",
    "dom":"Fi",
    "sec":"Se",
    "stack":"Fi-Se-Ni-Te"
},
{
    "mbti":"ESFJ",
    "dom":"Fe",
    "sec":"Si",
    "stack":"Fe-Si-Ne-Ti"
},
{
    "mbti":"ENFJ",
    "dom":"Fe",
    "sec":"Ni",
    "stack":"Fe-Ni-Se-Ti"
},
{
    "mbti":"ISTJ",
    "dom":"Si",
    "sec":"Te",
    "stack":"Si-Te-Fi-Ne"
},
{
    "mbti":"ISFJ",
    "dom":"Si",
    "sec":"Fe",
    "stack":"Si-Fe-Ti-Ne"
},
{
    "mbti":"ESTP",
    "dom":"Se",
    "sec":"Ti",
    "stack":"Se-Ti-Fe-Ni"
},
{
    "mbti":"ESFP",
    "dom":"Se",
    "sec":"Fi",
    "stack":"Se-Fi-Te-Ni"
},
{
    "mbti":"INTJ",
    "dom":"Ni",
    "sec":"Te",
    "stack":"Ni-Te-Fi-Se"
},
{
    "mbti":"INFJ",
    "dom":"Ni",
    "sec":"Fe",
    "stack":"Ni-Fe-Ti-Se"
},
{
    "mbti":"ENTP",
    "dom":"Ne",
    "sec":"Ti",
    "stack":"Ne-Ti-Fe-Si"
},
{
    "mbti":"ENFP",
    "dom":"Ne",
    "sec":"Fi",
    "stack":"Ne-Fi-Te-Si"
},
]

difficulty = ["easy", "medium", "hard"]
category = [
    "Any Category",
    "General Knowledge",
    "Entertainment: Books",
    "Entertainment: Film",
    "Entertainment: Music",
    "Entertainment: Musicals & Theatres",
    "Entertainment: Television",
    "Entertainment: Video Games",
    "Entertainment: Board Games",
    "Science & Nature",
    "Science: Computers",
    "Science: Mathematics",
    "Mythology",
    "Sports",
    "Geography",
    "History",
    "Politics",
    "Art",
    "Celebrities",
    "Animals",
    "Vehicles",
    "Entertainment: Comics",
    "Science: Gadgets",
    "Entertainment: Japanese Anime & Manga",
    "Entertainment: Cartoon & Animations"

]

mostmbtis = [{
    "introverted":{
        "judger":"INTJ",
        "perciever":"INTP",
        "introvert":"INTJ",
        "extravert":"ENFP",
        "intuitive":"INTJ",
        "sensor":"ISTP",
        "thinker":"INTJ",
        "feeler":"INFP"
    },
    "extraverted":{
        "judger":"ENFJ",
        "perciever":"ESTP",
        "introvert":"INFJ",
        "extravert":"ESTP",
        "intuitive":"ENFJ",
        "sensor":"ESTP",
        "thinker":"ESTP",
        "feeler":"ESFP"
    },
    "intuitive":{
        "judger":"INFJ",
        "perciever":"INTP",
        "introvert":"INFJ",
        "extravert":"ENTP",
        "intuitive":"INFJ",
        "sensor":"ISTP",
        "thinker":"INTP",
        "feeler":"INFJ"
    },
    "sensing":{
        "judger":"ISTJ",
        "perciever":"ESTP",
        "introvert":"ISTJ",
        "extravert":"ESTP",
        "intuitive":"ENTJ",
        "sensor":"ESTP",
        "thinker":"ESTP",
        "feeler":"ESFP"
    },
    "thinking":{
        "judger":"INTJ",
        "perciever":"INTP",
        "introvert":"INTP",
        "extravert":"ENTJ",
        "intuitive":"INTP",
        "sensor":"ISTJ",
        "thinker":"INTP",
        "feeler":"INFJ"
    },
    "feeling":{
        "judger":"ENFJ",
        "perciever":"ESFP",
        "introvert":"ISFJ",
        "extravert":"ESFP",
        "intuitive":"ENFJ",
        "sensor":"ESFP",
        "thinker":"ESTP",
        "feeler":"ESFP"
    },
    "percieving":{
        "judger":"ENFJ",
        "perciever":"ESFP",
        "introvert":"INTP",
        "extravert":"ESFP",
        "intuitive":"INTP",
        "sensor":"ESFP",
        "thinker":"ESTP",
        "feeler":"ESFP"
    },
    "judging":{
        "judger":"ENTJ",
        "perciever":"ISFP",
        "introvert":"INTJ",
        "extravert":"ENTJ",
        "intuitive":"ENTJ",
        "sensor":"ESTJ",
        "thinker":"ENTJ",
        "feeler":"ESFJ"
    }
}]

levels = [
    {'level': 1, 'messages_required': 70, 'commands_required': 10},
    {'level': 2, 'messages_required': 140, 'commands_required': 20},
    {'level': 3, 'messages_required': 210, 'commands_required': 30},
    {'level': 4, 'messages_required': 280, 'commands_required': 40},
    {'level': 5, 'messages_required': 350, 'commands_required': 50},
    {'level': 6, 'messages_required': 420, 'commands_required': 60},
    {'level': 7, 'messages_required': 490, 'commands_required': 70},
    {'level': 8, 'messages_required': 560, 'commands_required': 80},
    {'level': 9, 'messages_required': 630, 'commands_required': 90},
    {'level': 10, 'messages_required': 700, 'commands_required': 100},
    {'level': 11, 'messages_required': 770, 'commands_required': 110},
    {'level': 12, 'messages_required': 840, 'commands_required': 120},
    {'level': 13, 'messages_required': 910, 'commands_required': 130},
    {'level': 14, 'messages_required': 980, 'commands_required': 140},
    {'level': 15, 'messages_required': 1050, 'commands_required': 150},
    {'level': 16, 'messages_required': 1120, 'commands_required': 160},
    {'level': 17, 'messages_required': 1190, 'commands_required': 170},
    {'level': 18, 'messages_required': 1260, 'commands_required': 180},
    {'level': 19, 'messages_required': 1330, 'commands_required': 190},
    {'level': 20, 'messages_required': 1400, 'commands_required': 200},
    {'level': 21, 'messages_required': 1470, 'commands_required': 210},
    {'level': 22, 'messages_required': 1540, 'commands_required': 220},
    {'level': 23, 'messages_required': 1610, 'commands_required': 230},
    {'level': 24, 'messages_required': 1680, 'commands_required': 240},
    {'level': 25, 'messages_required': 1750, 'commands_required': 250},
    {'level': 26, 'messages_required': 1820, 'commands_required': 260},
    {'level': 27, 'messages_required': 1890, 'commands_required': 270},
    {'level': 28, 'messages_required': 1960, 'commands_required': 280},
    {'level': 29, 'messages_required': 2030, 'commands_required': 290},
    {'level': 30, 'messages_required': 2100, 'commands_required': 300},
    {'level': 31, 'messages_required': 2170, 'commands_required': 310},
    {'level': 32, 'messages_required': 2240, 'commands_required': 320},
    {'level': 33, 'messages_required': 2310, 'commands_required': 330},
    {'level': 34, 'messages_required': 2380, 'commands_required': 340},
    {'level': 35, 'messages_required': 2450, 'commands_required': 350},
    {'level': 36, 'messages_required': 2520, 'commands_required': 360},
    {'level': 37, 'messages_required': 2590, 'commands_required': 370},
    {'level': 38, 'messages_required': 2660, 'commands_required': 380},
    {'level': 39, 'messages_required': 2730, 'commands_required': 390},
    {'level': 40, 'messages_required': 2800, 'commands_required': 400},
    {'level': 41, 'messages_required': 2870, 'commands_required': 410},
    {'level': 42, 'messages_required': 2940, 'commands_required': 420},
    {'level': 43, 'messages_required': 3010, 'commands_required': 430},
    {'level': 44, 'messages_required': 3080, 'commands_required': 440},
    {'level': 45, 'messages_required': 3150, 'commands_required': 450},
    {'level': 46, 'messages_required': 3220, 'commands_required': 460},
    {'level': 47, 'messages_required': 3290, 'commands_required': 470},
    {'level': 48, 'messages_required': 3360, 'commands_required': 480},
    {'level': 49, 'messages_required': 3430, 'commands_required': 490},
    {'level': 50, 'messages_required': 3500, 'commands_required': 500},
    {'level': 51, 'messages_required': 3570, 'commands_required': 510},
    {'level': 52, 'messages_required': 3640, 'commands_required': 520},
    {'level': 53, 'messages_required': 3710, 'commands_required': 530},
    {'level': 54, 'messages_required': 3780, 'commands_required': 540},
    {'level': 55, 'messages_required': 3850, 'commands_required': 550},
    {'level': 56, 'messages_required': 3920, 'commands_required': 560},
    {'level': 57, 'messages_required': 3990, 'commands_required': 570},
    {'level': 58, 'messages_required': 4060, 'commands_required': 580},
    {'level': 59, 'messages_required': 4130, 'commands_required': 590},
    {'level': 60, 'messages_required': 4200, 'commands_required': 600},
    {'level': 61, 'messages_required': 4270, 'commands_required': 610},
    {'level': 62, 'messages_required': 4340, 'commands_required': 620},
    {'level': 63, 'messages_required': 4410, 'commands_required': 630},
    {'level': 64, 'messages_required': 4480, 'commands_required': 640},
    {'level': 65, 'messages_required': 4550, 'commands_required': 650},
    {'level': 66, 'messages_required': 4620, 'commands_required': 660},
    {'level': 67, 'messages_required': 4690, 'commands_required': 670},
    {'level': 68, 'messages_required': 4760, 'commands_required': 680},
    {'level': 69, 'messages_required': 4830, 'commands_required': 690},
    {'level': 70, 'messages_required': 4900, 'commands_required': 700},
    {'level': 71, 'messages_required': 4970, 'commands_required': 710},
    {'level': 72, 'messages_required': 5040, 'commands_required': 720},
    {'level': 73, 'messages_required': 5110, 'commands_required': 730},
    {'level': 74, 'messages_required': 5180, 'commands_required': 740},
    {'level': 75, 'messages_required': 5250, 'commands_required': 750},
    {'level': 76, 'messages_required': 5320, 'commands_required': 760},
    {'level': 77, 'messages_required': 5390, 'commands_required': 770},
    {'level': 78, 'messages_required': 5460, 'commands_required': 780},
    {'level': 79, 'messages_required': 5530, 'commands_required': 790},
    {'level': 80, 'messages_required': 5600, 'commands_required': 800},
    {'level': 81, 'messages_required': 5670, 'commands_required': 810},
    {'level': 82, 'messages_required': 5740, 'commands_required': 820},
    {'level': 83, 'messages_required': 5810, 'commands_required': 830},
    {'level': 84, 'messages_required': 5880, 'commands_required': 840},
    {'level': 85, 'messages_required': 5950, 'commands_required': 850},
    {'level': 86, 'messages_required': 6020, 'commands_required': 860},
    {'level': 87, 'messages_required': 6090, 'commands_required': 870},
    {'level': 88, 'messages_required': 6160, 'commands_required': 880},
    {'level': 89, 'messages_required': 6230, 'commands_required': 890},
    {'level': 90, 'messages_required': 6300, 'commands_required': 900},
    {'level': 91, 'messages_required': 6370, 'commands_required': 910},
    {'level': 92, 'messages_required': 6440, 'commands_required': 920},
    {'level': 93, 'messages_required': 6510, 'commands_required': 930},
    {'level': 94, 'messages_required': 6580, 'commands_required': 940},
    {'level': 95, 'messages_required': 6650, 'commands_required': 950},
    {'level': 96, 'messages_required': 6720, 'commands_required': 960},
    {'level': 97, 'messages_required': 6790, 'commands_required': 970},
    {'level': 98, 'messages_required': 6860, 'commands_required': 980},
    {'level': 99, 'messages_required': 6930, 'commands_required': 990},
    {'level': 100, 'messages_required': 7000, 'commands_required': 1000},
]

rpswins = [
    
        {
            "botchoice": "rock",
            "userchoice":"paper",
            "final":"You WIN!"
        },
        {
            "botchoice": "rock",
            "userchoice":"scissors",
            "final":"You LOST!"
        },
        {
            "botchoice": "paper",
            "userchoice":"rock",
            "final":"You LOST!"
        },
        {
            "botchoice": "paper",
            "userchoice":"scissors",
            "final":"You WIN!"
        },
        {
            "botchoice": "scissors",
            "userchoice":"rock",
            "final":"You WIN!"
        },
        {
            "botchoice": "scissors",
            "userchoice":"paper",
            "final":"You LOST!"
        }

    
]
