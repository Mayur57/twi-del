# Twitter Thread Deleter

## ⭐ Purpose
The script automatically deletes a thread from the bottom up and outputs all the deleted tweets to a text file. Logged information also includes the date and time of sending the tweet in addition to the tweet itself.

## ⭐ Usage

Open terminal (or cmd on Windows) and type the following command:
```python3 script.py -k```

Alternatively, you can edit the script to hard-code your keys and run:
```python3 script.py -d```

## ⭐ Flags
#### -k -> Set Keys Mode
This flag runs the script in the mode where the user is asked for their keys and tokens necessary for using the Twitter API.

#### -d -> Delete Tweets Mode
This flag runs the script in the mode where the user isn't required to input any authentication keys. This mode is for those users who have modified the script to include thier authentication in a hardcoded fashion.

#### help -> Help Mode
Shows a help message.

If you face any issues, just create an issue.