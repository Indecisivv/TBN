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


define music.TentBrass = "audio/music/01 Captains Tent Brass.ogg"
define music.TentStrings = "audio/music/01 Captains Tent Strings.ogg"

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


## end sfx #####################################################################


