# "list keys in your redis server"

KEYS *
KEYS demo.*

# "there is no command to create a key. Keys are created when key-value pairs are set."

SET chave valor


SET mykey value
SET foo bar
SET demo.redis.cli.keys 12999030039



# Caching values

SET user.5.username matheusmota
SET user.5.session iojiu2543tin2oi35tnIALWEMD23242

SET user.6.username fulanosilva
SET user.6.session iojhasjOIJASmnnOAIJSD

SET user.9.username jotap
SET user.9.session KJASKJDH8as7KASDLKnakjsndAKD


# "confirm the existence of a key"
EXISTS user.5
EXISTS user.5.*
EXISTS user.5.username



GET *
KEYS user.*
KEYS user.5.*
GET user.9.session 


# "check the TTL of a key"
# "in seconds"
TTL user.9.session          
"# in milliseconds"
PTTL user.9.session         


# "set the TTL of a key"

# in seconds:
EXPIRE user.9.session 20				
# in milliseconds:
PEXPIRE user.9.session 3600000			



# "delete a key" 

DEL user.5.session
DEL user.5.username

KEYS user.5.*
GET user.5.session 


# "there are other types"

# "SET"
SADD myset "Hello"
SADD myset "World"
SADD myset "World"
SMEMBERS myset

# "HASH"
HSET myhash field1 "Valor 1"
HSET myhash campo2 "Value 2"
HGETALL myhash
HGET myhash field1

HSET user.3.movies movieId 3 title "Lion Redemption" genres "Comedy|Adventure" year 1998
HGETALL user.3.movies 
HGET user.3.movies title


# "check the type of the value held by a key"

TYPE user.6.session 
TYPE myhash
TYPE user.3.movies

# "Official command reference: https://redis.io/commands#generic"