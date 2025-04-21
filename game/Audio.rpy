################################################################################
## Music 
################################################################################
init python:
    renpy.music.register_channel("music1", "music", loop=True, stop_on_mute=False, tight=True, file_prefix='', file_suffix='', buffer_queue=True)
    renpy.music.register_channel("music2", "music", loop=True, stop_on_mute=False, tight=True, file_prefix='', file_suffix='', buffer_queue=True)
    renpy.music.register_channel("music3", "music", loop=True, stop_on_mute=False, tight=True, file_prefix='', file_suffix='', buffer_queue=True)
    renpy.music.register_channel("music4", "music", loop=True, stop_on_mute=False, tight=True, file_prefix='', file_suffix='', buffer_queue=True)
    renpy.music.register_channel("music5", "music", loop=True, stop_on_mute=False, tight=True, file_prefix='', file_suffix='', buffer_queue=True)
    renpy.music.register_channel("music6", "music", loop=True, stop_on_mute=False, tight=True, file_prefix='', file_suffix='', buffer_queue=True)
    renpy.music.register_channel("music7", "music", loop=True, stop_on_mute=False, tight=True, file_prefix='', file_suffix='', buffer_queue=True)

# $ renpy.music.play("audio/music/01 Captains Tent Strings.ogg", channel='music1', loop=True, synchro_start=True, fadein=2, tight=True)
# $ renpy.music.play("audio/music/01 Captains Tent Brass.ogg", channel='music2', loop=True, synchro_start=True, fadein=1, tight=True)
# $ renpy.music.set_volume(0, delay=0, channel='music1')
# $ renpy.music.set_volume(0, delay=0, channel='music2')

## end music ###################################################################

################################################################################
## Ambiance 
################################################################################
#define audio.main = "audio/test2.ogg"

## end ambiance ################################################################

################################################################################
## SFX 
################################################################################
init python:
    renpy.music.register_channel("amb1", "sound", loop=True, stop_on_mute=False, tight=True, file_prefix='', file_suffix='', buffer_queue=True)
    renpy.music.register_channel("amb2", "sound", loop=True, stop_on_mute=False, tight=True, file_prefix='', file_suffix='', buffer_queue=True)
    renpy.music.register_channel("amb3", "sound", loop=True, stop_on_mute=False, tight=True, file_prefix='', file_suffix='', buffer_queue=True)
    renpy.music.register_channel("sfx1", "sound", loop=False, stop_on_mute=False, tight=True, file_prefix='', file_suffix='', buffer_queue=True)
    renpy.music.register_channel("sfx2", "sound", loop=False, stop_on_mute=False, tight=True, file_prefix='', file_suffix='', buffer_queue=True)
    renpy.music.register_channel("sfx3", "sound", loop=False, stop_on_mute=False, tight=True, file_prefix='', file_suffix='', buffer_queue=True)


define tent_open = "audio/sound/Tent Flap Open.ogg"
define tent_close = "audio/sound/Tent Flap Close.ogg"
define tent_place = "audio/sound/Tent Place.ogg"

define tree_move = "audio/sound/Tree Move.ogg"

define knife_vine_1 = "audio/sound/Knife Cut Vine.ogg"
define knife_vine_2 = "audio/sound/Knife Cut Vine 2.ogg"
define knife_vine_3 = "audio/sound/Knife Cut Vine 3.ogg"

define fireball = "audio/sound/Fireball.ogg"
define fireball_vine = "audio/sound/Fireball Destroy Vine.ogg"

define cave_amb = "audio/sound/Cave Amb.ogg"
define captains_amb = "audio/sound/Captains Chambers Amb.ogg"
define soldier_tent_amb = "audio/sound/Player Chamber Amb.ogg"

## end sfx #####################################################################

################################################################################
##  Character Voices
################################################################################
init python:
    renpy.music.register_channel("voices", "voices", loop=None)

##############################################################################
# This function is optional. Only include it if you want automatic pauses between punctuation
    def typography(what):
        replacements = [
                ('. ','. {w=.2}'), # Moderate pause after periods
                ('? ','? {w=.25}'), # Long pause after question marks
                ('! ','! {w=.25}'), # Long pause after exclamation marks
                (', ',', {w=.15}'), # Short pause after commas
        ]
        for item in replacements:
            what = what.replace(item[0],item[1])
        return what
    config.say_menu_text_filter = typography # This ensures the text block has the same ID value, even after all the replacements are made
##############################################################################

    def estimate_syllables(text):
        vowels = "aeiouyAEIOUY"
        syllables = 0
        prev_char_was_vowel = False

        for char in text:
            if char in vowels:
                if not prev_char_was_vowel:
                    syllables += 1
                    prev_char_was_vowel = True
            else:
                prev_char_was_vowel = False

        return max(syllables, 1)
##############################################################################

    def text_sounds(event, interact=False, **kwargs):
        if event == "show": # If textbox is shown
            what = renpy.store._last_say_what # This grabs the text that was most recently spoken on-screen
            if what:
                sound_count = estimate_syllables(what)
            else:
                sound_count = 1

            for _ in range(sound_count):# This creates a sound queue based on how many characters are in the dialog block
                randosound = renpy.random.randint(1, 3)# This generates a random number between 1 and 3 inclusive. Change this based on how many sound files you have
                renpy.sound.queue(f"audio/popcat{randosound}.wav", channel="voices", loop=False) # Change "popcat" to the name of your sound file
        elif event == "end" or event == "slow_done": # This stops the text sounds if there is a pause in the dialog or the text has finished displaying
            renpy.sound.stop(channel="sound")
##############################################################################

## end voices ##################################################################


