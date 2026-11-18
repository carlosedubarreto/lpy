

from qtconsole.rich_jupyter_widget import RichJupyterWidget
from qtconsole.inprocess import QtInProcessKernelManager
# from .streamredirection import GraphicalStreamRedirection
import sys, tempfile

class LpyShellWidget(RichJupyterWidget): #, GraphicalStreamRedirection):

    def __init__(self, parent=None):
        """
        :param  parent: specifies the parent widget.
        If no parent widget has been specified, it is possible to
        exit the interpreter by Ctrl-D.
        """
        if sys.executable.endswith('pythonw.exe'):
            lpylog = open(tempfile.gettempdir() + '/lpylog.txt', 'w')
            sys.stdout = lpylog 
            sys.stderr = lpylog

        RichJupyterWidget.__init__(self, parent)

        self.kernel_manager = QtInProcessKernelManager()
        self.kernel_manager.start_kernel(show_banner=False)

        self.kernel = self.kernel_manager.kernel
        self.kernel.gui = 'qt'

        self.shell = self.kernel.shell

        self.kernel_client = self.kernel_manager.client()
        self.kernel_client.start_channels()

        self.kernel.locals = self.kernel.shell.user_ns
        self.currentTheme = 'dark'
        self.setTheme(self.currentTheme)

        # Multiple Stream Redirection
        # GraphicalStreamRedirection.__init__(self, self.kernel.stdout, self.kernel.stderr)

    def setTheme(self, theme='dark'):
        self.currentTheme = theme
        try:
            from . import theme as lpytheme
            if lpytheme.is_dark_theme(theme):
                self.syntax_style = 'monokai'
                self.style_sheet = lpytheme.DARK_SHELL_STYLESHEET
            else:
                self.set_default_style('lightbg')
        except Exception:
            try:
                if str(theme).lower() == 'dark':
                    self.set_default_style('linux')
                else:
                    self.set_default_style('lightbg')
            except Exception:
                pass


def set_shell_widget(lpywidget):
    ipython_widget = LpyShellWidget(lpywidget.interpreterDock)
    if hasattr(lpywidget, 'currentTheme'):
        ipython_widget.setTheme(lpywidget.currentTheme)
    lpywidget.interpreterDock.setWidget(ipython_widget)

    kernel = ipython_widget.kernel

    lpywidget.shellwidget = ipython_widget
    lpywidget.interpreter = kernel
    lpywidget.shell = kernel.shell

    lpywidget.shellstdout = kernel.stdout
    lpywidget.shellstderr = kernel.stderr

    try:
        sys.stdout = kernel.stdout
        sys.stderr = kernel.stderr
    except Exception:
        print("cannot redirect sys.stdout to kernel.stdout")