import os
from dotenv import load_dotenv

load_dotenv()
# intent mapping
# >>>>> !!! DON'T CHANGE THE KEYS OF THE INTENT_MAP !!! <<<<<
# >>>>> !!! KEEP ALL ELEMENTS OF THE VALUE LISTS IN LOWER CASE !!! <<<<<
INTENT_MAP = {
    'GREETING': {'greeting', 'greetings', 'hi', 'hello', 'hey', 'good morning', 'good afternoon', 'good evening'},
    'ADD': {'add', 'create', 'insert', 'include', 'put', 'define', 'register', 'record'},
    'UPDATE': {'update', 'change', 'modify', 'alter', 'edit', 'correct', 'revise', 'replace', 'renew', 'redefine',
               'set', 'updating', 'changing', 'modifying', 'altering', 'editing', 'correcting', 'revising', 'replacing',
               'setting'},
    'READ': {'read', 'show', 'list', 'search', 'find', 'select', 'get', 'retrieve', 'fetch', 'view', 'give', 'display'},
    'DELETE': {'delete', 'remove', 'destroy', 'del', 'erase', 'kill'},
    'CANCELLATION': {'cancellation', 'cancel', 'stop', 'quit', 'exit'},
    'CONFIRMATION': {'confirmation', 'confirm', 'ok', 'yes'},
    'HELP': {'help', 'know'},
    'GOODBYE': {'bye', 'goodbye'},
    'MEANINGLESS': {'unknown', 'unintelligible', 'unrecognized', 'meaningless', 'uninterpretable'}
}

USELESS_EXPRESSIONS_FOR_INTENT_DISCOVERY = ['please', 'i want to', 'i want', 'could you', 'can you']

WHERE_CLAUSE_WORDS = {'where', 'which', 'that', 'whose', 'whom', 'who', 'what', 'when', 'for'}

# bot msgs
MISUNDERSTANDING = [
    "Um. I don't recognize it. Which operation do you want to do? Add, update, delete or get some information?\n(say 'help' for samples)",
    "Sorry, but I didn't get it. Try something like <b><i>register new student with name 'Joseph'</i></b> or <b><i>get all students with gender 'Male'</i></b>\n(say 'help' for more samples)",
    "Please, repeat in another way, because I didn't get it. (say 'help' for more info)"
]

GREETINGS = ["Hi! You can say something like <b><i>Add student with name 'Anderson'</i></b>",
             "Hello! Please say something like <b><i>Add student with name 'Anderson'</i></b>",
             "Hello! Good see you here! Please say some data operation like <b><i>Include student with name 'Anderson', email 'andersonmg@gmail.com'</i></b>"
             ]

BYE = ["Ok! Thank you. See you next time!",
       "Thank you so much. I stand at your disposal.",
       "Thank you! If you need add some info, please text me."
       ]

HELP = ["I'm a bot that helps you add your information in an organized, secure, and flexible way. Say what you want to add, update, delete or only get info. \n\nFor example, say something like: \n<b>Add operation:</b> <i>add a class with name 'Self-Adaptive Systems'</i> \n<b>Get operation:</b> <i>view classes</i> \n<b>Delete operation:</b> <i>delete class with name 'Java'</i> \n<b>Update operation:</b> <i>update class where name is 'Java', setting year '2024'</i> \n<b>Average operation:</b> <i>Get average class year</i> \n<b>Sum operation: </b> <i>Get sum of class year</i>\n<b>Analytics operation:</b> <i>Get greatest year from class</i> or <i>Get lowest year from class</i>",
        "I'm a bot that allows you to add your information using natural language. Like a traditional system, but more accessible and flexible.\n\nFor instance, to register a student, say to: \n<b>Add:</b> <i>add student with gender 'Female', name 'Mary', email 'mary@school.com'</i> \n<b>Delete:</b> <i>delete student where name is 'Mary'</i> \n<b>Read:</b> <i>get students with gender 'Female'</i> \n<b>Update:</b> <i>update student where name is 'Mary', setting age '21'</i> \n<b>Analytics:</b> <i>get mean students age</i> or <i>get highest age from students</i> or <i>get sum of students age</i>",
        "I'm your bot that securely saves your information. I understand better direct sentences.\nThus let me know first what you want to do (add, read, delete or update some data), what type the information you want to operate (a student, a class, a class registration, etc.), and, finally, the data itself. \n\nSome examples:\n<b><i>- Add a teacher with name 'Paulo Henrique', gender 'Male'\n- Delete a student with name 'Anderson'\n- Get the class with name 'Python'\n- Get average students grade\n- Get maximum cost from expense\n- Get lowest weight from cats\n- Get sum of expense cost</i></b>"
        ]

CANCEL = ['No problem! The operation was canceled successfully.']

CANCEL_WITHOUT_PENDING_INTENT = ['There is no operation to cancel.']

CONFIRMATION_WITHOUT_PENDING_INTENT = ['There is no operation to confirm.']

ASK_CONFIRM = ['OK to confirm current operation;\nCANCEL to cancel. ;)]',
               "[Any time you can say 'ok' to confirm the operation, or 'cancel' to cancel the current operation]"]

ATTRIBUTE_FORMAT = [
    "I'll understand better if the data is in the following format:\n 'data_name'  'data_value''.\nObserve the examples:\n- <b><i>add student with name 'Anderson', and age '21'</i></b>\n- <b><i>update the student with name 'Anderson', setting the age '21'</i></b>\n- <b><i>delete the student with name 'Anderson'</i></b>\n- <b><i>get the student with name 'Anderson'</i></b>"
]

ATTRIBUTE_OK = lambda opr, clas, att, where: [
                                              f"Ok! I got it!\nWe are going to <b>{opr}</b> a <b>"
                                              f"{clas.replace('_', ' ').title()}</b>."
                                              + (f"\nWith <b>{', '.join([f'{key}: <i>{value}</i>' for key, value in att.items()])}</b>." if att else "")
                                              + (f"\nOnly when <b>{', '.join([f'{key}: <i>{value}</i>' for key, value in where.items()])}</b>." if where else "")
                                              + f"\nSay <b>OK</b> to confirm or <b>CANCEL</b> to"
                                              f" cancel this operation."]

SAVE_SUCCESS = ['Ok! Information saved successfully!',
                'It done! Information saved. ;)',
                "Yes! All done. We've saved your data with security."]

DELETE_SUCCESS = lambda n_del: [f"Ok! <b>{n_del}</b> registers deleted.",
                                f"Done! <b>{n_del}</b> deleted.",
                                f"<b>{n_del}</b> registers deleted successfully."
                                ]

DELETE_FAILURE = ['Nothing to delete. Please, try again.']

ANALYTICS = [['average', 'mean', 'middle', 'mid'],['highest', 'greatest', 'largest', 'maximum', 'biggest', 'most'], ['lowest', 'minimum', 'smallest', 'least'], ['sum', 'total', 'amount']]

AVERAGE = lambda average, words: [f"Alright, here is the result!\n" +
                                f"<b>{words[1].title()} {words[2]} {words[3]} = {average}</b>"]
HIGHEST = lambda highest, words: [f"Alright here is the result!\n" +
                                f"<b>{words[1].title()} {words[4]} {words[2]} = {highest}</b>"]
LOWEST = lambda lowest, words: [f"Alright here is the result!\n" +
                              f"<b>{words[1].title()} {words[4]} {words[2]} = {lowest}</b>"]

SUM = lambda sum, words: [f"Alright here is the result!\n" +
                          f"<b>{words[1].title()} of {words[3]} {words[4]} = {sum}</b>"]

NO_REGISTERS = ['There are no info to show.']

LIMIT_REGISTERS = 10  # limit of registers to show

LIMIT_REGISTERS_MSG = "A maximum of <b>" + str(LIMIT_REGISTERS) + \
                      "</b>  registers are shown, ordered by the newest updated ones." \
                      "\nApply filters to a more accurate search."

CLASS_NOT_IN_DOMAIN = lambda clas: [f"There is no information about <b>'{clas}'</b> saved. \nPlease, try something else."]

MISSING_CLASS = [
    "Would you please inform me of the information type that you want to operate? For instance, if you are trying to add data about a student, say <i>add student with name=\'Anderson\'</i>.\n(If you wish to cancel this operation, say <b>CANCEL</b>.)"]

MULTIPLE_CLASSES = ['Please, try to inform the information type with only one word, ok?']

GENERAL_FAILURE = 'Sorry, but I could not complete the operation. Please, try again using other words.\n(say <b>HELP</b> for examples)'

# config variables
MANAGED_SYSTEM_NAME = 'managedsys'
SUFFIX_ENV = '_env'
SUFFIX_CONFIG = '_config'
SUFFIX_WEB = '_web'
WEBAPP_HOME_URL = 'http://localhost/admin'

PNL_GENERAL_THRESHOLD = 0.75

TIMEOUT_MSG_PARSER = 30  # seconds
TIMEOUT_MSG_PARSER = 999999

# limit of chars to show in a get message for each attribute
LENGTH_LIMIT_CHARS_TO_SHOW_IN_ROWS = 120

# size limit for user msg
MAX_USER_MSG_SIZE = 300
MAX_USER_MSG_SIZE_MSG = ["The message is too long. DoME is an experiment with academic purposes. Please, try to send it in a smaller version. Current limit in chars is " + str(MAX_USER_MSG_SIZE) + "."]

# max request per second per user
MAX_REQUESTS_PER_SECOND = 0.75
DDoS_MSG = "Sorry, but you are sending too many requests per second, and you'll receive a block penalty. This is an academic experiment, and that rule is to prevent malicious attacks.\nPlease, try again in a few minutes sending the messages at an average human pace."
DDoS_PENALTY = 60  # seconds

# production variables
RUN_WEB_SERVER = True
USE_PARSER_CACHE = False
DEBUG_MODE = False
PRINT_DEBUG_MSGS = True

if "DOME_DEBUG_MODE" in os.environ:
    DEBUG_MODE = eval(os.environ['DOME_DEBUG_MODE'])

if DEBUG_MODE:
    TIMEOUT_MSG_PARSER = 999999
    USE_PARSER_CACHE = False

# django default user
DJANGO_SUPERUSER_DEFAULT_USERNAME = 'admin'
DJANGO_SUPERUSER_DEFAULT_PASSWORD = 'admin'
DJANGO_SUPERUSER_DEFAULT_EMAIL = 'admin@t2s.org'

# Hugging Face token
HUGGINGFACE_TOKEN = os.environ['HUGGINGFACE_TOKEN']

# managed system webapp custom variables
MANAGED_SYSTEM_WEBAPP_TITLE = 'Managed System Webapp'
NUMBER_MAX_FIELDS_IN_MODELS_TO_STR_FUNCTION = 3

MANAGED_SYSTEM_WEBAPP_BASE_URL = 'http://dome-uece.duckdns.org'
if DEBUG_MODE:
    MANAGED_SYSTEM_WEBAPP_BASE_URL = 'http://127.0.0.1'

MANAGED_SYSTEM_WEBAPP_BASE_URL += '/admin/managedsys_web'