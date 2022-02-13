DROP DATABASE trellis;
DROP USER trellisuser;
CREATE DATABASE trellis;
CREATE USER trellisuser WITH PASSWORD 'trellis';
GRANT ALL PRIVILEGES ON DATABASE trellis TO trellisuser;
