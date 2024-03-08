import sys
from .warden_mapper import GTFO_WARDEN_MAPPER

def main(sys_args):
    wp_main = GTFO_WARDEN_MAPPER

    wp_main.run()

    return 0

def run():
    return main(sys.argv)

if __name__ == "__main__":
    main(sys.argv)