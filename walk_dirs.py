import os

""" Maps root directories and returns their file count.

    object => {path: file_count}
""" 
def walk_dirs(dirs):
  
    files_per_dir = {}
    dir_map = {}
    for d in dirs:
      
      
        dir_map[d] = 0 
        for occurence in dirs:
            if occurence == d:
                continue

            elif occurence in d:
                dir_map[d] += 1

    for key, val in dir_map.items():
        if val == 0:
        
           files_per_dir[key] = sum(len(files) for root, dirs, files in os.walk(key))

    return files_per_dir


visual_aid = """         
'/user/stuff' 0
'/user/stuff/cache' 1
'/user/stuff/cache/123' 0
'/user/other/stuff' 0""" 
