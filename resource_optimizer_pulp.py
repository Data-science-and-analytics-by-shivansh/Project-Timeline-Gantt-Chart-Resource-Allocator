import pandas as pd
from pulp import *

df = pd.read_csv('data/project_tasks.csv')
df['StartDate'] = pd.to_datetime(df['StartDate'])

# Simplified RCPSP - minimize makespan with resource constraint
prob = LpProblem("Resource_Leveling", LpMinimize)
max_day = df['EndDate'].max()  # placeholder

# Variables: new start day for each task
start_vars = {row.TaskID: LpVariable(f"start_{row.TaskID}", lowBound=0, cat='Integer') for _, row in df.iterrows()}

# Objective: minimize project end date
prob += lpSum(start_vars.values())  # can be improved

# Constraints: duration, predecessors, resource per day <= availability
# (full version in repo has 200+ lines with daily resource matrix)

prob.solve(PULP_CBC_CMD(msg=0))
print("Optimized project duration reduced by", "... days")
