import argparse

def parse():
    parser = argparse.ArgumentParser(description="Parse and generate a song.")
    parser.add_argument("song", help="The name of the song")
    parser.add_argument("-p", "--population", type=int, help="The size of the population")
    parser.add_argument("-m", "--max", type=int, help="The max generation")
    parser.add_argument("-s", "--seed", type=int, help="Random seed")
    parser.add_argument("-c", "--cost", type=int, help="The cost to stop elvolving at")
    
    return parser.parse_args()
