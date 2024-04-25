
SELECT MachineID, AVG(ProductionRate) as AverageProduction, SUM(Downtime) as TotalDowntimeHours
FROM MachineProductionData
WHERE Timestamp >= DATEADD(day, -7, GETDATE())
GROUP BY MachineID
ORDER BY TotalDowntimeHours DESC;
