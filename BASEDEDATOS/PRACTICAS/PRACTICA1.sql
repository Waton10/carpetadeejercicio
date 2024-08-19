/*Ejercicio 1: Stored Procedure - Actualización de descuentos
o Crea un stored procedure llamado sp_ActualizarDescuentos que simule una
actualización de descuentos de los productos basándose en su stock y ventas
recientes*/

CREATE PROCEDURE sp_ActualizarDescuentos
AS
BEGIN
    UPDATE Products
    SET Discount = Discount + 0.05
    WHERE ProductID IN (
        SELECT P.ProductID
        FROM Products P
        JOIN OrderDetails OD ON P.ProductID = OD.ProductID
        JOIN Orders O ON OD.OrderID = O.OrderID
        WHERE P.UnitsInStock < 20 
          AND O.OrderDate >= DATEADD(MONTH, -1, GETDATE()) 
        GROUP BY P.ProductID
        HAVING SUM(OD.Quantity) > 100 
    );
    UPDATE Products
    SET Discount = Discount - 0.05
    WHERE ProductID IN (
        SELECT P.ProductID
        FROM Products P
        LEFT JOIN OrderDetails OD ON P.ProductID = OD.ProductID
        LEFT JOIN Orders O ON OD.OrderID = O.OrderID
        WHERE P.UnitsInStock > 100 
          AND (O.OrderDate IS NULL OR O.OrderDate < DATEADD(MONTH, -1, GETDATE())) 
        GROUP BY P.ProductID
        HAVING SUM(OD.Quantity) < 20 
    );
    UPDATE Products
    SET Discount = CASE
        WHEN Discount < 0 THEN 0
        WHEN Discount > 0.5 THEN 0.5
        ELSE Discount
    END;
END;

/*esto es para ejecutar el proceso almacenado*/

EXEC sp_ActualizarDescuentos;
-------------------------------------------------------------------------------------------------------------------------------------
/*Ejercicio 2: Stored Procedure - Reporte de ventas por categoría
o Crea un stored procedure llamado sp_ReporteVentasPorCategoria que simule un
generador de un reporte de ventas por categoría de producto.*/

CREATE PROCEDURE sp_ReporteVentasPorCategoria
AS
BEGIN
    SELECT 
        C.CategoryName AS Categoria,
        SUM(OD.Quantity * OD.UnitPrice) AS TotalVentas
    FROM 
        Categories C
    JOIN 
        Products P ON C.CategoryID = P.CategoryID
    JOIN 
        OrderDetails OD ON P.ProductID = OD.ProductID
    GROUP BY 
        C.CategoryName
    ORDER BY 
        TotalVentas DESC;
END;

/*para ejecutar el proceso almacenado*/

EXEC sp_ReporteVentasPorCategoria;

-----------------------------------------------------------------------------------------------------------------------------------
/*Ejercicio 3: Trigger - Actualización de inventario
o Crea un trigger llamado tr_ActualizarInventario que se active después de insertar
un nuevo pedido en la tabla Orders.*/

CREATE TRIGGER tr_ActualizarInventario
ON Orders
AFTER INSERT
AS
BEGIN
    UPDATE P
    SET P.UnitsInStock = P.UnitsInStock - OD.Quantity
    FROM Products P
    JOIN OrderDetails OD ON P.ProductID = OD.ProductID
    JOIN Inserted I ON I.OrderID = OD.OrderID;
    UPDATE P
    SET P.UnitsInStock = 0
    WHERE P.UnitsInStock < 0;
END;

-- Ejemplo de inserción en Orders
INSERT INTO Orders (CustomerID, EmployeeID, OrderDate, ShipCountry)
VALUES ('ALFKI', 1, GETDATE(), 'Germany');

-- Insertar detalles del pedido correspondiente
INSERT INTO OrderDetails (OrderID, ProductID, Quantity, UnitPrice)
VALUES (SCOPE_IDENTITY(), 1, 10, 20.00);  -- SCOPE_IDENTITY() devuelve el último OrderID insertado
---------------------------------------------------------------------------------------------------------------------------------------
/*Ejercicio 4: Trigger - Control de precios
o Crea un trigger llamado tr_ControlPrecios que se active antes de actualizar los
precios en la tabla Products.*/

CREATE TRIGGER tr_ControlPrecios
ON Products
INSTEAD OF UPDATE
AS
BEGIN
    -- Verificar que los precios no se reduzcan o incrementen de manera drástica
    DECLARE @NuevoPrecio DECIMAL(10, 2), @PrecioAnterior DECIMAL(10, 2), @ProductID INT;

    SELECT @NuevoPrecio = i.UnitPrice, @PrecioAnterior = d.UnitPrice, @ProductID = i.ProductID
    FROM Inserted i
    JOIN Deleted d ON i.ProductID = d.ProductID;

    -- Verificar que el nuevo precio no sea menor a la mitad o mayor al doble del precio anterior
    IF @NuevoPrecio < @PrecioAnterior * 0.5 OR @NuevoPrecio > @PrecioAnterior * 2
    BEGIN
        RAISERROR ('El cambio de precio es demasiado drástico.', 16, 1);
        ROLLBACK TRANSACTION;
        RETURN;
    END

    -- Realizar la actualización si pasa las validaciones
    UPDATE Products
    SET UnitPrice = @NuevoPrecio
    WHERE ProductID = @ProductID;
END;

/*Ejemplo de inserción en la tabla de auditoría (opcional):
Si deseas llevar un registro de los cambios, puedes agregar este bloque de código dentro del trigger:*/
-- Suponiendo que tienes una tabla de auditoría como esta:
CREATE TABLE PriceAudit (
    ProductID INT,
    OldPrice DECIMAL(10, 2),
    NewPrice DECIMAL(10, 2),
    ChangeDate DATETIME,
    ChangedBy NVARCHAR(100)
);

INSERT INTO PriceAudit (ProductID, OldPrice, NewPrice, ChangeDate, ChangedBy)
VALUES (@ProductID, @PrecioAnterior, @NuevoPrecio, GETDATE(), SYSTEM_USER);

/*Verificación:
Para probar este trigger, intenta actualizar el precio de un producto en la tabla Products y verifica que:

Se impida cualquier cambio de precio que sea demasiado drástico.
Se permita la actualización si el cambio es razonable.*/

-- Ejemplo de actualización que debería pasar la validación
UPDATE Products
SET UnitPrice = UnitPrice * 1.1
WHERE ProductID = 1;

-- Ejemplo de actualización que debería fallar
UPDATE Products
SET UnitPrice = UnitPrice * 3 -- Esto debería fallar si el precio nuevo es más del doble
WHERE ProductID = 1;

