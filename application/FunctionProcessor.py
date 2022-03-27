import argparse
import logging
import random
from datetime import datetime

from sqlalchemy import and_

from Classes import Wizards, WizardsSlogans, ShortStory, Session, WizardsClashes

parser = argparse.ArgumentParser()


# logging DEBUG into file log.txt
logging.basicConfig(filename='log.txt', level=logging.DEBUG, format='[%(levelname)s] %(asctime)s - %(message)s')
logger = logging.getLogger('wizard_processor_handler')
log_format = logging.Formatter('[%(levelname)s] %(asctime)s - %(message)s')


# logging INFO into file handler.txt
info_handler = logging.FileHandler('handler.txt')
info_handler.setFormatter(log_format)
info_handler.setLevel(logging.INFO)
logger.addHandler(info_handler)


# logging ERROR into console
error_handler = logging.StreamHandler()
error_handler.setFormatter(log_format)
error_handler.setLevel(logging.ERROR)
logger.addHandler(error_handler)


class MyFilter(logging.Filter):
    def filter(self, record):
        if 'draw' in record.msg:
            return False
        else:
            return True


logger.addFilter(MyFilter())


def valid_date(s):
    try:
        return datetime.strptime(s, "%Y-%m-%d")
    except ValueError:
        msg = "not a valid date: {0!r}".format(s)
        raise argparse.ArgumentTypeError(msg)


parser.add_argument('--function', help='Choose function')
parser.add_argument('--name', help='Name of wizard', required=False)
parser.add_argument('--side', help='Side of wizard', required=False)
parser.add_argument("--birthday", help="Birthday of wizard - format YYYY-MM-DD", required=False, type=valid_date)
parser.add_argument('--is_alive', help='Is wizard alive?', required=False)
parser.add_argument('--power', help='Power of wizard', required=False)
parser.add_argument('--story', help='Short story of wizard', required=False)
parser.add_argument('--slogan', help='Slogan of wizard', required=False)


args = parser.parse_args()


def add_wizard():
    print(f'Adding wizard {args.name}')
    with Session() as session:
        wizard_side = args.side
        if wizard_side not in ['dark', 'white']:
            raise Exception(f"Wizard side should be either 'dark' or 'white', you are adding {wizard_side}.")
        session.add(Wizards(name=args.name, side=wizard_side, birthday=args.birthday, is_alive=bool(args.is_alive), power=args.power))
        session.commit()
        logger.info(f'Wizard {args.name} was added successfully')


def delete_wizard():
    print(f'Deleting wizard {args.name}')
    with Session() as session:
        wizard_to_delete = session.query(Wizards).filter(Wizards.name == args.name).first()
        session.delete(wizard_to_delete)
        session.commit()
        logger.info(f'Wizard {args.name} was deleted successfully')


def add_story():
    print(f'Adding story for {args.name}')
    with Session() as session:
            wizard = session.query(Wizards).filter(Wizards.name == args.name).first()
            if wizard is not None:
                session.add(ShortStory(hero_id=wizard.id, story=args.story))
                session.commit()
                logger.info(f'{args.name}"s story was added successfully')
            else:
                logger.error(f'You are trying to add story to non-existing Wizard with name {args.name}')
                raise Exception(f'You are trying to add story to non-existing Wizard with name {args.name}')


def add_slogan():
    print(f'Adding slogan for {args.name}')
    with Session() as session:
            wizard = session.query(Wizards).filter(Wizards.name == args.name).first()
            if wizard is not None:
                number_of_story = session.query(WizardsSlogans).filter(WizardsSlogans.hero_id == wizard.id).count()
                session.add(WizardsSlogans(hero_id=wizard.id, moto_id = number_of_story+1,moto=args.slogan))
                session.commit()
                logger.info(f"{args.name}'s slogan was added successfully")
            else:
                logger.error(f'You are trying to add slogan to non-existing Wizard with name {args.name}')
                raise Exception(f'You are trying to add slogan to non-existing Wizard with name {args.name}')


def add_fight():
    print('Making up a fight!!!')
    with Session() as session:
        white_wizard = random.choice(session.query(Wizards).filter(and_(Wizards.side == 'white', Wizards.is_alive == True)).all())
        dark_wizard = random.choice(session.query(Wizards).filter(and_(Wizards.side == 'dark', Wizards.is_alive == True)).all())
        moto_white = random.choice(session.query(WizardsSlogans).filter(WizardsSlogans.hero_id == white_wizard.id).all())
        moto_dark = random.choice(session.query(WizardsSlogans).filter(WizardsSlogans.hero_id == dark_wizard.id).all())
        winner = 0
        if white_wizard.power > dark_wizard.power:
            winner = 1
            session.query(Wizards).filter(Wizards.id == dark_wizard.id).update({Wizards.is_alive: False})
            logger.info(f'Battle between {white_wizard.name} and {dark_wizard.name} was conducted successfully. {white_wizard.name} is a winner')
        elif white_wizard.power < dark_wizard.power:
            winner = 2
            session.query(Wizards).filter(Wizards.id == white_wizard.id).update({Wizards.is_alive: False})
            logger.info(f'Battle between {white_wizard.name} and {dark_wizard.name} was conducted successfully. {dark_wizard.name} is a winner')
        else:
            logger.error(f"Battle between {white_wizard.name} and {dark_wizard.name} was conducted successfully. It's a draw")
        session.add(WizardsClashes(hero_1_id=white_wizard.id, hero_2_id=dark_wizard.id,hero_1_moto_id=moto_white.moto_id,hero_2_moto_id=moto_dark.moto_id, winner=winner))
        session.commit()


# processing provided function name
function_name = args.function


if function_name == 'add_wizard':
    add_wizard()
elif function_name == 'delete_wizard':
    delete_wizard()
elif function_name == 'add_story':
    add_story()
elif function_name == 'add_slogan':
    add_slogan()
elif function_name == 'add_fight':
    add_fight()
else:
    logger.error('No such function')






