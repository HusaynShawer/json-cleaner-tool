from model import CleanJson
import argparse

parser = argparse.ArgumentParser(description="JSON Clean code")

parser.add_argument("--input",required=True,help="path to input file")
parser.add_argument("--output",required=True,help="path to output file")

args = parser.parse_args()

clea_json = CleanJson(args.input)
data = clea_json.write_file(args.input,args.output)
print(data)