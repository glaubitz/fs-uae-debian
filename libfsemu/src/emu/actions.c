/* libfsemu - a library with emulator support functions
 * Copyright (C) 2011 Frode Solheim <frode-code@fengestad.no>
 *
 * This library is free software; you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation; either version 2.1 of the License, or (at
 * your option) any later version.
 *
 * This library is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
 * or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public
 * License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this library; if not, write to the Free Software Foundation,
 * Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <fs/emu.h>
#include <fs/emu/actions.h>
#include <fs/lazyness.h>
#include <fs/glib.h>
#include "video.h"
#include <stdlib.h>

static const char* g_taunts[] = {
        "You play like a dairy farmer!",
        "No one will ever catch ME playing as badly as you do!",
        "I once owned a dog that played better then you!",
        "Never before have I faced someone so sissified.",
        "You're no match for my skills, you poor fool.",
        "Go home and be a family man!",
        "It's good to be the king.",
        "Your mother was a hamster and your father smelt of elderberries",
        NULL,
};
static int g_num_taunts = 8;

static void taunt()
{
    char *text = g_strdup_printf("%c%s\n", 1,
            g_taunts[g_random_int_range(0, g_num_taunts)]);
    fs_emu_netplay_say(text);
    g_free(text);
}

void fs_emu_handle_libfsemu_action(int action, int state)
{
    if (g_fs_log_input) {
        fs_log("fs_emu_handle_libfsemu_action %d %d\n", action, state);
    }
    if (state) {
        if (action == FS_EMU_ACTION_MENU_ALT) {
            fs_emu_menu_toggle();
        } else if (action == FS_EMU_ACTION_TAUNT) {
            taunt();
        } else if (action == FS_EMU_ACTION_SCREENSHOT) {
            g_fs_emu_screenshot = 1;
        } else if (action == FS_EMU_ACTION_PAUSE) {
            fs_emu_pause(!fs_emu_is_paused());
        }
    }
}