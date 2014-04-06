from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

class Options:

    @staticmethod
    def get(name):
        return options[name]

N_ = lambda x: x

options = {

"audio_buffer_target_bytes": {
    "default": "8192",
    "description": N_("Audio buffer target size (bytes)"),
    "type": "integer",
    "min": 1024,
    "max": 32768,
},

"audio_buffer_target_size": {
    "default": "40",
    "description": N_("Audio buffer target size (ms)"),
    "type": "integer",
    "min": 1,
    "max": 100,
},

"audio_frequency": {
    "default": "48000",
    "description": N_("Audio output freqency"),
    "type": "choice",
    "values": [
        ("48000", "48000 Hz"),
        ("44100", "44100 Hz"),
        ("22050", "22050 Hz"),
        ("11025", "11025 Hz"),
    ]
},

"automatic_input_grab": {
    "default": "1",
    "description": N_("Grab mouse and keyboard input when clicking on FS-UAE window"),
    "type": "boolean",
},

"builtin_configs": {
    "default": "1",
    "description": N_("Include built-in configurations"),
    "type": "boolean",
},

"database_auth": {
    "default": "",
    "description": N_("Game database authentication"),
    "type": "string",
},

"database_email": {
    "default": "",
    "description": N_("Game database email"),
    "type": "string",
},

"database_feature": {
    "default": "0",
    "description": N_("Enable online database support (requires restart)"),
    "type": "boolean",
},

"database_password": {
    "default": "",
    "description": N_("Game database password"),
    "type": "string",
},

"database_server": {
    "default": "oagd.net",
    "description": N_("Custom game database server address"),
    "type": "string",
},

"database_show_games": {
    "default": "1",
    "description": N_("Show games from database"),
    "type": "choice",
    "values": [
        ("1", N_("Games you have and all downloadable games")),
        ("2", N_("Games you have and automatically downloadable")),
        ("3", N_("Only games you have")),
    ]
},

"database_username": {
    "default": "",
    "description": N_("Game database user name"),
    "type": "string",
},

"device_id": {
    "default": "",
    "description": N_("Device ID used with OAGD.net authentication"),
    "type": "string",
},

"floppy_drive_volume": {
    "default": "20",
    "description": N_("Floppy drive volume"),
    "type": "integer",
    "min": 0,
    "max": 100,
},

"fsaa": {
    "default": "0",
    "description": N_("Full-scene anti-aliasing (FSAA)"),
    "type": "choice",
    "values": [
        ("0", N_("Off")),
        ("2", "2x2"),
        ("4", "4x4"),
        ("8", "8x8"),
    ]
},

"fullscreen": {
    "default": "0",
    "description": N_("Start FS-UAE in fullscreen mode"),
    "type": "boolean",
},

"initial_input_grab": {
    "default": "",
    "description": N_("Grab mouse and keyboard input when FS-UAE starts"),
    "type": "boolean",
},

"irc_nick": {
    "default": "",
    "description": N_("IRC nickname"),
    "type": "string",
},

"irc_server": {
    "default": "irc.fengestad.no",
    "description": N_("Custom IRC server address"),
    "type": "string",
},

"keep_aspect": {
    "default": "0",
    "description": N_("Keep aspect ratio when scaling (do not stretch)"),
    "type": "boolean",
},

"kickstart_setup": {
    "default": "1",
    "description": N_("Show kickstart setup page on startup when all ROMs are missing"),
    "type": "boolean",
},

"load_state": {
    "default": "",
    "description": N_("Load state by number"),
    "type": "integer",
    "min": 1,
    "max": 9,
},

"low_latency_vsync": {
    "default": "0",
    "description": N_("Low latency video sync"),
    "type": "boolean",
},

"middle_click_ungrab": {
    "default": "1",
    "description": N_("Ungrab mouse and keyboard on middle mouse click"),
    "type": "boolean",
},

"min_first_line_ntsc": {
    "default": "21",
    "description": N_("First rendered line (NTSC)"),
    "type": "",
},

"min_first_line_pal": {
    "default": "26",
    "description": N_("First rendered line (PAL)"),
    "type": "",
},

"mouse_speed": {
    "default": "100",
    "description": N_("Mouse speed (%)"),
    "type": "integer",
    "min": 1,
    "max": 500,
},

"netplay_feature": {
    "default": "0",
    "description": N_("Enable experimental net play GUI (requires restart)"),
    "type": "boolean",
},

"netplay_tag": {
    "default": "UNK",
    "description": N_("Net play tag (max 3 characters)"),
    "type": "string",
},

"rtg_scanlines": {
    "default": "0",
    "description": N_("Render scan lines in RTG graphics mode"),
    "type": "boolean",
},

"scanlines": {
    "default": "0",
    "description": N_("Render scan lines"),
    "type": "boolean",
},

"stereo_separation": {
    "default": "100",
    "description": N_("Stereo separation"),
    "type": "choice",
    "values": [
        ("100", "100%"),
        ("90", "90%"),
        ("80", "80%"),
        ("70", "70%"),
        ("60", "60%"),
        ("50", "50%"),
        ("40", "40%"),
        ("30", "30%"),
        ("20", "20%"),
        ("10", "10%"),
        ("0", "0%"),
    ]
},

"swap_ctrl_keys": {
    "default": "0",
    "description": N_("Swap left and right CTRL keys"),
    "type": "boolean",
},

"texture_filter": {
    "default": "linear",
    "description": N_("Texture filter"),
    "type": "choice",
    "values": [
        ("nearest", "GL_NEAREST"),
        ("linear", "GL_LINEAR"),
    ]
},

"texture_format": {
    "default": "",
    "description": N_("Video texture format (on the GPU)"),
    "type": "choice",
    "values": [
        ("rgb", "GL_RGB"),
        ("rgb8", "GL_RGB8"),
        ("rgba", "GL_RGBA"),
        ("rgba8", "GL_RGBA8"),
        ("rgb5", "GL_RGB5"),
        ("rgb5_1", "GL_RGB5_1"),
    ]
},

"uae_sound_output": {
    "default": "",
    "description": N_("Sound emulation"),
    "type": "",
    "values": [
        ("none", "Disabled"),
        ("interrupts", "Emulated, No Output"),
        ("exact", "Enabled"),
    ]
},

"video_format": {
    "default": "bgra",
    "description": N_("Video buffer format and color depth"),
    "type": "choice",
    "values": [
        ("bgra", N_("32-bit BGRA")),
        ("rgba", N_("32-bit RGBA")),
        ("rgb565", N_("16-bit")),
    ]
},

"video_sync": {
    "default": "auto",
    "description": N_("Video synchronization"),
    "type": "choice",
    "values": [
        ("auto", N_("Auto")),
        ("vblank", N_("Buffer swap only")),
        ("off", N_("Off")),
    ]
},

"video_sync_method": {
    "default": "",
    "description": N_("Video synchronization method"),
    "type": "choice",
    "values": [
        ("swap", "Swap"),
        ("swap-finish", "Swap-Finish"),
        ("finish-swap-finish", "Finish-Swap-Finish"),
        ("finish-sleep-swap-finish", "Finish-Sleep-Swap-Finish"),
        ("sleep-swap-finish", "Sleep-Swap-Finish"),
        ("swap-fence", "Swap-Fence"),
        ("swap-sleep-fence", "Swap-Sleep-Fence"),
    ]
},

"volume": {
    "default": "100",
    "description": N_("Main volume control"),
    "type": "integer",
    "min": 0,
    "max": 100,
},

"zoom": {
    "default": "auto",
    "description": N_("Zoom Amiga display (crop)"),
    "type": "choice",
    "values": [
        ("auto", N_("Auto")),
        ("full", N_("Full Frame")),
        ("640x400", "640x400"),
        ("640x480", "640x480"),
        ("640x512", "640x512"),
        ("auto+border", N_("Auto + Border")),
        ("640x400+border", N_("640x400 + Border")),
        ("640x480+border", N_("640x480 + Border")),
        ("640x512+border", N_("640x512 + Border")),
    ]
},

}
