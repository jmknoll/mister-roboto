import twitter
import yaml

# get config from yml
with open("/home/mister-roboto/config.yaml", 'r') as stream:
    try:
        config = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)

# authenticate against twitter api
api = twitter.Api(consumer_key=config["CONSUMER_KEY"],
                  consumer_secret=config["CONSUMER_SECRET"],
                  access_token_key=config["ACCESS_TOKEN"],
                  access_token_secret=config["ACCESS_TOKEN_SECRET"])

# favorites and rewteets - topic 1
results = api.GetSearch(
    raw_query="q=scholarship&count=2")

for r in results:
  api.CreateFavorite(r)

results = api.GetSearch(
  raw_query="q=scholarship&count=1")

for r in results:
  api.PostRetweet(r.id)

# favorites and retweets - topic 2
results = api.GetSearch(
    raw_query="q=college&count=2")

for r in results:
  api.CreateFavorite(r)

results = api.GetSearch(
  raw_query="q=university&count=1")

for r in results:
  api.PostRetweet(r.id)
