import os
def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found, NOT include '.'
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if suffix == '':
        return []
    
    # Base condition
    if os.listdir(path)==[]:
        return []
    
    output = []
    
    cur_folder = os.listdir(path) # list all elements in current folder
    files = [] 
    folders = []
    for ele in cur_folder:
        if '.'+suffix in ele:
            files.append(ele)
        elif '.' not in ele:
            folders.append(ele)
    for folder in folders:
        sub_path = path + '/'+folder
        files.extend(find_files(suffix,sub_path))
    return files

# Testing case
if __name__=='__main__':
    path = 'testdir'
    # test case 1
    print(find_files('c',path)) #['t1.c', 'b.c', 'a.c', 'a.c']
    # test case 2
    print(find_files('h',path)) # ['t1.c', 'b.c', 'a.c', 'a.c']
    # test case 3: edge case
    print(find_files('txt',path)) # [], no such file type in the directionary
    print(find_files('',path)) #[], suffix is empty
    