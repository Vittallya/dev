INSERT INTO Category (Id, Name) VALUES
                                (1, 'Лампа накаливания'),
                                (2, 'Люминисцентная');

INSERT INTO Tovars (Id, Name, cost, categoryid) VALUES
                                (1, 'Лампочка 1', 120, 1),
                                (2, 'Лампочка 2', 220, 2);

INSERT INTO UserAcc (UUID, Login, PasswordHash) VALUES
                                ('5b819f8005874871bca276df4481937e', 'Admin', 'pbkdf2:sha256:260000$lCb0UO3E58tawCPN$ceabe16c39e94be646e2020dc83d6e7f10215e5a21736152ab502049b8bbd1f2');

