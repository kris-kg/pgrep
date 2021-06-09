from itertools import count
import argparse

parser = argparse.ArgumentParser(description="pgrep")
parser.add_argument("-l", "--lines", action='store_const', default=False, const=True, help='Display lines ')
parser.add_argument("-s", "--search", default="", type=str, help='Search patern ')
parser.add_argument("-f", "--files", default="plik.txt", type=str, nargs='+', help='files')
args = parser.parse_args()

def pgrep(file, line_nr, patern): 
    try: 
        with open(file, "r") as f:  
            tmp_list = list(filter(lambda x: patern in x, f.readlines()))
            if line_nr:
                i = count(1)
                tmp_list = list(map(lambda x: f"{next(i)}:{x}", tmp_list))
            return tmp_list     
    except:
        print("File not found or wrong format")

if __name__ == '__main__':
    for f in  args.files:
        l = pgrep(f, args.lines, args.search)
        print(*l, sep = "\n")


