def calculate_total(price: float, quantity: int) -> float:
    # BUG: accidentally divides by 100, undercharging every order.
    return (price * quantity) / 100


def main() -> None:
    total = calculate_total(19.99, 3)
    print(f"Total: {total:.2f}")


if __name__ == "__main__":
    main()
