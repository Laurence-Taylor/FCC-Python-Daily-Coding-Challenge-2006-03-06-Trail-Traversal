# Trail Traversal

Given an array of strings representing your trail map, return a string of the moves needed to get to your goal.

The given strings will contain the values:

    "C": Your current location
    "G": Your goal
    "T": Traversable parts of the trail
    "-": Untraversable parts of the map

Return a string with the moves needed to follow the trail from your location to your goal where:

    "R" is a move right

    "D" is a move down

    "L" is a move left

    "U" is a move up

    There will always be a single continuous trail, without any branching, from your current location to your goal.

    Each trail location will have a maximum of two traversable locations touching it.

For example, given:

[
"-CT--",
"--T--",
"--TT-",
"---T-",
"---G-"
]

Return "RDDRDD".
