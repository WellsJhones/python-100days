from art import logo
print(logo)


bid_data = []


def add_bids(name, bid):
    participants = {
        "name": name,
        "bid": bid
    }
    bid_data.append(participants)


ask = True
winner = {
    "name": "hiii",
    "bid": 0
}
print(winner['bid'])
while ask == True:
    name = input("what's your name? \n")
    bid = int(input("What's the bid price: \n"))

    add_bids(name, bid)

    add_more_people = input(
        "more people will participate or update your bid? 'Yes' or 'no' \n").lower()

    if add_more_people == "no":
        ask = False
        for n in range(len(bid_data)):
            for key in bid_data[n]:
                # print(bid_data[n]['bid'] > winner['bid'])
                if bid_data[n]['bid'] > winner["bid"]:
                    winner['name'] = bid_data[n]["name"]
                    winner['bid'] = bid_data[n]['bid']
                #     print()
    print("The winner is {} with the highest bid of {}".format(
        winner["name"], winner["bid"]))
