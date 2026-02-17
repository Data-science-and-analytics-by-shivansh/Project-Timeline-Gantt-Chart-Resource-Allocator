CREATE TABLE ProjectTasks (
    TaskID VARCHAR(20) PRIMARY KEY,
    TaskName VARCHAR(255),
    StartDate DATE,
    EndDate DATE,
    Duration INT,
    PercentComplete DECIMAL(5,2),
    AssignedResource VARCHAR(100),
    MaxAvailability INT,
    Cost DECIMAL(12,2),
    Milestone VARCHAR(5),
    Predecessors VARCHAR(100),
    Status VARCHAR(50)
);
-- Import CSV via BULK INSERT or tool
