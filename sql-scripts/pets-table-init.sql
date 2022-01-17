CREATE TABLE PETS(
    id INT NOT NULL IDENTITY(1, 1),
    name VARCHAR(75) NOT NULL,
    type VARCHAR(75) NOT NULL,
	description VARCHAR(800) NOT NULL,
    image_path VARCHAR(100) NULL,
	PRIMARY KEY (id)
);

INSERT INTO dbo.PETS (name, type, description)
VALUES (
    'Wolfe',
    'dog',
    'She was a good dogo.'
);

INSERT INTO dbo.PETS (name, type, description)
VALUES (
    'Marty',
    'cat',
    'I miss you sweetie.'
);

INSERT INTO dbo.PETS (name, type, description)
VALUES (
    'Spectre',
    'cat',
    'Hims is a long boi.'
);