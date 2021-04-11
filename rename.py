import os
import pathlib

EXT = [".JPG", ".jpg"]
PRE = ["PG"]

def rename(root_dir=None, ext=EXT, pre=PRE, specifier="image"):
    """
    Renames files of interest by appending the specifier to the file path.
    Extracts files from folders not named by the prefix and rewrites their
    paths such that their parent folder becomes one with the specified prefix.

    param: root_dir - str beginning location of recursive file search
    param: ext - list of str - filetype of interest
    param: pre - list of str - prefix of parent folders to move files of interest into
    param: specifier - str - tag appended to files of interest
    return: None
    """
    try:
        dir_type = type(root_dir)
        if root_dir is None:
            root_dir = "."
        elif dir_type is str:
            root_dir = pathlib.PurePath(root_dir)
        else:
            raise TypeError(dir_type)

        file_type = ext
        item_label = specifier
        sub_dirs = os.listdir(root_dir)
        #dir_label = os.path.split(root_dir)[-1].split("_")[-1]
        count = 0
        for prefix in pre:
            for item in sub_dirs:
                class_label = None
                item_path = os.path.join(root_dir, item)
                item_type = os.path.splitext(item_path)[1]
                if item.startswith(prefix):
                    class_label = item.split(" ")[0]
                
                    if os.path.isdir(item_path):
                        rename(root_dir=item_path, ext=file_type, pre=PRE, specifier=item_label)
                    elif os.path.isfile(item_path) and item_type in ext:
                        count +=1
                        dest_path = str(root_dir) + f"\\{class_label}_{specifier}_{count}{item_type}"
                        print(dest_path)
                        #os.rename(item_path, dest_path)
                    else:
                        continue
                    
    except TypeError:
        print(f"Invalid root_dir type. Must be of type str or None. Input was of type {dir_type}.")


def main():
    start_dir= input("Enter an absolute filepath: ")
    rename(root_dir=start_dir)

if __name__ == '__main__': 
    main() 


