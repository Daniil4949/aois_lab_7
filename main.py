from memory import Processor


def main():
    block = Processor(5, 8)
    print(f"Memory - {block.associative_memory}")
    print(f"Find nearest lesser value - {block.find_nearest_value(1)}")
    print(f"Find nearest greater value - {block.find_nearest_value(1, reverse=True)}")
    print(f"Min to max - {block.sort_min_to_max()}")
    print(f"Max to min - {block.sort_max_to_min()}")


if __name__ == "__main__":
    main()
