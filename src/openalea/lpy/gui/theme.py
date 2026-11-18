"""
L-Py GUI Theme management (Dark and Light themes).
Provides modern dark/light styling and syntax highlighting palettes.
"""

from openalea.plantgl.gui.qt.QtGui import QColor

# Syntax highlighting color schemes
DARK_SYNTAX_COLORS = {
    'lpykeyword': '#C678DD',   # Vibrant purple for L-Py keywords (Axiom, production, produce, etc.)
    'keyword': '#61AFEF',      # Vibrant cyan/blue for Python keywords (def, if, for, etc.)
    'delimiter': '#ABB2BF',    # Light neutral for delimiters () [] {} + - * / : < > =
    'prod': '#E5C07B',         # Golden amber for L-system rewrite arrows (-->) and productions
    'func': '#61AFEF',         # Cyan for function def names
    'string': '#98C379',       # Soft green for strings
    'number': '#D19A66',       # Warm orange for numbers
    'comment': '#7F848E',      # Muted slate gray for comments
    'tab': '#3A3F4B',          # Subtle dark tab block
    'space': '#2C313A',        # Subtle dark space block
}

LIGHT_SYNTAX_COLORS = {
    'lpykeyword': '#8B008B',   # darkMagenta
    'keyword': '#0000FF',      # blue
    'delimiter': '#00008B',    # darkBlue
    'prod': '#000000',         # black
    'func': '#FF00FF',         # magenta
    'string': '#A9A9A9',       # darkGray
    'number': '#FF0000',       # red
    'comment': '#006400',      # darkGreen
    'tab': '#DCDCDC',          # 220, 220, 220
    'space': '#F0F0F0',        # 240, 240, 240
}

# Editor specific styles
DARK_EDITOR_STYLESHEET = """
QTextEdit {
    background-color: #21252B;
    color: #ABB2BF;
    selection-background-color: #3E4451;
    selection-color: #FFFFFF;
    border: none;
}
"""

LIGHT_EDITOR_STYLESHEET = """
QTextEdit {
    background-color: #FFFFFF;
    color: #000000;
    selection-background-color: #B5D5FF;
    selection-color: #000000;
    border: none;
}
"""

# Shell specific dark stylesheet for QtConsole (RichJupyterWidget)
DARK_SHELL_STYLESHEET = """
QPlainTextEdit, QTextEdit {
    background-color: #21252B;
    background-clip: padding;
    color: #ABB2BF;
    selection-background-color: #3E4451;
    selection-color: #FFFFFF;
}
.inverted {
    background-color: #ABB2BF;
    color: #21252B;
}
.error { color: #E06C75; }
.in-prompt-number { font-weight: bold; }
.out-prompt-number { font-weight: bold; }
.in-prompt, .in-prompt-number { color: #98C379; }
.out-prompt, .out-prompt-number { color: #E5C07B; }
"""

# Global application stylesheet for Dark Theme
DARK_APP_STYLESHEET = """
/* Global Window & Basic Widget Styling */
QWidget {
    background-color: #282C34;
    color: #ABB2BF;
}

QMainWindow {
    background-color: #21252B;
}

QMainWindow::separator {
    background-color: #1E2227;
    width: 4px;
    height: 4px;
}

QMainWindow::separator:hover {
    background-color: #61AFEF;
}

/* ToolBar */
QToolBar {
    background-color: #21252B;
    border-bottom: 1px solid #1E2227;
    spacing: 4px;
    padding: 2px;
}

QToolBar::separator {
    background-color: #3E4451;
    width: 1px;
    margin: 4px 6px;
}

QToolButton {
    background-color: transparent;
    color: #ABB2BF;
    border: 1px solid transparent;
    border-radius: 3px;
    padding: 3px 5px;
    margin: 1px;
}

QToolButton:hover {
    background-color: #3E4451;
    color: #FFFFFF;
    border: 1px solid #4B5263;
}

QToolButton:pressed, QToolButton:checked {
    background-color: #2C313A;
    color: #61AFEF;
    border: 1px solid #61AFEF;
}

QToolButton:disabled {
    color: #5C6370;
}

/* Menu Bar & Menus */
QMenuBar {
    background-color: #21252B;
    color: #ABB2BF;
    border-bottom: 1px solid #1E2227;
    padding: 2px;
}

QMenuBar::item {
    background: transparent;
    padding: 4px 8px;
    border-radius: 2px;
}

QMenuBar::item:selected {
    background-color: #3E4451;
    color: #FFFFFF;
}

QMenu {
    background-color: #282C34;
    color: #ABB2BF;
    border: 1px solid #181A1F;
    padding: 4px 0px;
}

QMenu::item {
    padding: 5px 25px 5px 20px;
    border: 1px solid transparent;
}

QMenu::item:selected {
    background-color: #3E4451;
    color: #FFFFFF;
}

QMenu::item:disabled {
    color: #5C6370;
}

QMenu::separator {
    height: 1px;
    background-color: #3E4451;
    margin: 4px 8px;
}

/* Dock Widgets */
QDockWidget {
    color: #ABB2BF;
    titlebar-close-icon: none;
    titlebar-normal-icon: none;
}

QDockWidget::title {
    background-color: #21252B;
    padding: 5px 8px;
    border-bottom: 1px solid #1E2227;
    font-weight: bold;
    color: #DCDFE4;
}

/* Tab Bar & Tabs */
QTabBar {
    background-color: #21252B;
    qproperty-drawBase: 0;
}

QTabBar::tab {
    background-color: #282C34;
    color: #7F848E;
    border: 1px solid #181A1F;
    border-bottom: none;
    padding: 6px 12px;
    margin-right: 2px;
    border-top-left-radius: 3px;
    border-top-right-radius: 3px;
}

QTabBar::tab:hover {
    background-color: #323842;
    color: #ABB2BF;
}

QTabBar::tab:selected {
    background-color: #21252B;
    color: #FFFFFF;
    border-top: 2px solid #61AFEF;
}

QTabWidget::pane {
    border: 1px solid #181A1F;
    background-color: #282C34;
}

/* Inputs: QLineEdit, QSpinBox, QComboBox */
QLineEdit, QSpinBox, QDoubleSpinBox {
    background-color: #1E2227;
    color: #DCDFE4;
    border: 1px solid #3E4451;
    border-radius: 3px;
    padding: 3px 6px;
    selection-background-color: #3E4451;
    selection-color: #FFFFFF;
}

QLineEdit:focus, QSpinBox:focus, QDoubleSpinBox:focus {
    border: 1px solid #61AFEF;
}

QComboBox {
    background-color: #1E2227;
    color: #DCDFE4;
    border: 1px solid #3E4451;
    border-radius: 3px;
    padding: 3px 6px;
    min-width: 60px;
}

QComboBox:focus {
    border: 1px solid #61AFEF;
}

QComboBox::drop-down {
    border: none;
    width: 20px;
}

QComboBox QAbstractItemView {
    background-color: #282C34;
    color: #ABB2BF;
    selection-background-color: #3E4451;
    selection-color: #FFFFFF;
    border: 1px solid #181A1F;
}

/* Push Buttons */
QPushButton {
    background-color: #353B45;
    color: #DCDFE4;
    border: 1px solid #4B5263;
    border-radius: 3px;
    padding: 4px 12px;
    min-height: 18px;
}

QPushButton:hover {
    background-color: #3E4451;
    color: #FFFFFF;
    border-color: #61AFEF;
}

QPushButton:pressed {
    background-color: #282C34;
}

QPushButton:disabled {
    background-color: #282C34;
    color: #5C6370;
    border-color: #3E4451;
}

/* CheckBox & RadioButton */
QCheckBox, QRadioButton {
    color: #ABB2BF;
    spacing: 5px;
}

QCheckBox:disabled, QRadioButton:disabled {
    color: #5C6370;
}

/* GroupBox */
QGroupBox {
    border: 1px solid #3E4451;
    border-radius: 4px;
    margin-top: 10px;
    padding-top: 10px;
    font-weight: bold;
}

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top left;
    padding: 0 4px;
    color: #61AFEF;
}

/* Status Bar */
QStatusBar {
    background-color: #21252B;
    color: #7F848E;
    border-top: 1px solid #1E2227;
}

QStatusBar::item {
    border: none;
}

/* ScrollBars */
QScrollBar:vertical {
    background-color: #21252B;
    width: 10px;
    margin: 0px;
}

QScrollBar::handle:vertical {
    background-color: #4B5263;
    min-height: 20px;
    border-radius: 5px;
    margin: 2px;
}

QScrollBar::handle:vertical:hover {
    background-color: #5C6370;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}

QScrollBar:horizontal {
    background-color: #21252B;
    height: 10px;
    margin: 0px;
}

QScrollBar::handle:horizontal {
    background-color: #4B5263;
    min-width: 20px;
    border-radius: 5px;
    margin: 2px;
}

QScrollBar::handle:horizontal:hover {
    background-color: #5C6370;
}

QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
    width: 0px;
}

/* Tree, Table, List Views */
QTreeView, QTableView, QListView {
    background-color: #21252B;
    color: #ABB2BF;
    border: 1px solid #181A1F;
    alternate-background-color: #282C34;
    selection-background-color: #3E4451;
    selection-color: #FFFFFF;
}

QHeaderView::section {
    background-color: #282C34;
    color: #ABB2BF;
    padding: 4px 6px;
    border: 1px solid #181A1F;
}

/* Splitter */
QSplitter::handle {
    background-color: #1E2227;
}

QSplitter::handle:hover {
    background-color: #61AFEF;
}

/* Dialogs */
QDialog {
    background-color: #282C34;
    color: #ABB2BF;
}
"""

def is_dark_theme(theme_name):
    """Check if the given theme name corresponds to dark mode."""
    return str(theme_name).strip().lower() == 'dark'

def get_syntax_colors(theme_name):
    """Get the dictionary of syntax highlighting colors for the theme."""
    if is_dark_theme(theme_name):
        return DARK_SYNTAX_COLORS
    return LIGHT_SYNTAX_COLORS

def set_dark_title_bar(window, is_dark=True):
    """
    Sets the native window title bar to dark mode on Windows 10/11 using the DWM API.
    """
    import sys
    if sys.platform != 'win32' or window is None:
        return
    try:
        import ctypes
        hwnd = int(window.winId())
        DWMWA_USE_IMMERSIVE_DARK_MODE = 20
        DWMWA_USE_IMMERSIVE_DARK_MODE_BEFORE_20H1 = 19
        value = ctypes.c_int(1 if is_dark else 0)

        # Try modern Windows 10 (20H1+) and Windows 11 attribute first
        res = ctypes.windll.dwmapi.DwmSetWindowAttribute(
            hwnd,
            DWMWA_USE_IMMERSIVE_DARK_MODE,
            ctypes.byref(value),
            ctypes.sizeof(value)
        )
        if res != 0:
            # Fallback for Windows 10 builds 1809 - 1909
            ctypes.windll.dwmapi.DwmSetWindowAttribute(
                hwnd,
                DWMWA_USE_IMMERSIVE_DARK_MODE_BEFORE_20H1,
                ctypes.byref(value),
                ctypes.sizeof(value)
            )
    except Exception:
        pass

def apply_theme(window, theme_name='dark'):
    """
    Apply a theme ('dark' or 'light') to a window or widget.
    """
    is_dark = is_dark_theme(theme_name)
    if is_dark:
        window.setStyleSheet(DARK_APP_STYLESHEET)
    else:
        window.setStyleSheet("")
    set_dark_title_bar(window, is_dark)
