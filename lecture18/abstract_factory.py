# Абстрактні класи для продуктів
class Button:
    def click(self):
        pass


class Window:
    def render(self):
        pass


# Абстрактна фабрика
class GUIFactory:
    def create_button(self):
        pass

    def create_window(self):
        pass


# Конкретні продукти для Windows
class WindowsButton(Button):
    def click(self):
        print("Windows button clicked")


class WindowsWindow(Window):
    def render(self):
        print("Windows window rendered")


# Конкретні продукти для MacOS
class MacOSButton(Button):
    def click(self):
        print("MacOS button clicked")


class MacOSWindow(Window):
    def render(self):
        print("MacOS window rendered")


# Конкретні фабрики
class WindowsGUIFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_window(self):
        return WindowsWindow()


class MacOSGUIFactory(GUIFactory):
    def create_button(self):
        return MacOSButton()

    def create_window(self):
        return MacOSWindow()


# Використання
def create_gui(factory):
    button = factory.create_button()
    window = factory.create_window()
    return button, window


windows_factory = WindowsGUIFactory()
macos_factory = MacOSGUIFactory()

windows_button, windows_window = create_gui(windows_factory)
macos_button, macos_window = create_gui(macos_factory)

windows_button.click()
windows_window.render()

macos_button.click()
macos_window.render()

