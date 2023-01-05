# Cat dog horse sorter
import pathlib
import argparse
import os
import shutil

def get_args():
    parser = argparse.ArgumentParser(description="Used to collect the directory and sort")
    parser.add_argument('--input_dir',type=pathlib.Path)
    parser.add_argument('--target_dir',type=pathlib.Path)
    args=parser.parse_args()
    return args

def collect_stats(dir):
    stats={'cat_num':0,'dog_num':0,'horse_num':0,'rider_num':0}
    files = os.listdir(dir)
    for specific_file in files:
        if "cat" in specific_file:
            stats['cat_num']=+1
        elif "dog" in specific_file:
            stats['dog_num']=+1
        elif "horse" in specific_file:
            stats['horse_num']=+1
        elif "rider" in specific_file:
            stats['rider_num']=+1
    return
def make_and_move(args,files):
    cat_dir=os.path.join(args.target_dir, "cat_picture")
    dog_dir=os.path.join(args.target_dir, "dog_picture")
    horse_dir=os.path.join(args.target_dir, "horse_picture")
    rider_dir=os.path.join(args.target_dir, "rider_picture")
    os.mkdir(cat_dir)
    os.mkdir(dog_dir)
    os.mkdir(horse_dir)
    os.mkdir(rider_dir)     # Making Complete

    for specific_file in files:
        if "cat" in specific_file:
            shutil.copy(os.path.join(args.input_dir,specific_file),cat_dir)
        elif "dog" in specific_file:
            shutil.copy(os.path.join(args.input_dir,specific_file),dog_dir)
        elif "horse" in specific_file:
            shutil.copy(os.path.join(args.input_dir,specific_file),horse_dir)
        elif "rider" in specific_file:
            shutil.copy(os.path.join(args.input_dir,specific_file),rider_dir)

    return

def main():
    args = get_args()
    files=os.listdir(args.input_dir)
    collect_stats(args.input_dir)
    make_and_move(args,files)
    #Move function
    return

if __name__ == "__main__":
    main()