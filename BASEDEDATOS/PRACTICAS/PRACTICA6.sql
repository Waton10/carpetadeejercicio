use NORTHWND
go

/*
Ejercicio 1:
o CTE para calcular el total de ventas por categoría
*/

IF OBJECT_ID('tempdb..#VentasPorCategoria') IS NOT NULL
BEGIN
    DROP TABLE #VentasPorCategoria;
END

DECLARE @FechaReferencia DATE = '1998-05-31';

WITH VentasPorProducto AS (
    SELECT
        P.ProductID,
        P.ProductName,
        C.CategoryID,
        C.CategoryName,
        SUM(OD.Quantity * OD.UnitPrice) AS TotalSales
    FROM
        Products P
        JOIN [Order Details] OD ON P.ProductID = OD.ProductID
        JOIN Orders O ON OD.OrderID = O.OrderID
        JOIN Categories C ON P.CategoryID = C.CategoryID
    WHERE
        O.OrderDate >= DATEADD(MONTH, -1, @FechaReferencia)
        AND O.OrderDate <= @FechaReferencia
    GROUP BY
        P.ProductID, P.ProductName, C.CategoryID, C.CategoryName
)

SELECT
    CategoryID,
    CategoryName,
    SUM(TotalSales) AS TotalSalesPorCategoria
INTO #VentasPorCategoria
FROM
    VentasPorProducto
GROUP BY
    CategoryID, CategoryName;

-- Seleccionar los 5 mejores categorías por ventas
SELECT TOP 5 *
FROM #VentasPorCategoria
ORDER BY TotalSalesPorCategoria DESC;

----------------------------------------------------------------------------------------------------------------
/*
• Ejercicio 2:
o CTE para calcular el total de ventas por categoría
*/

IF OBJECT_ID('tempdb..##ClientesActivos') IS NOT NULL
BEGIN
    DROP TABLE ##ClientesActivos;
END

-- Encontrar la fecha más reciente en la base de datos
DECLARE @UltimaFecha DATE = (SELECT MAX(OrderDate) FROM Orders);

WITH VentasPorCategoria AS (
    SELECT
        C.CustomerID,
        C.CompanyName,
        CA.CategoryID,
        CA.CategoryName,
        SUM(OD.Quantity * OD.UnitPrice) AS TotalSales
    FROM
        Customers C
        JOIN Orders O ON C.CustomerID = O.CustomerID
        JOIN [Order Details] OD ON O.OrderID = OD.OrderID
        JOIN Products P ON OD.ProductID = P.ProductID
        JOIN Categories CA ON P.CategoryID = CA.CategoryID
    WHERE
        O.OrderDate >= DATEADD(YEAR, -1, @UltimaFecha)
    GROUP BY
        C.CustomerID, C.CompanyName, CA.CategoryID, CA.CategoryName
)

SELECT
    CustomerID,
    CompanyName,
    COUNT(DISTINCT O.OrderID) AS NumberOfOrders,
    SUM(TotalSales) AS TotalPurchases,
    MAX(O.OrderDate) AS LastPurchase
INTO ##ClientesActivos
FROM
    Customers C
    JOIN Orders O ON C.CustomerID = O.CustomerID
    JOIN VentasPorCategoria VPC ON C.CustomerID = VPC.CustomerID
GROUP BY
    C.CustomerID, C.CompanyName
HAVING
    COUNT(DISTINCT O.OrderID) > 5; -- Consideramos activos a los que tienen más de 5 órdenes

-- Ejemplo de uso
SELECT *
FROM ##ClientesActivos
WHERE TotalPurchases > (SELECT AVG(TotalPurchases) FROM ##ClientesActivos)
ORDER BY TotalPurchases DESC;

--------------------------------------------------------------------------------------------------------
/*
• Ejercicio 3:
o CTE recursiva para mostrar la jerarquía de empleados
*/
IF OBJECT_ID('tempdb..##ClientesActivos') IS NOT NULL
BEGIN
    DROP TABLE ##ClientesActivos;
END

-- Encontrar la fecha más reciente en la base de datos
DECLARE @UltimaFecha DATE = (SELECT MAX(OrderDate) FROM Orders);

WITH VentasPorCategoria AS (
    SELECT
        C.CustomerID,
        C.CompanyName,
        SUM(OD.Quantity * OD.UnitPrice) AS TotalSales,
        COUNT(DISTINCT O.OrderID) AS NumberOfOrders,
        MAX(O.OrderDate) AS LastPurchase
    FROM
        Customers C
        JOIN Orders O ON C.CustomerID = O.CustomerID
        JOIN [Order Details] OD ON O.OrderID = OD.OrderID
        JOIN Products P ON OD.ProductID = P.ProductID
        JOIN Categories CA ON P.CategoryID = CA.CategoryID
    WHERE
        O.OrderDate >= DATEADD(YEAR, -1, @UltimaFecha)
    GROUP BY
        C.CustomerID, C.CompanyName
)

-- Insertar los clientes activos en una tabla temporal
SELECT
    CustomerID,
    CompanyName,
    NumberOfOrders,
    TotalSales AS TotalPurchases,
    LastPurchase
INTO ##ClientesActivos
FROM
    VentasPorCategoria
WHERE
    NumberOfOrders > 5; -- Consideramos activos a los que tienen más de 5 órdenes

-- Ejemplo de uso: seleccionar clientes con compras superiores al promedio
SELECT *
FROM ##ClientesActivos
WHERE TotalPurchases > (SELECT AVG(TotalPurchases) FROM ##ClientesActivos)
ORDER BY TotalPurchases DESC;

-------------------------------------------------------------------------------------------------------------------------------------
/*
• Ejercicio 4:
o CTE con columnas de salida explícitamente definidas para calcular las ventas
totales por empleado
*/

IF OBJECT_ID('tempdb..#VentasPorEmpleado') IS NOT NULL
BEGIN
    DROP TABLE #VentasPorEmpleado;
END

-- CTE para calcular las ventas por empleado
WITH VentasPorEmpleado AS (
    SELECT
        E.EmployeeID,
        E.FirstName + ' ' + E.LastName AS EmployeeName,
        COALESCE(SUM(OD.Quantity * OD.UnitPrice), 0) AS TotalSales -- Aseguramos que TotalSales no sea NULL
    FROM
        Employees E
        LEFT JOIN Orders O ON E.EmployeeID = O.EmployeeID
        LEFT JOIN [Order Details] OD ON O.OrderID = OD.OrderID
    GROUP BY
        E.EmployeeID, E.FirstName, E.LastName
)

-- Insertar los resultados en una tabla temporal
SELECT
    EmployeeID,
    EmployeeName,
    TotalSales
INTO #VentasPorEmpleado
FROM
    VentasPorEmpleado;

-- Seleccionar las ventas totales por empleado ordenadas de mayor a menor
SELECT *
FROM #VentasPorEmpleado
ORDER BY TotalSales DESC;