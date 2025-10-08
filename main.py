"""
Exercise 1.

4 Oct 2025
"""


def clear_screen() -> None:
    """Clear screen method."""
    print("\033c", end="")


def main() -> None:
    clear_screen()

    print("Hi Exercise 1.")


if __name__ == "__main__":
    main()
