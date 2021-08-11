from my_sample_madlibs import ai, blockchain, eating, fitness
import random

if __name__ == "__main__":
    m = random.choice([ai, blockchain, eating, fitness])
    m.madlib()