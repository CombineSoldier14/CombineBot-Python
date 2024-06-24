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
