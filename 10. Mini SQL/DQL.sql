-- DQL
-- SELECT CompanyName as "Назва компанії", City as Місто
-- from Customers;

--  з табиличи Orders (ID, data shiping, city shipped)

-- select LastName, FirstName, City
-- from Employees
-- where Country = "USA";

-- select ContactName, City
-- from Customers
-- where City="Berlin" or City="London";

-- select ContactName, City
-- from Customers
-- where Country in ("Germany", "Spain", "Italy");

-- select ProductName, UnitPrice
-- from Products
-- where UnitPrice >= 10 and UnitPrice <=20;

-- select ProductName, UnitPrice
-- from Products
-- where UnitPrice between 10 and 20;


-- select ProductName, UnitPrice, UnitsInStock
-- from Products
-- where ProductName like "ch%";

-- select count(*) as TotalCustomers
-- from Customers;

-- select OrderId,  sum(UnitPrice * Quantity) as "Order Sum"
-- from "Order Details"
-- group by OrderID
-- having "Order Sum" <= 1000;

-- AVG() - average середнє
-- ax() - 

-- Знайти країни, в яких кількість клієнтів >= 5
-- select country, max(CustomerCountByCountry)
-- from (
-- 	select Country, count(*) as CustomerCountByCountry
-- 	from Customers
-- 	Group by Country
-- )

-- select ProductName, CategoryName
-- from Products as P
-- left join Categories as C on P.CategoryID = C.CategoryID


-- select C.CustomerID, C.ContactName, sum(OD.UnitPrice * OD.Quantity * (1 - OD.Discount)) as TotalCustomerSum
-- from Customers as C
-- left join Orders as O On C.CustomerID = O.CustomerID
-- inner join "Order Details" as OD on O.OrderId = OD.OrderID
-- group by C.CustomerID;



