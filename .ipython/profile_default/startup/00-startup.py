# .ipython/profile_default/startup/00-startup.py
import IPython

# 2. Crucial: Tell IPython to manage the Qt event loop in the background
ip = IPython.get_ipython()
if ip is not None:
    ip.run_line_magic("gui", "qt5")

print("Portable Xview IPython environment loaded. Ready to launch GUI!")
