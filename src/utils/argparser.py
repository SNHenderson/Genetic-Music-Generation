import argparse


def parse():
    """Add arguments to arg parse and parses """
    parser = argparse.ArgumentParser(description="Parse and generate a song.")
    parser.add_argument("song", help="The name of the song")
    parser.add_argument("-p", "--population", type=int,
                        help="The size of the population")
    parser.add_argument("-m", "--max", type=int, help="The max generation")
    parser.add_argument("-s", "--seed", type=int, help="Random seed")
    parser.add_argument("-r", "--reverse", action='store_true', help="Reverse the order of the final song")
    parser.add_argument(
        "-c",
        "--cost",
        type=int,
        help="The cost to stop elvolving at")
    parser.add_argument(
        "-n",
        "--number",
        type=int,
        help="The number n for saving each nth generation")
    parser.add_argument(
        "-t",
        "--title",
        type=int,
        help="The title of the file to save")

    return parser.parse_args()
