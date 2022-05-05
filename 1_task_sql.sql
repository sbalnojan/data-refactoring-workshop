SELECT (SELECT SUM(AA.facevalue) FROM (SELECT clients.client_id, clients.name, trades.facevalue FROM clients
INNER JOIN trades
ON clients.client_id=trades.client_id AND
(clients.name LIKE '%Green%' OR clients.name LIKE '%Purple%')) AA) * 100 / 
(SELECT SUM(facevalue) FROM trades) AS Frac
