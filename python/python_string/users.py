tweets="What a game , hats off to both teams . Well done @benstokes38 @patcummins30 you have bought test cricket back to life. Love test cricket  @TheBarmyArmy @CricketAus @ECB_cricket"
users=tweets.split()
for t in users:
 if t.startswith("@"):
  print(t)
