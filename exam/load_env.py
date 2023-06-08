
import os 
from dotenv import load_dotenv

def dump_env():
    # for key, val in os.environ.items():
    #    print(key, " = ", val)
    return os.environ.copy()

def dump_diff(env1, env2):
    key1 = set(env1.keys())
    key2 = set(env2.keys())
    diff = key2 - key1 
    return diff

if __name__ == "__main__":
    env1 = dump_env()
    load_dotenv()
    env2 = dump_env()

    diff = dump_diff(env1, env2)
    print(list(diff))

    print(os.environ["XXX1"])
    print(os.environ["XXX2"])
