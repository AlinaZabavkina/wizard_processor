# Harry Potter Universal Wizards Clashes
Program which holds wizards in SQL DB and organizes clashes between them
### Main features
- add wizards
- delete wizards
- add wizards slogans
- add wizards short stories
- simulates battle between a wizard from dark side and wizard from white side. If a wizard loses a battle, he dies (is_alive attribute becomes false)
### ToDo
- deploy somewhere for others to test
- add wizards, their slogans and short stories
```Linux Kernel Module
python processor.py --function='add_wizard' --name='Harry Potter' --side='white' --birthday='1911-01-12' --is_alive=True --power=10
```

```Linux Kernel Module
python processor.py --function='add_slogan' --name='Hermione' --slogan='Your knowledge is your power'
```

```Linux Kernel Module
python processor.py --function='add_story' --name='Hermione' --story='Minister Hermione Jean Granger (b. 19 September, 1979) was an English Muggle-born witch born to Mr and Mrs Granger. At the age of eleven, she learned about her magical nature and was accepted into Hogwarts School of Witchcraft and Wizardry. Hermione began attending Hogwarts in 1991 and was Sorted into Gryffindor House.' 
```
- conduct battles between a wizard from dark side and wizard from white side
```Linux Kernel Module
python processor.py --function='add_fight'
```
-delete wizards
```Linux Kernel Module
python processor.py --function='delete_wizard' --name='Hermione' 
```



### development: docker
To deploy - from the root folder:
```Linux Kernel Module
docker-compose up -d --build
```
On develop environment database is recreated each time docker is started. 

To switch containers off:
```Linux Kernel Module
docker-compose down -v
```
### production: docker
To deploy - from the root folder:
```Linux Kernel Module
docker-compose -f docker-compose.prod.yaml up -d --build
```
To fill the database with initial tables & values:
```Linux Kernel Module
docker-compose -f docker-compose.prod.yaml exec web python db_initializer.py initialize_db
```
To switch containers off:
```Linux Kernel Module
docker-compose -f docker-compose.prod.yaml down -v