

from faker import Faker

fake = Faker('en_AU')

def generate_medicare_number():
    return fake.random_number(digits=6, fix_len=True)

def generate_hpi_i_number():
    fake.random_number(digits=16, fix_len=True)
    
def generate_hpi_o_number():
    return fake.random_number(digits=16, fix_len=True)


def generate_IHI():
    return fake.random_number(digits=16, fix_len=True)

def generate_medicare_number():
    return fake.random_number(digits=10, fix_len=True)

def generate_dva():
    return fake.lexify(text="????????")

def generate_authoredOn():
    return f"{fake.date_between(start_date='-2y', end_date='today')}T{fake.time()}+00:00"

def generate_message_identifier():
    return f"AURF-{fake.random_number(digits=3, fix_len=True)}"

def generate_securemessage_endpoint():
    return fake.bothify(text='??#####')
