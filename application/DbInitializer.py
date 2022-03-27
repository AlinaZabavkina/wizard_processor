import datetime

from Classes import Wizards, WizardsSlogans, ShortStory, Session


def initialize_db():
    with Session() as session:
        print("Starting filling the database with initial values(wizards, slogans, stories).")
        session.add(Wizards(name='Harry Potter', side='white', birthday=datetime.date(1994, 7, 13), is_alive=True, power=8))
        session.add(Wizards(name='Albus Dumbledore', side='white', birthday=datetime.date(1345, 8, 25), is_alive=True,power=10))
        session.add(Wizards(name='Neville Longbottom', side='white', birthday=datetime.date(1993, 4, 17), is_alive=True,power=3))
        session.add(Wizards(name='Malfoy Slizerin', side='dark', birthday=datetime.date(1995, 8, 21), is_alive=True, power=5))
        session.add(Wizards(name='Tom Riddle', side='dark', birthday=datetime.date(1973, 11, 13), is_alive=True, power=8))
        session.add(Wizards(name='Volan De Mort', side='dark', birthday=datetime.date(1973, 11, 13), is_alive=True, power=10))

        session.add(WizardsSlogans(hero_id=1, moto='I\'m Harry Potter!!!'))
        session.add(WizardsSlogans(hero_id=2, moto='Albus Dumbledore slogan 1'))
        session.add(WizardsSlogans(hero_id=3, moto='Why I\'m always in awkward situation?'))
        session.add(WizardsSlogans(hero_id=4, moto='Hey, Potter, you\'re stinky!'))
        session.add(WizardsSlogans(hero_id=5, moto='I can make you cry.'))
        session.add(WizardsSlogans(hero_id=6, moto='Die everyone!!!'))
        session.add(WizardsSlogans(hero_id=6, moto='I\'ll kill you!!!'))
        session.add(WizardsSlogans(hero_id=6, moto='Avada kedavra!!!'))
        session.add(WizardsSlogans(hero_id=1, moto='Harry Potter slogan 2'))
        session.add(WizardsSlogans(hero_id=2, moto='Albus Dumbledore slogan 2'))

        session.add(ShortStory(hero_id=1, story='Was born in London in 1994'))
        session.add(ShortStory(hero_id=2, story='The greatest wizard in the universal. Has infamous brother, Max'))
        session.add(ShortStory(hero_id=3, story='Always puts his foot in a trouble. Sometime he can make '))
        session.add(ShortStory(hero_id=4, story='Bad guy from Slizerin, hates Harry Potter'))
        session.add(ShortStory(hero_id=5, story='Young Volan De Mort. Nobody knew who he will become.'))
        session.add(ShortStory(hero_id=6, story='A bad genius, which threatens all the world.'))
        session.commit()
        print("Finished filling the database with initial values(wizards, slogans, stories).")


def print_db_statistics():
    print('Describe all wizards:')
    with Session() as session:
        for hero in session.query(Wizards).all():
            print(hero)
            print(f'Hero story is {hero.short_story}.')
            print(f'Hero has {len(hero.wizards_slogans)} slogans')
