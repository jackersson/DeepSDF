"""
    python split_train_test.py -d data/ShapeNetV2/plane -o examples/splits
"""

import os
import json
import glob
import random
import typing as typ
import numpy as np


def list_files(folder: str, *, file_format: str = '.obj') -> typ.List[str]:
    pattern = '{0}/*{1}'.format(folder, file_format)
    filenames = glob.glob(pattern)
    return filenames


def split_train_test(dataset: list, *, train_ratio: float = 0.75) -> typ.Tuple[list, list]:
    """Create test/train split

    """
    n = len(dataset)
    np.random.shuffle(dataset)
    n_train = int(n * train_ratio)
    return dataset[:n_train], dataset[n_train:]


def save(filename: str, items: typ.List[str], *, dataset_name: str = "dataset", class_name: str = "object"):
    with open(filename, 'w') as f:
        json.dump({dataset_name: {class_name : items}}, f)

    print(f"Saved ({len(items)}) samples to {filename}")


def get_filename(fn: str) -> str:
    return os.path.splitext(os.path.basename(fn))[0]


if __name__ == "__main__":

    import argparse

    arg_parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description="Splits dataset for train and test",
    )

    arg_parser.add_argument(
        "--data_dir",
        "-d",
        dest="data_dir",
        required=True,
        help="The directory which holds the data to preprocess and append.",
    )

    arg_parser.add_argument(
        "--ratio",
        "-r",
        dest="ratio",
        required=False,
        default=0.75,
        help="Num samples in train dataset total * r, test dataset total * (1 - r)",
    )

    arg_parser.add_argument(
        "--output",
        "-o",
        dest="output",
        required=True,
        help="The outputs directory which holds splits.",
    )

    args = arg_parser.parse_args()

    data_dir = args.data_dir
    class_name = os.path.basename(data_dir)
    dataset_name = os.path.basename(os.path.dirname(data_dir))

    total_samples = list(map(get_filename, list_files(data_dir)))

    train_samples, test_samples = split_train_test(total_samples, train_ratio=args.ratio)

    filename = os.path.join(args.output, f"{dataset_name}_{class_name}s_train.json")
    save(filename, train_samples, dataset_name=dataset_name, class_name=class_name)

    filename = os.path.join(args.output, f"{dataset_name}_{class_name}s_test.json")
    save(filename, test_samples , dataset_name=dataset_name, class_name=class_name)