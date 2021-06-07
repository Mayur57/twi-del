import datetime
import codecs


s = [0, 1, 1, 0, 1, 2, 1, 1, 2, 4, 1, 2, 1, 3, 1, 2, 3, 3, 2, 4, 3, 4, 2, 3, 5, 5, 5, 3, 2, 2]
t = [u'"Director of Languages and Runtimes" is such a cool position to have \U0001f62d\U0001f62d', u'Reachability and Extensions on mobile versions. This is fucking amazing. I want extension for Chrome on Android @googlechrome \U0001f61e\U0001f61e\U0001f61e', u'Safari looks suuuuuuuper appealing to the designer in me ;_;', u'Shortcuts on macOS is going to be the feature for me. Automate the boring stuff.', u"macOS Monterey.\n\nAtleast it's better than Big Sur", u'MACOS TIME \u2728\u2728', u"can't wait for someone to rediscover these features next year and tweet a banger", u'Okay how do I skip to the macOS section?', u'They added Brave browser to Safari, ok', u'OMG building apps on a iPad?????? I WANT IT', u'apple my dear apple, why are you rewriting what you already have? MACOS DOES THIS ALREADY', u"They could've added this Widget with apps last year this is bullcrap.", u'Gagan looks so young man how old are they?', u'I LOVE THIS CARD DESIGN WEATHER HAS LVJXLVJSVHL', u'Do you think Apple encourages travel so that devs can have photos to show off? \U0001f602', u'Okay this is better than Google', u'Memories is a Google Photos with the same name!', u'Why is Chelsea Brunette a blonde \U0001f62d\U0001f62d\U0001f62d\U0001f62d\U0001f62d\U0001f62d', u'I like Spotlight on mac so this looks good', u'Abey Google Lens on iPhones \U0001f62d\U0001f602\U0001f62d\U0001f602\U0001f62d\U0001f602\U0001f62d', u'Apple graphic design team how to apply for????', u'uh ya zen mode is there already but i want others to know my phone is on silent shut up', u'I want Focus on Android.', u'uhhh this notification summary thing is nice actually', u'Mindy \U0001f633\U0001f633\U0001f633\U0001f633\U0001f633\U0001f633\U0001f633\U0001f633\U0001f633\U0001f633\n\ndown bad laude chup', u'It nice to see Apple develope features that enable people to connect in times like a pandemic\n\nDiscord tho', u'Bro this is just discord apple version', u'Portrait Mode, we have taken inspiration from Google!', u'But Craig, I have noone to FaceTime \U0001f972\U0001f972\U0001f972', u'Man I love Craig so much']
d = [datetime.datetime(2021, 6, 7, 18, 38, 37), datetime.datetime(2021, 6, 7, 18, 34, 57), datetime.datetime(2021, 6, 7, 18, 32, 27), datetime.datetime(2021, 6, 7, 18, 29, 57), datetime.datetime(2021, 6, 7, 18, 23, 7), datetime.datetime(2021, 6, 7, 18, 21, 40), datetime.datetime(2021, 6, 7, 18, 10, 28), datetime.datetime(2021, 6, 7, 17, 59, 3), datetime.datetime(2021, 6, 7, 17, 52, 13), datetime.datetime(2021, 6, 7, 17, 49, 11), datetime.datetime(2021, 6, 7, 17, 44, 12), datetime.datetime(2021, 6, 7, 17, 41), datetime.datetime(2021, 6, 7, 17, 36, 33), datetime.datetime(2021, 6, 7, 17, 30, 47), datetime.datetime(2021, 6, 7, 17, 28, 5), datetime.datetime(2021, 6, 7, 17, 26, 26), datetime.datetime(2021, 6, 7, 17, 25, 50), datetime.datetime(2021, 6, 7, 17, 25, 11), datetime.datetime(2021, 6, 7, 17, 24, 51), datetime.datetime(2021, 6, 7, 17, 22, 7), datetime.datetime(2021, 6, 7, 17, 21, 26), datetime.datetime(2021, 6, 7, 17, 20, 23), datetime.datetime(2021, 6, 7, 17, 19, 48), datetime.datetime(2021, 6, 7, 17, 19, 1), datetime.datetime(2021, 6, 7, 17, 15, 55), datetime.datetime(2021, 6, 7, 17, 14, 17), datetime.datetime(2021, 6, 7, 17, 11, 44), datetime.datetime(2021, 6, 7, 17, 10, 17), datetime.datetime(2021, 6, 7, 17, 8, 29), datetime.datetime(2021, 6, 7, 17, 7, 4)]


def output_to_file(s, t, d):
    s.reverse()
    t.reverse()
    d.reverse()

    f = codecs.open("OUTPUT", "a", "utf-8")
    
    f.write("""
<------------------------- Automatically Generated ------------------------->


⭐⭐⭐ Tweet Outputs:
""")
    for i in range(0, len(t)):
        f.write("\n\nTweet #" + str(i+1) + "\nTweet: " +
                t[i].replace("\n", "") + "\nTimestamp: " + str(d[i]) + "\nLikes: " + str(s[i]))
    print("\n\nOUTPUT file was generated with all the deleted tweets.")


output_to_file(s, t, d)
