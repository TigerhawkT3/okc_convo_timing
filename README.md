# okc_convo_timing
Groups the timestamps of each user's messages in an OkCupid conversation into hourly buckets.

_**NOTE:**_ This script will only run with Python 3.6 or newer. If necessary, you might be able to tweak it to handle an earlier version of Python 3 (3.3 or so, perhaps) by turning the format strings (e.g. `f'{a}+{b}={a+b}'`) into `str.format` calls (e.g. `'{}+{}={}'.format(a, b, a+b)`).

This script allows you to track activity and participation in an OkCupid conversation. It produces tab-delimited output with the date (to the hour), the number of your messages in that hour, and the number of messages from the other user in that hour. A header row is included. Typical output looks like this:

    Date	Alice518	Bob919
    2017/05/02 00:00	0	0
    2017/05/02 01:00	0	0
    2017/05/02 02:00	0	0
    2017/05/02 03:00	0	0
    2017/05/02 04:00	0	0
    2017/05/02 05:00	0	0
    2017/05/02 06:00	1	0
    2017/05/02 07:00	10	11
    2017/05/02 08:00	0	0
    2017/05/02 09:00	0	2
    2017/05/02 10:00	0	0
    2017/05/02 11:00	0	0
    2017/05/02 12:00	6	5
    2017/05/02 13:00	0	0
    2017/05/02 14:00	0	0
    2017/05/02 15:00	0	0
    2017/05/02 16:00	0	0
    2017/05/02 17:00	6	8
    2017/05/02 18:00	22	20
    2017/05/02 19:00	0	0
    2017/05/02 20:00	0	0
    2017/05/02 21:00	0	0

In the above example, Alice518 (who is running this script) sent a message a bit before 7am (on 5/2, the second of May), then talked with Bob919 over breakfast. Bob919 thought of something funny to say shortly after he got to work, sending a couple messages at that time. They exchanged a few messages during lunch, then talked more extensively when they returned home from work.

* To get the proper input for this script, you will need the full conversation, with timestamps and user names. You can get this from the conversation view on the OKC mobile site.
* Remember to load older messages.

1. Dump this content in your preferred manner, such as printing the page to PDF in Chrome for Android.
0. Then transfer it to your computer.
0. If you have something other than a plain text file, open the file, select all, copy, paste it into a regular text editor (like Notepad), and save the new file.
0. Finally, run the script, passing it the new filename, your username, and the other person's username.
0. You may pass the correct date as an optional argument (`y/m/d`). This is necessary if:
   * the file's last modification date is different from the date of the last message, and
   * the last message just says the weekday or "Yesterday" or "Today" instead of the actual date
0. If you'd like to hide rows that contain no messages, you may pass the word `suppress` as an optional argument. If you want to include both of these optional arguments, `suppress` must follow the date.
0. Since you'll be pasting this into another program anyway, it's most useful if you pipe the output to the clipboard rather than letting it go to the console or directing it to a file. Some examples:

       py conversation_analytics.py saved_conversation.txt Alice518 Bob919 | clip
       py conversation_analytics.py saved_conversation.txt Alice518 Bob919 2017/5/2 | clip
       py conversation_analytics.py saved_conversation.txt Alice518 Bob919 suppress | clip
       py conversation_analytics.py saved_conversation.txt Alice518 Bob919 2017/5/2 suppress | clip

0. Paste into a spreadsheet program. To handle the chart's border padding, paste the data starting a few rows down instead of in the first row.
0. Create a _bar_ chart (not a column chart) from your pasted data. The hours will be arranged vertically, matching your pasted data.
0. Invert the Y axis so that earlier dates are at the top, matching your pasted data.
0. Resize the graph object so that each bar lines up nicely with the corresponding hour in your pasted data.

Graphing trivial data: more fun than board game night! \o/
