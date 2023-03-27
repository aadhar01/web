Install SQLite using:
                    sudo apt install sqlite3

When running the sqlite3 into terminal
            run using
            sqlite3 <tablename>
            run commands
            .mode columns (to make the view better)
            .headers yes

SQLite Types:
                Text
                Numeric
                Integer
                Real
                Blob  Binary large object


MySQL:          
                CHAR(size)
                VARCHAR(size)
                SMALLINT
                INT
                BIGINT
                FLOAT
                DOUBLE
                
COSTRAINTS
                CHECK
                DEFAULT
                NOT NULL
                PRIMARY KEY
                UNIQUE

COMMANDS
                CREATE
                INSERT (INSERT INTO <TABLE_NAME>(col1, col2, col3)VALUES(col1_value, col2_values, col3_values);)
                SELECT (SELECT * FROM flights;) 

                FUNCTIONS:
                            AVERAGE
                            COUNT
                            MAX
                            MIN
                            SUM

                UPDATE 
                        example:
                                UPDATE flights
                                SET duration = 420
                                WHERE origin = "New York" 
                                AND destination = "London"
                DELETE

                other clauses:
                                LIMIT
                                ORDER BY
                                GROUP BY 
                                HAVING

                Foreign Key:

                            NORMALISE DATA

                JOIN

                CREATE INDEX

        SQL INJECTION:
                This so that the vulnerabilites do not get exploited


        Race Conditions:
                Multiple things happening simulatneously
                Multiple Thread

                how to do?
                        Lock on the transaction


            
                            



