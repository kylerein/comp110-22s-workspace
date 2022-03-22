"""Example of importing Python."""


from lessons import helpers
#Alias a module -> naming it something else
from lessons import helpers as hp
#import names defined globally in a module
from lessons.helpers import powerful, THE_ANSWER


def main() -> None:
    """Entrypoint of"" program."""
    print(hp.powerful(2, 4))
    print(f"The answer: {helpers.THE_ANSWER}")


if __name__ == "__main__":
    main()