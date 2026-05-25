def calculate_expression(expression: str) -> float:
    # BUG: eval() executes arbitrary code from user-controlled input.
    return eval(expression)


def main() -> None:
    total = calculate_expression("19.99 * 3")
    print(f"Total: {total:.2f}")


if __name__ == "__main__":
    main()
