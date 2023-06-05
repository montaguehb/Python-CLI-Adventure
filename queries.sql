CREATE TABLE IF NOT EXISTS rooms (
    "id" INTEGER PRIMARY KEY,
    "item_id" INTEGER,
    "enemy_id" INTEGER,
    "top" BOOLEAN,
    "bottom" BOOLEAN,
    "left" BOOLEAN,
    "right" BOOLEAN,
    FOREIGN KEY ("item_id") REFERENCES items(id)
);

-- .mode csv;
-- .import data.csv rooms;