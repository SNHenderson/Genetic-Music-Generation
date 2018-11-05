# Genetic-Music-Generation

This is a project that aims to generate a tune through genetic programming. This is done with ABC_NOTATION to encode the tunes and a self-written genetic algorithm. 

Usage: `bin/music_generator [-h] [-p POPULATION] [-m MAX] [-s SEED] [-c COST] [-n NUMBER] [-t TITLE] [-r] song`

**Positional arguments:**    
`song`: The name of the song

**optional arguments:**    
`  -h, --help`: show help message and exit    
`  -p POPULATION, --population POPULATION`: The size of the population    
`  -m MAX, --max MAX`: The max generation    
`  -s SEED, --seed SEED`: Random seed    
`  -c COST, --cost COST`: The cost to stop elvolving at    
`  -n NUMBER, --number NUMBER`: The number n for saving each nth generation    
`  -t TITLE, --title TITLE`: The title of the file to save    
`  -r, --reverse`: If included, save output in reverse order (target piece -> initial random piece)


