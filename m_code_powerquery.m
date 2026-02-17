let
    Source = Csv.Document(File.Contents("data/project_tasks.csv"),[Delimiter=",", Encoding=1252]),
    #"Promoted Headers" = Table.PromoteHeaders(Source),
    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{{"StartDate", type date}, {"EndDate", type date}, {"Duration", Int64.Type}, {"PercentComplete", type number}}),
    #"Added DurationBar" = Table.AddColumn(#"Changed Type", "GanttBar", each Text.Repeat("█", [Duration]), type text),
    #"Added RiskScore" = Table.AddColumn(#"Added DurationBar", "RiskScore", each if [PercentComplete] < 20 and [Duration] > 15 then "High" else "Low", type text)
in
    #"Added RiskScore"
