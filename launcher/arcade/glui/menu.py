from arcade.glui.animation import AnimateValueBezier
from arcade.glui.navigatable import Navigatable
from arcade.glui.state import State
from arcade.glui.topmenu import TopMenu
from fsbc.application import app


class Menu(Navigatable):
    def __init__(self, title=""):
        self.navigatable = None
        self.top = TopMenu()
        # self.top_mode = False
        self.title = title
        self.parent_menu = None
        self.parents = []
        self.items = []
        self._selected_index = 0
        self.position = 0.0
        self._position_animation = None
        self.last_scroll_pos = 0
        self.last_scroll_time = 0
        self.cur_scroll_speed = 0
        self.configuration_index = 0
        self.top_menu_transition = 1.0
        self.search_text = ""

    def use_game_center_item(self):
        return app.settings["game-center:top-logo"] != "0"

    def update_path(self, menu_path):
        # FIXME: UPDATE PATH
        # return
        print("update_path", menu_path)
        if self.use_game_center_item():
            from arcade.glui.topmenu import GameCenterItem
            self.top.append_left(GameCenterItem())
        # if len(menu_path) > 0:
        from arcade.glui.topmenu import HomeItem
        self.top.append_left(HomeItem())
        last_index = len(menu_path) - 1
        for i, item in enumerate(menu_path):
            if item.path_title or last_index == i:
                print("adding item", item)
                self.top.append_left(item)
                # if last_index == i:
                #     item.enabled = False
                # else:
                #     item.enabled = True

                # FIXME: FOR NOW, ALWAYS DISABLE PATH ELEMENTS
                item.enabled = False
        self.set_default_top_selected()

    def set_default_top_selected(self):
        # for i in range(len(self.top.left) - 1, -1, -1):
        #     if self.top.left[i].enabled:
        #         self.top.set_selected_index(i)
        #         break
        i = len(self.top.left) + len(self.top.right) - 1
        self.top.set_selected_index(i)

    def add_add_item(self):
        from arcade.glui.topmenu import AddItem
        self.top.append_left(AddItem())
        self.set_default_top_selected()
        # print("FIXME: add_add_item temporarily disabled")

    def append(self, item):
        self.items.append(item)

    def remove(self, item):
        self.items.remove(item)

    def reset_position(self):
        self.position = self._selected_index
        self.configuration_index = 0

    @property
    def selected_item(self):
        # if self.top_mode:
        #     return self.top.selected_item
        return self.items[self._selected_index % len(self.items)]

    def get_selected_index(self):
        return self._selected_index

    def get_current_position(self):
        t = State.get().time
        if self.last_scroll_time == t:
            pass
        elif self.last_scroll_time - t < 1.0:
            self.cur_scroll_speed = (self.position - self.last_scroll_pos) / \
                                    (t - self.last_scroll_time)
        else:
            self.cur_scroll_speed = 0
        self.last_scroll_pos = self.position
        self.last_scroll_time = t
        # print "speed", self.cur_scroll_speed

        return self.position

    def set_selected_index(self, index, immediate=False):
        self._selected_index = index
        if immediate:
            self.reset_position()
        else:
            p1 = self.position + self.cur_scroll_speed * 0.040
            self._position_animation = AnimateValueBezier(
                (self, "position"),
                self.position, State.get().time,
                p1, State.get().time + 0.040,
                index, State.get().time + 0.080,
                index, State.get().time + 0.200)
        self.configuration_index = 0

    def go_left(self, count=1):
        # FIXME:
        from arcade.glui.window import set_items_brightness
        set_items_brightness(1.0, duration=0.300)
        self.set_selected_index(self._selected_index - count)

    def go_right(self, count=1):
        from arcade.glui.window import set_items_brightness
        set_items_brightness(1.0, duration=0.300)
        self.set_selected_index(self._selected_index + count)

    def activate(self):
        result = self.selected_item.activate(self)
        if result is None:
            return
        # FIXME
        from arcade.glui.window import enter_menu
        enter_menu(result)

    def render(self):
        pass

    def update(self):
        pass

    def render_transparent(self, data):
        pass

    def __getitem__(self, index):
        return self.items[index]

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return "<{2} {0} ({1} items)>".format(self.title, len(self),
                                              self.__class__.__name__)
