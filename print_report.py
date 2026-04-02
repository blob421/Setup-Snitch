
from walk_dirs import walk_dirs

def get_report(handler):
    sus_files = handler.suspicious_paths
    folders = handler.created_folders

    sus_files_length = len(sus_files.keys())
    folders_length = len(folders)

    print(f'\nSuspicious files found : {sus_files_length}')
    print('===========================================')
    if sus_files_length > 0:
        print('Idx   type    path         program \n')
        for key, val in sus_files.items():
            print(f'{key} {val['type']}  {val['path']}          {val['program']}')

    if handler.sus_events:
        print(f'\nSuspicious Events : {len(handler.sus_events)}')
        print('===========================================')
        print('Idx    reason            description \n')
        for idx, (key, val) in enumerate(handler.sus_events.items()):
            print(f'{idx}      {key}        {val}')

    files_per_dir = walk_dirs(folders)
    print(f'\n\nFolders created : {folders_length}')
    print('===========================================')    
    if folders_length > 0 :
        print('Idx  count   path\n')
        for idx, (key, val) in enumerate(files_per_dir.items()):
           print(f'{idx}  {val}  {key}')

    print(f'\n\nNew files in main installation dir : {handler.files_created_main}')
    print('===========================================')  

    outside  = walk_dirs(handler.written_paths)
    print(f'\n\nFiles created outside of main :')
    print('===========================================')
    if len(outside) > 0:
        print('Idx  count   path\n')
        for idx, (key, val) in enumerate(outside.items()):

            print(f' {idx}    {val}     {key}')

