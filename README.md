# ParallelUniverse
- Store the data of universes
- List families in a particular universe
- Check if families with same identifiers have same power in all universes
- Find unbalanced families and balance them

## API Documentation
### Store the data of Person API:   `/person`
```
curl -X POST -d '{"person_id": <personid>, "power": <power>, "universe_id": <universeid>, "family_id": <familyid>}' 
'http://127.0.0.1:5000/person'
```

### Get list of Families in particular Universe API: `/universe/<universe_id>`
```
curl -X GET
'http://127.0.0.1:5000/universe/u1'
```

### Check if families with same identifiers have same power in all universes API: `/balancepower`
```
curl -X GET
'http://127.0.0.1:5000/balancepower'
```

### Find unbalanced families and balance them API: `/balancepower`
```
curl -X POST
'http://127.0.0.1:5000/balancepower'
```

 ## Tech Stack Used:-
  - Flask
  - MySql
 
 ## Data Model:
 - Table : person

| Field          | Type          | Null | Key | Default | Extra |
|----------------|---------------|------|-----|---------|-------|
| person_id     | varchar(100)   | NO   | PRI | NULL    |       |
| power         | Integer        | NO   |     | NULL    |       |
| universe_id   | varchar(100)   | NO   |     | NULL    |       |
| family_id     | varchar(100)   | NO   |     | NULL    |       |

- Table : family

| Field      | Type        | Null | Key | Default | Extra          |
|------------|-------------|------|-----|---------|----------------|
| family_id  | varchar(100)| NO   | PRI | NULL    |                |


- Table : universe

| Field      | Type        | Null | Key | Default | Extra          |
|------------|-------------|------|-----|---------|----------------|
| universe_id| varchar(100)| NO   | PRI | NULL    |                |            
