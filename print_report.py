
from walk_dirs import walk_dirs

def get_report(handler):
    sus_files = handler.suspicious_paths
    written_files = handler.written_paths
    folders = handler.created_folders

    sus_files_length = len(sus_files.keys())
    folders_length = len(folders)

    print(f'\nSuspicious files found : {sus_files_length}')
    print('===========================================')
    if sus_files_length > 0:
        print('Idx         type           path\n')
        for key, val in sus_files.items():
            print(f'{key}           {val['type']}            {val['path']}')

    files_per_dir = walk_dirs(folders)
    print(f'\n\nFolders created : {folders_length}')
    print('===========================================')    
    if folders_length > 0 :
        print('Idx       new files          path\n')
        for idx, (key, val) in enumerate(files_per_dir.items()):
           print(f'{idx}            {val}              {key}')