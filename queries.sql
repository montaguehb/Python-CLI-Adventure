CREATE TABLE items (
    "id" INTEGER PRIMARY KEY,
    "item_name" TEXT,
    "item_description" TEXT,
    "item_type" TEXT
);

-- .mode csv
-- .import items.csv items