PREMIER_LEAGUE_TEAMS = ["arsenal","aston villa","bournemouth","brentford","brighton","chelsea",
                        "crystal palace","everton","fulham","leeds united","leicester city","liverpool","manchester city",
                        "manchester united","newcastle","nottingham forest","southampton","tottenham",
                        "west ham","wolverhampton"]

DATABASE_INJECTION = [{'arsenal': {'positive_tweet_count': 331, 'negative_tweet_count': 168, 'tweet_count': 499, 'positive_percentage': 66.3, 'negative_percentage': 33.7}}, 
                        {'aston villa': {'positive_tweet_count': 278, 'negative_tweet_count': 77, 'tweet_count': 355, 'positive_percentage': 78.3, 'negative_percentage': 21.7}}, 
                        {'bournemouth': {'positive_tweet_count': 338, 'negative_tweet_count': 160, 'tweet_count': 498, 'positive_percentage': 67.9, 'negative_percentage': 32.1}}, 
                        {'brentford': {'positive_tweet_count': 159, 'negative_tweet_count': 124, 'tweet_count': 283, 'positive_percentage': 56.2, 'negative_percentage': 43.8}}, 
                        {'brighton': {'positive_tweet_count': 351, 'negative_tweet_count': 148, 'tweet_count': 499, 'positive_percentage': 70.3, 'negative_percentage': 29.7}}, 
                        {'chelsea': {'positive_tweet_count': 353, 'negative_tweet_count': 145, 'tweet_count': 498, 'positive_percentage': 70.9, 'negative_percentage': 29.1}}, 
                        {'crystal palace': {'positive_tweet_count': 241, 'negative_tweet_count': 90, 'tweet_count': 331, 'positive_percentage': 72.8, 'negative_percentage': 27.2}}, 
                        {'everton': {'positive_tweet_count': 431, 'negative_tweet_count': 68, 'tweet_count': 499, 'positive_percentage': 86.4, 'negative_percentage': 13.6}}, 
                        {'fulham': {'positive_tweet_count': 283, 'negative_tweet_count': 97, 'tweet_count': 380, 'positive_percentage': 74.5, 'negative_percentage': 25.5}}, 
                        {'leeds united': {'positive_tweet_count': 347, 'negative_tweet_count': 151, 'tweet_count': 498, 'positive_percentage': 69.7, 'negative_percentage': 30.3}}, 
                        {'leicester city': {'positive_tweet_count': 143, 'negative_tweet_count': 47, 'tweet_count': 190, 'positive_percentage': 75.3, 'negative_percentage': 24.7}}, 
                        {'liverpool': {'positive_tweet_count': 271, 'negative_tweet_count': 229, 'tweet_count': 500, 'positive_percentage': 54.2, 'negative_percentage': 45.8}}, 
                        {'manchester city': {'positive_tweet_count': 373, 'negative_tweet_count': 126, 'tweet_count': 499, 'positive_percentage': 74.7, 'negative_percentage': 25.3}}, 
                        {'manchester united': {'positive_tweet_count': 365, 'negative_tweet_count': 135, 'tweet_count': 500, 'positive_percentage': 73.0, 'negative_percentage': 27.0}}, 
                        {'newcastle': {'positive_tweet_count': 239, 'negative_tweet_count': 259, 'tweet_count': 498, 'positive_percentage': 48.0, 'negative_percentage': 52.0}}, 
                        {'nottingham forest': {'positive_tweet_count': 255, 'negative_tweet_count': 42, 'tweet_count': 297, 'positive_percentage': 85.9, 'negative_percentage': 14.1}}, 
                        {'southampton': {'positive_tweet_count': 269, 'negative_tweet_count': 227, 'tweet_count': 496, 'positive_percentage': 54.2, 'negative_percentage': 45.8}}, 
                        {'tottenham': {'positive_tweet_count': 379, 'negative_tweet_count': 119, 'tweet_count': 498, 'positive_percentage': 76.1, 'negative_percentage': 23.9}}, 
                        {'west ham': {'positive_tweet_count': 351, 'negative_tweet_count': 148, 'tweet_count': 499, 'positive_percentage': 70.3, 'negative_percentage': 29.7}}, 
                        {'wolverhampton': {'positive_tweet_count': 296, 'negative_tweet_count': 125, 'tweet_count': 421, 'positive_percentage': 70.3, 'negative_percentage': 29.7}}]

DATABASE_INJECTION_2 = [('chelsea', 98344), ('arsenal', 76936), 
                        ('liverpool', 67462), ('newcastle', 26826), 
                        ('manchester united', 25233), ('brighton', 19080),
                        ('everton', 16225), ('tottenham', 12820), 
                        ('west ham', 8164), ('southampton', 7505), 
                        ('manchester city', 5337), ('bournemouth', 4622), 
                        ('leeds united', 3831), ('crystal palace', 3449), 
                        ('aston villa', 3408), ('wolverhampton', 3270), 
                        ('fulham', 3238), ('brentford', 2136), 
                        ('nottingham forest', 1489), ('leicester city', 1373)]

def random_injection(data):
    import random

    for sentiment in data:
        for sent in sentiment.values():
            rand_value = random.randint(30,100)
            sent['positive_percentage'] = rand_value

    return data

