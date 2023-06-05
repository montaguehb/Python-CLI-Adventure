IF NOT EXISTS CREATE TABLE enemy (
    id INTEGER PRIMARY KEY,
    name TEXT,
    level INT,
    type TEXT,
    mechanics TEXT
);

INSERT INTO enemy (Name, Level, Type, Mechanics)
VALUES
('git lord', 3, 'hard', 'stage, pull, add, commit, push, merge'),
('git ghoul', 2, 'medium', 'add, push'),
('git gremlin', 2, 'medium', 'stash, pull, commit'),
('git ghast', 2, 'medium', 'add, commit, push'),
('git mage', 2, 'medium', 'add, commit'),
('git sorceress', 2, 'medium', 'branch, switch'),
('git sorcerer', 2, 'medium', 'clone, add'),
('git spectre', 2, 'medium', 'branch'),
('git shadow', 2, 'medium', 'stash, pull'),
('git abomination', 2, 'medium', 'branch, show'),
('git revenant', 2, 'medium', 'init, add'),
('git scorpion', 1, 'easy', 'log'),
('git pest', 1, 'easy', 'status'),
('git spirit', 1, 'easy', 'diff'),
('git monster', 1, 'easy', 'branch'),
('git dweller', 1, 'easy', 'switch'),
('git howler', 1, 'easy', 'merge'),
('git serpent', 1, 'easy', 'checkout'),
('git spider', 1, 'easy', 'clone'),
('git lich', 1, 'easy', 'fetch'),
('git wraith', 1, 'easy', 'push'),
('git seeker', 1, 'easy', 'pull'),
('git bat', 1, 'easy', 'remote'),
('git blob', 1, 'easy', 'config'),
('git ghost', 1, 'easy', 'grep'),
('git minion', 1, 'easy', 'show'),
('git grime', 1, 'easy', 'add'),
('git goo', 1, 'easy', 'commit'),
('git slime', 1, 'easy', 'init');
