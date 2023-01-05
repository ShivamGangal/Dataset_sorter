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

def get_class_name(self,specific_file):
    specific_file_class = specific_file.split('.')[0]
    if '-' in specific_file_class:
        specific_file_class = specific_file_class.split('-')[0]
    return specific_file_class

def collect_stats(dir):
    stats={}
    files = os.listdir(dir)
    for specific_file in files:
        specific_file_class = self.get_class_name(specific_file)        
        if specific_file_class not in stats:
            stats[specific_file_class]=1
        else:
            stats[specific_file_class]+=1
    return stats

def make_and_move(args,stats):
    keys=list(stats.keys())
    directories={}
    for k in keys:
        directories[k] = os.path.join(args.target_dir,k)
        if os.path.isdir(directories[k]):
            pass
        else:
            os.mkdir(directories[k])   
   
    files=os.listdir(args.input_dir)
    for specific_file in files:
        specific_file_class = specific_file.split('.')[0]
        if specific_file_class in specific_file:
            shutil.copy(os.path.join(args.input_dir,specific_file),directories[specific_file_class])

    return

def main():
    args = get_args()
    stats = collect_stats(args.input_dir)
    make_and_move(args,stats)
    return

if __name__ == "__main__":
    main()