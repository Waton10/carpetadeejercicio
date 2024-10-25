USE NORTHWND
GO

/*EJERCICIO 1*/
SELECT TOP 10
    o.OrderID, 
    c.CompanyName,
    p.ProductName,
    od.Quantity,
    od.UnitPrice,
    (od.Quantity * od.UnitPrice) AS TotalAmount
FROM Orders o
INNER JOIN Customers c ON o.CustomerID = c.CustomerID
INNER JOIN [Order Details] od ON o.OrderID = od.OrderID
INNER JOIN Products p ON od.ProductID = p.ProductID
WHERE YEAR(o.OrderDate) = 1997
ORDER BY TotalAmount DESC;

/*EJERCICIO */
SELECT 
    c.CategoryName,
    p.ProductName,
    ISNULL(SUM(od.Quantity), 0) AS TotalQuantitySold
FROM Categories c
LEFT JOIN Products p ON c.CategoryID = p.CategoryID
LEFT JOIN [Order Details] od ON p.ProductID = od.ProductID
GROUP BY c.CategoryName, p.ProductName
ORDER BY c.CategoryName, TotalQuantitySold DESC;

/*EJERCICIO 3*/
SELECT 
    e.FirstName + ' ' + e.LastName AS EmployeeName,
    r.RegionDescription,
    COUNT(DISTINCT o.OrderID) AS NumberOfOrders
FROM Orders o
RIGHT JOIN Employees e ON o.EmployeeID = e.EmployeeID
LEFT JOIN EmployeeTerritories et ON e.EmployeeID = et.EmployeeID
LEFT JOIN Territories t ON et.TerritoryID = t.TerritoryID
LEFT JOIN Region r ON t.RegionID = r.RegionID
GROUP BY e.EmployeeID, e.FirstName, e.LastName, r.RegionDescription
ORDER BY NumberOfOrders DESC;

/*EJERCICIO 4*/
SELECT 
    e.FirstName + ' ' + e.LastName AS EmployeeName, 
    o.OrderID
FROM Employees e
FULL JOIN Orders o ON e.EmployeeID = o.EmployeeID;