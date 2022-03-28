import datetime

from Classes import Wizards, WizardsSlogans, ShortStory, Session
import psycopg2


def initialize_db():
    with Session() as session:
        print("Starting filling the database with initial values(wizards, slogans, stories).")
        session.add(Wizards(id=1, name='Harry Potter', side='white', birthday=datetime.date(1994, 7, 13), is_alive=True, power=8))
        session.add(Wizards(id=2, name='Albus Dumbledore', side='white', birthday=datetime.date(1345, 8, 25), is_alive=True,power=10))
        session.add(Wizards(id=3, name='Neville Longbottom', side='white', birthday=datetime.date(1993, 4, 17), is_alive=True,power=3))
        session.add(Wizards(id=4, name='Malfoy Slizerin', side='dark', birthday=datetime.date(1995, 8, 21), is_alive=True, power=5))
        session.add(Wizards(id=5, name='Tom Riddle', side='dark', birthday=datetime.date(1973, 11, 13), is_alive=True, power=8))
        session.add(Wizards(id=6, name='Volan De Mort', side='dark', birthday=datetime.date(1973, 11, 13), is_alive=True, power=10))

        session.add(WizardsSlogans(hero_id=1, moto_id=1, moto='I\'m Harry Potter!!!'))
        session.add(WizardsSlogans(hero_id=2, moto_id=1, moto='Your brain is your everything. Use it.'))
        session.add(WizardsSlogans(hero_id=3, moto_id=1, moto='Why I\'m always in awkward situation?'))
        session.add(WizardsSlogans(hero_id=4, moto_id=1, moto='Hey, Potter, you\'re stinky!'))
        session.add(WizardsSlogans(hero_id=5, moto_id=1, moto='I can make you cry.'))
        session.add(WizardsSlogans(hero_id=6, moto_id=1, moto='Die everyone!!!'))
        session.add(WizardsSlogans(hero_id=6, moto_id=2, moto='I\'ll kill you!!!'))
        session.add(WizardsSlogans(hero_id=6, moto_id=3, moto='Avada kedavra!!!'))
        session.add(WizardsSlogans(hero_id=1, moto_id=2, moto='My friends always support me.'))
        session.add(WizardsSlogans(hero_id=2, moto_id=2, moto='More books you read - more power you have!'))

        session.add(ShortStory(hero_id=1, story='Was born in London in 1994'))
        session.add(ShortStory(hero_id=2, story='The greatest wizard in the universal. Has infamous brother, Max'))
        session.add(ShortStory(hero_id=3, story='Always puts his foot in a trouble. Sometime he can make great things.'))
        session.add(ShortStory(hero_id=4, story='Bad guy from Slizerin, hates Harry Potter'))
        session.add(ShortStory(hero_id=5, story='Young Volan De Mort. Nobody knew who he will become.'))
        session.add(ShortStory(hero_id=6, story='A bad genius, which threatens all the world.'))

        session.commit()
        print("Finished filling the database with initial values(wizards, slogans, stories).")


def print_db_statistics():
    with Session() as session:
        wizards = session.query(Wizards).all()
        print(f'There are {len(wizards)} wizards in the database.')
        for hero in wizards:
            print(f'Wizard {hero.name} story is {hero.short_story}.')
            print(f'The wizard has {len(hero.wizards_slogans)} slogans:')
            print(hero.wizards_slogans)
