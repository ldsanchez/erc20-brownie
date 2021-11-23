from brownie import (
    network,
    config,
    accounts,
)

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]


def get_account(index=None, id=None):
    # use different accounts
    # account[0] ganache-local
    # accpunts.add("env") enviroment-variables
    # accounts.load("id") brownie accounts
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])
