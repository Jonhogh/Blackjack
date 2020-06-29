# # import random
# # deck=[]
# # suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
# # numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
# # for n in numbers:
# #     for s in suits:
# #         deck.append(n + " of " + s)
# # print(deck)

deck_dict = {
    '2 of Spades': https://uc0ada720f315793f4aaa568c35c.previews.dropboxusercontent.com/p/thumb/AA209EqvxQJn-gchZjjB4pAB6qwTrZLawX5W50gnp6sIg6LJ4bEADyNvCY-xwgCRNB2hFg1Q0H41nK1LKODBGTWv_buKNoxF-s4f9Ay8ps_9Elk2NKIKZsUMBLbynjKXzNPdSPmwqPKiYcXGn_e8dpG5u0LZtqj6ZVjYjhKVP25ekCpb2RFiyW4icc6c3ABNax1PMYxmyWb5lR0D3vPTFDWGzpjizcrC44V-eoX4xJtjOVZJjI9xGg30L7jePISMQ-AAJyCaLxU-J7-K4XaGwPleiuSQkBH9TtRTY6iAna8bhnNQWXtuJo8zJMhqQTUNn-F9nhbEDTuaJLodpNaCbVlUKPIZX2uwsVp-3Sp6n1pbpw/p.png?size=178x178&size_mode=1,
    '2 of Hearts': https://uce0b6e5ac21fc03f7225009ad6f.previews.dropboxusercontent.com/p/thumb/AA1C_aKxXtcoO6OEAVIPTgmtGX24ElqYoxnvldjRyZn3CYwr1zFfQbV4e5iX3_0_I_1Gb3FF1PqFyt1-68kfNR482U8QC7_QD-nzCuOkWQvymLZsBblFdM35pXu0GzCgy55oS5CZNl2E55C9NGSbHdcUnCLXpjq9PKxfTBaSHm9CFU87vRvESgWqN29Wk2p50gKFscZEWx_T6fu_N8_c7fDMA9p0-SyVzXkagkJjvEHuoTzfQGOCp-dKDn8AiPHT-L7jSWROrM6xTibc-5kIYl3NvvJdLoePzpoLwfu-jcdZ5i7DmbY9LF6qOELWV9mc9AoZFOpXoh3HE-OYToMtfRm6mDQhqy5e5WXimdOVQNI2dA/p.png?size=178x178&size_mode=1,
    '2 of Clubs': https://uc915cf48682fe91602b930187cc.previews.dropboxusercontent.com/p/thumb/AA2eUSh83ZYFh0HfrmGIpCISGjMfcu4IQ79ixvq78zil7Uf9ra3TD6X1HG0fRZ1gfPXFf7fnwkprdH5tSK-yE478bqRobY9Dn8FtMJmvxbfou8sEkJ_d9nbOaLLTTSiKNj4htGDh5PlSi-hCWoKEk_Nz4CdeorSGu0Tqlt2fFCWILulGKq7s-fzIhT1LuYJhCkX5Cf3P1JosP8r2qss2Or4_WrJ3lHwuNmTDpEUsOj0khVc3apDS60AIw6mhRHJT2u7BJlPlkPEFblCId1icy7k9mRQFvbo4qr7w8haVlyuGKX7obSoI74au8MLR6BNNulp95EDAdzuUUsc30axOcNX3ZNNIXQ0YfaHtUDDGElD6GQ/p.png?fv_content=true&size_mode=5,
    '2 of Diamonds': https://ucad7a5b3c895922e1e7f04a6be3.previews.dropboxusercontent.com/p/thumb/AA09N-Rn0t24Pm54SpfiDgcjfOOfLyjMF5nCoRFH6R1R012KdGAfezpklHbpmnhQmegObouYHjrg3AY4nDPhLOXgSGkgZ449geoLwkXlLydKK2P47mKExuMUtmvD4qvWJI4AqbceEZxBAVaz_9PMl5Uq_6VXOyXqdtW3iqWIqfJGd4JXsZjkyNA0VoIoJyYwctmNeNKZd8917qX6K7xW0HIPoaNT0DGA4qfPgNbIYUmmf0LaXAelCFEqyQeMZZZf1XFO9LUR3tWr0gyjZTqYQCs3A3OHZMy_Xw3FULWnWTFqfd565a9UhGIYfj7OE5dg7JTZWixJKqhKrpUfmP2Z69BikwEBdjtyBruXzlKv3XvGBQ/p.png?size=178x178&size_mode=1,
    # '3 of Spades': 3,
    # '3 of Hearts': 3,
    # '3 of Clubs': 3,
    # '3 of Diamonds': 3,
    # '4 of Spades': 4,
    # '4 of Hearts': 4,
    # '4 of Clubs': 4,
    # '4 of Diamonds': 4,
    # '5 of Spades': 5,
    # '5 of Hearts': 5,
    # '5 of Clubs': 5,
    # '5 of Diamonds': 5,
    # '6 of Spades': 6,
    # '6 of Hearts': 6,
    # '6 of Clubs': 6,
    # '6 of Diamonds': 6,
    # '7 of Spades': 7,
    # '7 of Hearts': 7,
    # '7 of Clubs': 7,
    # '7 of Diamonds': 7,
    # '8 of Spades': 8,
    # '8 of Hearts': 8,
    # '8 of Clubs': 8,
    # '8 of Diamonds': 8,
    # '9 of Spades': 9,
    # '9 of Hearts': 9,
    # '9 of Clubs': 9,
    # '9 of Diamonds': 9,
    # '10 of Spades': 10,
    # '10 of Hearts': 10,
    # '10 of Clubs': 10,
    # '10 of Diamonds': 10,
    # 'J of Spades': 10,
    # 'J of Hearts': 10,
    # 'J of Clubs': 10,
    # 'J of Diamonds': 10,
    # 'Q of Spades': 10,
    # 'Q of Hearts': 10,
    # 'Q of Clubs': 10,
    # 'Q of Diamonds': 10,
    # 'K of Spades': 10,
    # 'K of Hearts': 10,
    # 'K of Clubs': 10,
    # 'K of Diamonds': 10,
    # 'A of Spades': 11,
    # 'A of Hearts': 11,
    # 'A of Clubs': 11,
    # 'A of Diamonds': 11
    # }
print(deck_dict['A of Diamonds'] + deck_dict['A of Diamonds'])

def stand():
    for i in range(1, len(player_hand):
        x = sum(deck_dict(player_hand)[i])
    return