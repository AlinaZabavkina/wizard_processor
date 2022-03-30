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
python application/FunctionProcessor.py --function='add_wizard' --name='Harry Potter' --side='white' --birthday='1911-01-12' --is_alive=True --power=10
```

```Linux Kernel Module
python application/FunctionProcessor.py --function='add_slogan' --name='Hermione' --slogan='Your knowledge is your power'
```

```Linux Kernel Module
python application/FunctionProcessor.py --function='add_story' --name='Hermione' --story='Minister Hermione Jean Granger (b. 19 September, 1979) was an English Muggle-born witch born to Mr and Mrs Granger. At the age of eleven, she learned about her magical nature and was accepted into Hogwarts School of Witchcraft and Wizardry. Hermione began attending Hogwarts in 1991 and was Sorted into Gryffindor House.' 
```
- conduct battles between a wizard from dark side and wizard from white side
```Linux Kernel Module
python application/FunctionProcessor.py --function='add_fight'
```
- delete wizards. When wizard is deleted, his slogans and short story is deleted as well. In clashes table hero_id becomes null.
```Linux Kernel Module
python application/FunctionProcessor.py --function='delete_wizard' --name='Hermione' 
```



### development: docker
To deploy - from the root folder:
```Linux Kernel Module
docker-compose up -d --build
```
On develop environment the database is recreated each time docker is started and is filled with predefined values on the start.

To switch containers off:
```Linux Kernel Module
docker-compose down -v
```
### production: docker
To deploy - from the root folder:
```Linux Kernel Module
docker-compose -f docker-compose-prod.yaml up -d --build
```
To fill the database with initial tables & values:
```Linux Kernel Module
python application/FunctionProcessor.py --function='fill_database'
```

To switch containers off:
```Linux Kernel Module
docker-compose -f docker-compose-prod.yaml down -v
```

Ways to improve:
```Linux Kernel Module
1) Initial db filling doesn't work perfect since there are some hardcoded ids, I would rework it if I had time
2) I would develop some better interface for functions
3) Now a wizard with more power wins a battle, it'd be better if there is some random chance least powered wizard to win
```

The programm was tested on Docker version 20.10.8, build 3967b7d on MacOS 12.0.1 (21A559)
