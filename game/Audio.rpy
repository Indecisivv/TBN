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


