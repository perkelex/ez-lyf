import ctypes

# taken from shuberman's post at https://stackoverflow.com/questions/57647034/prevent-sleep-mode-python-wakelock-on-python
# slightly modified

class WindowsInhibitor:
        '''Prevent OS sleep/hibernate in windows; code from:
        https://github.com/h3llrais3r/Deluge-PreventSuspendPlus/blob/master/preventsuspendplus/core.py
        API documentation:
        https://msdn.microsoft.com/en-us/library/windows/desktop/aa373208(v=vs.85).aspx'''
        ES_CONTINUOUS = 0x80000000
        ES_SYSTEM_REQUIRED = 0x00000001
        ES_DISPLAY_REQUIRED = 0x00000002

        def __init__(self):
            pass

        @staticmethod
        def inhibit():
            print("Preventing Windows from going to sleep")
            ctypes.windll.kernel32.SetThreadExecutionState(
                WindowsInhibitor.ES_CONTINUOUS | \
                WindowsInhibitor.ES_SYSTEM_REQUIRED | \
                WindowsInhibitor.ES_DISPLAY_REQUIRED)

        @staticmethod
        def uninhibit():
            print("Allowing Windows to go to sleep")
            ctypes.windll.kernel32.SetThreadExecutionState(
                WindowsInhibitor.ES_CONTINUOUS)
