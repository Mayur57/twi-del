import sys
import tweepy
import codecs

argumentList = sys.argv[1:]

consumer_key = 'Rxo5nyfVZriRliNe0hLoo1KFU'
consumer_secret = '5xyiTPIQ6CwvGcG44Gk93UedmbbeBKLIFyQrRPJw1SbfINWXcJ'
access_token = '749528490274353152-0yzSBWFxgBBVR7n7Wh4cC2xiu6a8xEx'
access_token_secret = 'uFlp4rUNDPUX9U9NOtEokXzpZnAyqIwYRRGgBzS5MSUjL'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweet = []
likes = []
timestamps = []


def showHelp():
    print('''
-------------------------------------------------------------------
 >> HELP - Twitter Thread Deleter
-------------------------------------------------------------------

    ⭐ Purpose

    The script automatically deletes a thread from the bottom
    up and outputs all the deleted tweets to a text file.
    Logged information also includes the date and time of
    sending the tweet in addition to the tweet itself.

    ⭐ Usage

    Open terminal (or cmd on Windows) and type the following
    command without quotes:
    "python3 script.py -d"


    ⭐ Flags

    -k -> Set Keys Mode
        This flag runs the script in the mode where the user
        is asked for their keys and tokens necessary for using
        the Twitter API.

    -d -> Delete Tweets Mode
        This flag runs the script in the mode where the user
        isn't required to input any authentication keys. This
        mode is for those users who have modified the script to
        include thier authentication in a hardcoded fashion.

    help -> Help Mode
        Shows this message.

    If you face any issues, post an issue on the GitHub repository:
    https://github.com/Mayur57/twi-del

-------------------------------------------------------------------
    ''')


def delete_iteratively(reply_id_arg):
    reply_id = reply_id_arg
    try:
        while (str(api.get_status(reply_id, tweet_mode="extended").in_reply_to_status_id) != 'None'):
            tb_deleted_id = reply_id

            twt_t = api.get_status(tb_deleted_id, tweet_mode="extended")

            reply_id = api.get_status(reply_id).in_reply_to_status_id

            tweet.append(twt_t.full_text)
            likes.append(twt_t.favorite_count)
            timestamps.append(twt_t.created_at)

            api.destroy_status(tb_deleted_id)

            print("Deleted: " + str(tb_deleted_id))

    except Exception as e:
        print("An exception occurred: " + str(e))

    finally:
        tweet.append(api.get_status(reply_id, tweet_mode="extended").full_text)
        likes.append(api.get_status(
            reply_id, tweet_mode="extended").favorite_count)
        timestamps.append(api.get_status(
            reply_id, tweet_mode="extended").created_at)
        api.destroy_status(reply_id)
        print("Deleted: " + str(reply_id))
        output_to_file(likes, tweet, timestamps)


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


def setKeys():
    print("\nEnter your Consumer Key:")
    ck = input()

    print("\nEnter your Consumer Secret Key:")
    cs = input()

    print("\nEnter your Access Token:")
    at = input()

    print("\nEnter your Access Token Secret:")
    ats = input()

    print("\n\nYour keys have been set.")
    deleter(ck, cs, at, ats)


def deleter(ck, cs, at, ats):
    if(ck == '' or cs == '' or at == '' or ats == ''):
        print("Keys have not been set. Run the script with -k flag to set keys.")
        sys.exit(0)

    else:
        print("\nDo you want to delete your Twitter thread? (Y|n)")
        inp = input()
        if(inp == "Y"):
            print("\nPaste the Tweet ID of the last tweet in your thread: ")
            id = input()
            print("\nDeleting...")
            delete_iteratively(id)
            print("Thread deletion completed successfully.")

        elif(inp == "n"):
            print(
                "\n\nCool, terminating the script. None of your tweets will be deleted.")
            sys.exit(0)

        else:
            print("Invalid arguments. Try running script again")
            showHelp()
            sys.exit(0)


if('-k' in argumentList):
    print("\nDo you want to set your access keys? (Y|n)")
    inp = input()
    if(inp == "Y"):
        setKeys()
    elif(inp == "n"):
        print("\n\nCool, terminating the script. None of your tweets will be deleted.")
        sys.exit(0)


elif ('-d' in argumentList):
    deleter(consumer_key, consumer_secret, access_token, access_token_secret)

elif ('help' in argumentList):
    showHelp()

else:
    print("\nInvalid arguments. Try running script again.")
