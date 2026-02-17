import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)
start_date = datetime(2025, 3, 1)

tasks = []
for i in range(45):
    duration = np.random.randint(3, 25)
    start = start_date + timedelta(days=np.random.randint(0, 60))
    end = start + timedelta(days=duration)
    percent = np.random.randint(0, 101)
    resources = np.random.choice(['Alice', 'Bob', 'Charlie', 'Dana', 'Eve', 'Frank'], p=[0.25,0.2,0.2,0.15,0.1,0.1])
    
    tasks.append({
        'TaskID': f'T{100+i}',
        'TaskName': f'Task {i+1} - {"Development" if i%3==0 else "Testing" if i%3==1 else "Design"}',
        'StartDate': start.date(),
        'EndDate': end.date(),
        'Duration': duration,
        'PercentComplete': percent,
        'AssignedResource': resources,
        'MaxAvailability': 8,
        'Cost': round(np.random.uniform(5000, 45000), 2),
        'Milestone': 'Yes' if i in [5,12,25,38] else 'No',
        'Predecessors': '' if i<3 else f'T{99+i-np.random.randint(1,4)}',
        'Status': 'Delayed' if percent < 30 and (datetime.now().date() - start.date()).days > 10 else 'On Track'
    })

df = pd.DataFrame(tasks)
df.to_csv('data/project_tasks.csv', index=False)
print("Sample dataset created: 45 tasks with resources, dependencies & risks")
