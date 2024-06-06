def read_txt(filepath: str):
    with open(filepath, "r") as file:
        return [row.strip() for row in file]


sybils = [wallet.lower() for wallet in read_txt("sybils.txt")]
wallets = [wallet.lower() for wallet in read_txt("wallets.txt")]

zero = 0
for i, wallet in enumerate(wallets, start=1):
    if wallet in sybils:
        print(f"{i} | {wallet}")
        zero += 1
print(f"\nyou have {zero} sybil wallets")
