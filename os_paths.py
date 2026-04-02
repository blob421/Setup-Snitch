os_paths = {'\\AppData\\Local\\Microsoft\\' :  ['loggz', 'odlgz', 'json', 'dat', 'tmp', 'log', 
                                                'ini', 'xml', 'txt','db', 'sqlite', 'vscdb','png', 
                                                'jpg', 'jpeg', 'TMP' ,'ldb', 'sst'], 

            '\\AppData\\Local\\D3DSCache\\': ['bin', 'dat', 'tmp'],

            '\\AppData\\Local\\Temp\\': ['tmp', 'temp', 'log','json', 'txt','dat', 'bin',
                                         'cab', 'msi', 'manifest','htm', 'html','png', 'jpg', 
                                         'jpeg'],
                                         
            '\\AppData\\Local\\Packages\\' : ['json', 'dat', 'tmp', 'log','xml', 'ini', 'txt',
                                              'db', 'sqlite','png', 'jpg', 'jpeg', 'db-wal', 'db-shm'],

            '\\ProgramData\\Microsoft\\Windows\\WER\\Temp\\': ['tmp', 'dmp', 'wer'],

            '\\ProgramData\\regid.1991-06.com.microsoft\\': ['xml', 'xrm-ms', 'dat'],

            '\\System32': ['log'],
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
