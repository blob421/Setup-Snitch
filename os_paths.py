

SUSPICIOUS_EXTS = [
    # Executables                       # Scripts
     'exe', 'dll', 'sys', 'drv', 'ocx', 'bat', 'cmd', 'ps1', 'psm1', 'vbs', 'vbe',
     'js', 'jse', 'wsf', 'wsh',
    # Installers / archives    # Droppers / payloads        # Python (rare outside dev)
    'msi', 'msp', 'cab', 'pkg', 'scr', 'pif', 'com', 'jar', 'py', 'pyc', 'pyo',
    # Office macro formats # Shellcode containers
    'docm', 'xlsm', 'pptm', 'bin', 'dat' 
]

EXCEPTIONS_BY_PATH = ({ '\\Windows\\Temp': ['msi', 'msp', 'cab', 'dat'], 
                        '\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup': [], 
                        'ProgramData\\Microsoft\\Windows\\Start Menu\\Programs': [], 
                        '\\ProgramData\\Microsoft\\Windows\\AppRepository\\': [], 
                        '\\AppData\\Local\\Microsoft\\': ['bin', 'dat'], 
                        '\\AppData\\Local\\D3DSCache\\': ['bin', 'dat'], 
                        '\\AppData\\Local\\Temp\\': ['msi', 'cab', 'bin', 'dat'], 
                        '\\AppData\\Local\\Packages\\': ['bin', 'dat'], 
                        '\\ProgramData\\Microsoft\\Windows\\WER\\Temp\\': [],
                        '\\ProgramData\\Microsoft': ['dat'], 
                        '\\ProgramData\\regid.1991-06.com.microsoft\\': ['dat'], 
                        '\\System32': [],
                        '\\C:\\ProgramData\\Mozilla': ['bin', 'sqlite'],
                        '\\AppData\\Roaming\\Mozilla\\Firefox' : ['js', 'json']
                        }
                        )





### *** Used to build my exceptions list 
"""exceptions_by_path = {}
def find_match():
    global copy, exceptions_by_path
    allowed_by_path = os_paths.copy()

    for key, val in allowed_by_path.items():
        exts = SUSPICIOUS_EXTS.copy()
        allowed_by_path[key] = exts
    
    for bad_ext in SUSPICIOUS_EXTS:
        for key, val in os_paths.items():

            if not exceptions_by_path.get(key):
                exceptions_by_path[key] = []

            if val and bad_ext in val:
                 allowed_by_path[key].remove(bad_ext)
                 exceptions_by_path[key].append(bad_ext)"""
 

