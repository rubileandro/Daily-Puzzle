"""
Branson and his sister Beatrice combined their allowance of $7 each, so they could buy a movie for $12. 
They bought $1 containers of fruit salad with the remaining money and split the containers evenly between
them. How many containers of salad did they each get?
"""

combined_allowance = 2 * 7
cost_of_movie = 12
cost_of_cont = 1 


containers_each = ((combined_allowance - cost_of_movie) / cost_of_cont) / 2
print(f"Branson and Beatrice, each got {containers_each} container.")
