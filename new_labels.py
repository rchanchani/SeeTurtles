import os
import pathlib
import shutil

EXT = [".JPG", ".jpg", ".png", ".PNG"]
PRE = ["PG"]

def new_labels(count, root_dir=None, f_types=EXT, classes=PRE, specifier="image"):
    """
    Renames files of interest by appending the specifier to the file path.
    Extracts files from folders not named by the prefix and rewrites their
    paths such that their parent folder becomes one with the specified prefix
    and the entire set's parent folder becomes "renamed_images" within the 
    current directory.

    param: root_dir - str - beginning location of recursive file search
    param: f_types - list of str - filetype of interest
    param: classes - list of str - prefix of parent folders of files of interest
    param: specifier - str - tag appended to files of interest
    return: None
    """


   #try:
    #dir_type = type(root_dir)
    #if dir_type == str:
    root_dir = pathlib.PurePath(root_dir) # PurePath to make OS agnostic
    #else:
    #    raise TypeError(dir_type)
    dir_contents = os.listdir(root_dir)
    for prefix in classes:
    #count = 0
        for item in dir_contents:
            item_path = os.path.join(root_dir, item)
            if os.path.isdir(item_path):
                new_labels(count=count, root_dir=item_path, f_types=f_types, classes=classes, specifier=specifier)
            elif os.path.isfile(item_path):
                    item_type = os.path.splitext(item_path)[1]
                    class_ID = f"{prefix}" + os.path.split(os.path.split(item_path)[0].split(prefix)[1])[0].split(" ")[0]
                    count += 1
                    dest_path = pathlib.PurePath(f"./renamed_images/{class_ID}/")
                    if item_type in f_types:
                        os.makedirs(dest_path, exist_ok=True)
                        image_name = pathlib.PurePath(dest_path, pathlib.PurePath(f"{class_ID}_{specifier}_{count}{item_type}"))
                        shutil.copy(item_path, image_name)
                    else: continue

    #except TypeError:
    #    print(f"Invalid root_dir type. Must be of type str or None. Was of type {dir_type}.")


def main():
    count=0
    start_dir= input("Enter an absolute filepath: ")
    prefixes = input("Enter directory prefixes of interest separated by commas: ")
    f_types = input("Enter file types of interest separated by commas: ")
    tag = input("Enter a file of interest specifier (e.g. \"image\" without quotes): ")
    dest_parent_dir = pathlib.PurePath("./renamed_images/")
    os.makedirs(dest_parent_dir, exist_ok=True)
    new_labels(count=count, root_dir=start_dir)


if __name__ == '__main__':
    main()