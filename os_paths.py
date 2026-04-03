
SAFE_TEMP_EXTS = [
    # Windows noise / housekeeping
    "tmp", "temp", "log", "etl", "blf", "regtrans-ms",
    "dmp", "mdmp", "hdmp",

    # Installer / updater noise
    "cab", "msi", "msp", "bak", "old", "manifest",
    "cat", "mum", "psf", "sqm",

    # Browser & app caches
    "crdownload", "part", "dat", "sqlite", "sqlite-shm",
    "sqlite-wal", "json", "txt", "ini", "cfg", "cache",
    "ico", "png", "jpg", "gif",

    # AppX / UWP deployment
    "pri", "appx", "appxsym", "appxblockmap",
    "appxsignature", "xml",

    # Windows Search / indexing
    "edb", "jrs", "chk"
]


os_paths = {'\\Windows\\Temp': SAFE_TEMP_EXTS,
            
             ## STARTUP FOLDER 
            '\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup': [],
        
            'ProgramData\\Microsoft\\Windows\\Start Menu\\Programs': ['lnk'],
            '\\ProgramData\\Microsoft\\Windows\\AppRepository\\': ['pckgdep', 'rslc', 'xml'],
    
            '\\AppData\\Local\\Microsoft\\' :  ['loggz', 'odlgz', 'json', 'dat', 'tmp', 'log', 
                                                'ini', 'xml', 'txt','db', 'sqlite', 'vscdb','png', 
                                                'jpg', 'jpeg', 'TMP' ,'ldb', 'sst', '', 
                                                'tbres', 'bin'], 

            '\\AppData\\Local\\D3DSCache\\': ['bin', 'dat', 'tmp', 'dxcache-wal', 'dxcache-shm'],

            '\\AppData\\Local\\Temp\\': ['tmp', 'temp', 'log','json', 'txt','dat', 'bin',
                                         'cab', 'msi', 'manifest','htm', 'html','png', 'jpg', 
                                         'jpeg', 'xml'],
                                         
            '\\AppData\\Local\\Packages\\' : ['json', 'dat', 'tmp', 'log','xml', 'ini', 'txt',
                                              'db', 'sqlite','png', 'jpg', 'jpeg', 'db-wal', 
                                              'db-shm', 'bin', 'bak', 'TMP', 'lock'],

            '\\ProgramData\\Microsoft\\Windows\\WER\\Temp\\': ['tmp', 'dmp', 'wer'],
            '\\ProgramData\\Microsoft' : ["dat"],

            '\\ProgramData\\regid.1991-06.com.microsoft\\': ['xml', 'xrm-ms', 'dat'],

            '\\System32': ['log', 'blf', 'regtrans-ms', 'etl'],
}

SUSPICIOUS_EXTS = [
    # Executables
    'exe', 'dll', 'sys', 'drv', 'ocx',

    # Scripts
    'bat', 'cmd', 'ps1', 'psm1', 'vbs', 'vbe',
    'js', 'jse', 'wsf', 'wsh',

    # Installers / archives
    'msi', 'msp', 'cab', 'pkg',

    # Droppers / payloads
    'scr', 'pif', 'com', 'jar',

    # Python (rare outside dev)
    'py', 'pyc', 'pyo',

    # Office macro formats
    'docm', 'xlsm', 'pptm',

    # Shellcode containers
    'bin', 'dat'  # only suspicious outside known OS folders
]
