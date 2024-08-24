from IPython.core.magic import (register_line_magic,
                                register_cell_magic)
import redis as redis_db

# Connect to the Redis server
r = redis_db.Redis(host='localhost', port=6379, db=0)

def query_redis_output_text(redis_query: str):
    value = r.execute_command(redis_query)
    print(redis_query)
    print(value)
    print()
    return value

def redis(line, cell_content):
    
    # %redis table
    # if line == 'table': ...
    lines = cell_content.splitlines()
    
    for line in lines:
        # Process each line (here we just print it)
        stripped_line = line.strip()
        # Skip empty lines
        if stripped_line:        
            query_redis_output_text(stripped_line)

        

def load_ipython_extension(ipython):

    ipython.register_magic_function(redis, 'cell')
    