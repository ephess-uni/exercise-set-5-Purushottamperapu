"""ex_5_1.py"""
import argparse
try:
    from src.ex_5_0 import line_count
except ImportError:
    from ex_5_0 import line_count


def main(infile):
    """Call line_count with the infile argument."""
    line_count(infile)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description='This is a program that uses ex_5_0')
    parser.add_argument('infile',help='Name of the input file')
    args=parser.parse_args()
    line_count(args.infile)

