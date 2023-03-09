SELECT tb1.invoice_id,
    tb1.branch,
    tb1.city,
    tb1.customer_type,
    tb1.gender,
    tb1.product_line,
    tb1.unit_price,
    tb2.date,
    tb2.time,
    tb2.payment,
    tb2.quantity,
    tb2.tax_5_percent,
    tb2.total,
    tb3.cogs,
    tb3.gross_income,
    tb3.gross_margin_percentage,
    tb3.rating FROM
    table1 AS tb1
        INNER JOIN
    table2 AS tb2 ON tb1.invoice_id = tb2.invoice_id
        INNER JOIN
    table3 AS tb3 ON tb2.invoice_id = tb3.invoice_id;