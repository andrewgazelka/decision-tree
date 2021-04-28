import numpy as np


def entropy(*amounts):
    amounts = np.array(amounts)
    total = np.sum(amounts)
    probabilities = amounts / total
    arr = np.array(probabilities)
    assert -0.01 < arr.sum() < 1.01
    dot = arr * np.log2(arr + 1e-20)
    return -dot[0]


def split_entropy(*amounts):
    flat = sum(amounts, ())
    total = sum(flat)

    total_entropy = 0
    for amount in amounts:
        amount = np.array(amount)
        in_split = np.sum(amount)
        proportion = in_split / total
        total_entropy += proportion * entropy(*amount)

    print(total_entropy)


def first_layer():
    split_entropy(
        (5, 5),
        (2, 0),
        (7, 0)
    )

    split_entropy(
        (4, 2),
        (2, 4),
        (1, 1)
    )

    split_entropy(
        (3, 6),
        (4, 2),
    )


def second_layer():
    split_entropy(
        (3,0),
        (1,1),
        (1,0),
    )

    split_entropy(
        (1,1),
        (4, 0),
    )


if __name__ == "__main__":
    first_layer()
    second_layer()


