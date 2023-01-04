DECLARE @data_ref DATE;
SET @data_ref = '2022/12/01'
SELECT DATEADD(month,-1,DATEADD(year,-1,@data_ref))

--FECHADO
SELECT TOP 10 * FROM selloutmensal_trade
WHERE DATA = DATEADD(month,-1,@data_ref)
AND BANDEIRA IN ['MAGAZINE LUIZA','MAGAZINE LUIZA.COM']

--MES ATUAL ANO ANTERIOR
--SELECT TOP 10 * FROM selloutmensal_trade
--WHERE DATA = DATEADD(year,-1,@data_ref)

--M�S/ ANO ANTERIOR 
--SELECT TOP 10 * FROM selloutmensal_trade
--WHERE DATA = DATEADD(month,-1,DATEADD(year,-1,@data_ref))

--PROJE��O M1
SELECT TOP 10 * FROM selloutmensal_trade
WHERE DATA = DATEADD(month,1,@data_ref) 
