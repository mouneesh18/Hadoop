CREATE KEYSPACE IF NOT EXISTS sparkify
WITH REPLICATION = {
'class':'SimpleStrategy',
'replication_factor':1
};

USE sparkify;
