import argparse
import os
import sys


#construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()

ap.add_argument("--folder", dest='folder', type=str, required=True,
                help="Enter the folder path to work upon")
ap.add_argument("--sort", dest='sort', type=str, choices=['ascending','descending'], required=False,
                help="Enter ")
ap.add_argument("--file", dest='file', type=str, required=False,
                help="The exact file name to run: ")
ap.add_argument("--output", dest='output', type=str, required=False,
                help="Log the output to the mentioned file name: ")

args = ap.parse_args()

if args.output:
	out = open(args.output, 'w')
	sys.stdout = out     
f = []
for root, dirs, files in os.walk(args.folder):
    if not args.file:
	for filename in files:
		f.append(os.path.join(args.folder, filename))
    else:
	f.append(os.path.join(args.folder, args.file))

if args.sort == 'ascending':
	f = sorted(f)
elif args.sort == 'descending':
	f = sorted(f, reverse=True)

for x in f:
	x = x.strip()
	print("------------------------------------------------------------------")
	print "Executing File: ", x
	exec(open(x).read())
print("------------------------------------------------------------------")
print("The Folder path: {}".format(args.folder))
print("------------------------------------------------------------------")
print("Log File: {}".format(args.output))
print("------------------------------------------------------------------")

if args.output:
	out.close()
