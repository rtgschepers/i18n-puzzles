TWEET_LIMIT = 140
TWEET_COST = 7
SMS_LIMIT = 160
SMS_COST = 11
DISCOUNT = 13

out = 0
with open('./input.txt', 'r') as file:
    for line in file:
        valid_tweet = False
        valid_sms = False
        line = line.strip()

        if len(line) <= TWEET_LIMIT:
            valid_tweet = True
        if len(line.encode('utf-8')) <= SMS_LIMIT:
            valid_sms = True

        if valid_tweet and valid_sms:
            out += DISCOUNT
        elif valid_tweet:
            out += TWEET_COST
        elif valid_sms:
            out += SMS_COST
print(out)
