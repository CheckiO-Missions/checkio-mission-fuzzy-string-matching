"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["apple", "appel", 2],
            "answer": True
        },
        {
            "input": ["apple", "bpple", 1],
            "answer": True
        },
        {
            "input": ["apple", "bpple", 0],
            "answer": False
        },
        {
            "input": ["apple", "apples", 1],
            "answer": True
        },
        {
            "input": ["apple", "bpples", 2],
            "answer": True
        },
        {
            "input": ["apple", "apxle", 1],
            "answer": True
        },
        {
            "input": ["apple", "pxxli", 3],
            "answer": False
        },
    ],
    "Extra": [
        {
            "input": ["hello world", "hxllo world", 1],
            "answer": True
        },
        {
            "input": ["fuzzy", "fuzy", 2],
            "answer": True
        },
        {
            "input": ["apple", "apples", 0],
            "answer": False
        },
    ]
}
