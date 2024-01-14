DROP TABLE IF EXISTS transaction;
DROP TABLE IF EXISTS product_nomenclature;

CREATE TABLE transaction (
    dt DATE, -- date à laquelle la commande a été passée
    order_id BIGINT, -- identifiant unique de la commandetransaction
    client_id BIGINT, -- identifiant unique du client
    prod_id BIGINT, -- identifiant unique du produit acheté
    prod_price DECIMAL, -- prix unitaire du produit
    prod_qty INT-- quantité de produit achetée
);

INSERT INTO transaction (dt, order_id, client_id, prod_id, prod_price, prod_qty)
VALUES
    ('01/01/20', 1234, 999, 490756, 50, 1),
    ('01/01/20', 1234, 999, 389728, 3.56, 4),
    ('01/01/20', 3456, 845, 490756, 50, 2),
    ('01/01/20', 3456, 845, 549380, 300, 1),
    ('01/01/20', 3456, 845, 293718, 10, 6),
    ('02/01/20', 3456, 845, 293718, 10, 6),
    ('02/01/19', 3456, 845, 293718, 10, 6);


CREATE TABLE product_nomenclature (
    product_id BIGINT, -- identifiant unique du produit
    product_type TEXT, -- type de produit (DECO ou MEUBLE)
    product_name TEXT -- le nom du produit Echantillon de la table PRODUCT_NOMENCLA
);

INSERT INTO product_nomenclature (product_id, product_type, product_name)
VALUES
    (490756, 'MEUBLE', 'Chaise'),
    (389728, 'DECO', 'Boule de Noël'),
    (549380, 'MEUBLE', 'Canapé'),
    (293718, 'DECO', 'Mug');