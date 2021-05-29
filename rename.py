import os
import pathlib

EXT = [".JPG", ".jpg", ".png", ".PNG"]
PRE = ["PG"]

def rename(root_dir=None, f_types=EXT, classes=PRE, specifier="image"):
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

    try:
        dir_type = type(root_dir)
        if root_dir is None:
            root_dir = "."
        elif dir_type is str:
            root_dir = pathlib.PurePath(root_dir) # PurePath to make OS agnostic
        else:
            raise TypeError(dir_type)
        sub_dirs = os.listdir(root_dir)
        for prefix in classes:
            count = 0
            for item in sub_dirs:
                item_path = os.path.join(root_dir, item)
                if os.path.isdir(item_path):
                    rename(root_dir=item_path, f_types=f_types, classes=classes, specifier=specifier)
                elif os.path.isfile(item_path):
                        item_type = os.path.splitext(item_path)[1]
                        class_ID = f"{prefix}" + os.path.split(os.path.split(item_path)[0].split(prefix)[1])[0].split(" ")[0]
                        if item_type in f_types:
                            count += 1
                            dest_path = str(".") + f"\\renamed_images\\{class_ID}\\{class_ID}_{specifier}_{count}{item_type}"
                            os.rename(item_path, dest_path)

    except TypeError:
        print(f"Invalid root_dir type. Must be of type str or None. Input was of type {dir_type}.")


def main():
    start_dir= input("Enter an absolute filepath: ")
    #prefixes = input("Enter directory prefixes of interest separated by commas: ")
    #f_types = input("Enter file types of interest separated by commas: ")
    #tag = input("Enter a file of interest specifier (e.g. "image" without quotes): ")
    #os.makedirs(".\\renamed_images\\", exist_ok=False)
    print("running!")
    rename(root_dir=start_dir, f_types=EXT, classes=PRE)


if __name__ == '__main__':
    main()