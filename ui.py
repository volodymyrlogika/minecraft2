from ursina import *

Text.default_font = "assets\\F77MinecraftRegular-0VYv.ttf"


class MenuButton(Button):
    def __init__(self, text, action, x, y, parent):
        super().__init__(text=text, on_click=action, x=x, y=y, parent=parent,
                         scale=(0.6, 0.1),
                         origin=(0, 0),
                         ignore_paused=True,
                         texture='assets\\block_textures\\stone.png',
                         color=color.color(0, 0, random.uniform(0.9, 1)),
                         highlight_color=color.gray,
                         highlight_scale=1.05,
                         pressed_scale=1.05,
                         )


# Клас для керування меню
class MenuControl(Entity):
    def __init__(self, menu, **kwargs):
        super().__init__(ignore_paused=True, **kwargs)
        self.menu = menu

    def input(self, key):
        if key == 'escape':
            self.menu.toggle_menu()


class Menu(Entity):
    def __init__(self, game, **kwargs):
        game.menu = self
        super().__init__(parent=camera.ui, ignore_paused=True, **kwargs)
        self.bg = Sprite(texture='assets\\menu_bg.png',
                         parent=self, z=1, color=color.white, scale=0.1)
        self.title = Text(text="UrsinaCraft", scale=5,
                          parent=self, origin=(0, 0), x=0, y=0.35)
        self.bg_music = Audio(
            'assets\\StockTune-Enchanting Mystic Forest Melody_1728725154.mp3', volume=0.3, loop=True, autoplay=True)

        MenuButton("Нова гра", game.generate_world, 0, 0.13, self)
        MenuButton("Завантажити гру", game.load_game, 0, 0, self)
        MenuButton("Зберегти", game.save_game, 0, -0.13, self)
        MenuButton("Вийти", application.quit, 0, -0.26, self)

        MenuControl(self)


    def toggle_menu(self):
        application.paused = not application.paused
        self.enabled = application.paused
        self.visible = self.visible
        mouse.locked = not mouse.locked
        mouse.visible = not mouse.visible


if __name__ == "__main__":
    app = Ursina()
    menu = Menu(app)
    app.run()
