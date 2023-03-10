from ShikiXMusic.config import ASSISTANT_NAME, PROJECT_NAME


class Messages:
    START_MSG = "**Hello đ [{}](tg://user?id={})!**\n\nđ¤ I am an advanced bot created for playing music in the voice chats of Telegram Groups & Channels.\n\nâ Send me /help for more info."
    HELP_MSG = [
        ".",
        f"""
**Hey đ Welcome back to {PROJECT_NAME}

âŞď¸ {PROJECT_NAME} can play music in your group's voice chat as well as channel voice chats

âŞď¸ Assistant name >> @{ASSISTANT_NAME}\n\nClick next for instructions**
""",
        f"""
**Setting up**

1) Make bot admin (Group and in channel if use cplay)
2) Start a voice chat
3) Try /play [song name] for the first time by an admin
*) If userbot joined enjoy music, If not add @{ASSISTANT_NAME} to your group and retry

**For Channel Music Play**
1) Make me admin of your channel 
2) Send /userbotjoinchannel in linked group
3) Now send commands in linked group
""",
        f"""
**Commands**

**=>> Song Playing đ§**

- /play: Play the requestd song
- /play [yt url] : Play the given yt url
- /play [reply yo audio]: Play replied audio
- /ytplay: Directly play song via Youtube Music

**=>> Playback âŻ**

- /player: Open Settings menu of player
- /skip: Skips the current track
- /pause: Pause track
- /resume: Resumes the paused track
- /end: Stops media playback
- /mute: mute song play
- /unmute: unmute song play
- /current: Shows the current Playing track
- /playlist: Shows playlist

*Player cmd and all other cmds except /play, /current  and /playlist  are only for admins of the group.
""",
        f"""
**=>> Channel Music Play đ **

âŞď¸ For linked group admins only:

- /cplay [song name] - play song you requested
- /cplaylist - Show now playing list
- /cccurrent - Show now playing
- /cplayer - open music player settings panel
- /cpause - pause song play
- /cresume - resume song play
- /cskip - play next song
- /cend - stop music play
- /cmute - mute song play
- /mute - mute song play
- /unmute - mute song play
- /userbotjoinchannel - invite assistant to your chat

channel is also can be used instead of c ( /cplay = /channelplay )

âŞď¸ If you donlt like to play in linked group:

1) Get your channel ID.
2) Create a group with tittle: Channel Music: your_channel_id
3) Add bot as Channel admin with full perms
4) Add @{ASSISTANT_NAME} to the channel as an admin.
5) Simply send commands in your group. (remember to use /ytplay instead /play)
""",
        f"""
**=>> More tools đ§âđ§**

- /musicplayer [on/off]: Enable/Disable Music player
- /admincache: Updates admin info of your group. Try if bot isn't recognize admin
- /userbotjoin: Invite @{ASSISTANT_NAME} Userbot to your chat
""",
        f"""
**=>> Song Download đ¸**

- /video [song mame]: Download video song from youtube
- /song [song name]: Download audio song from youtube
- /saavn [song name]: Download song from saavn
- /deezer [song name]: Download song from deezer

**=>> Search Tools đ**

- /search [song name]: Search youtube for songs
- /lyrics [song name]: Get song lyrics
""",
        f"""
**=>> Commands for Sudo Users âď¸**

 - /userbotleaveall - remove assistant from all chats
 - /broadcast <reply to message> - globally brodcast replied message to all chats
 - /pmpermit [on/off] - enable/disable pmpermit message
*Sudo Users can execute any command in any groups

""",
    ]
