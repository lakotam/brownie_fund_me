from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print(
        f"The current entry fee is 50 * 10**18 * 10 ** 18 / {fund_me.getPrice()} = {entrance_fee}"
    )
    print(f"The current price is {fund_me.getPrice()}")
    print(f"Check if {fund_me.getPrice()} * {entrance_fee} / 1 *10**18 >= 50")
    print("Funding...")

    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
