import random

def generate_no_rekening() -> str:
    #Generate Rekening 10 angka Random
    # Bagian tetap dari no_rekening
    pref = "00920240"
    random_prof = ''.join([str(random.randint(0, 9)) for _ in range(3)]) 
    no_rekening = pref + random_prof
    return no_rekening
