import random
random.seed(13)

profile_name_pool = ["Misha", "Vlad", "Masha", "Lera", "Grisha"]
profile_age_pool = ["18", "19", "100", "22"]
profile_sex_pool = ["male", "female", "other"]
profile_country_pool = ["russia", "usa", "uk", "germany"]
profile_city_pool = ["St. Petersburg", "Moscow", "The Great New City", "Boston", "Belin", "London"]
profile_about_pool = ["sdjkfsldnf", "12312hwbjefnds", "......."]
profile_goal_pool = ["work", "study", "science", "relationship", "friendship"]

area_of_interests_pool = {"sport": ["football", "basketball", "chess"], "computer games": ["dota 2", "CSGO"], "art": ["drawing", "poetry", "films"]}

university_pool = {"itmo": {"vt": ["pi", "ivt"], "kt": ["pmi", "is"]}, "bmstu": {"sm": ["sm5", "sm7"], "iu": ["iu2", "iu7"]}}

university_country_pool = ["russia", "usa"]
university_city_pool = ["St. Petersburg", "Moscow", "Boston"]
field_of_study_year_pool = [1, 2, 3, 4, 5]

image_path_pool = ["/to/smth", "/path/path/path"]
reaction_type_pool = ["like", "skip"]

def generate_user(count: int):
    s = "insert into service_user (created, active, reactions_from, reactions_to) values"
    for i in range(1, count+1):
        s += " (timestamp \'2023-12-19 23:12:54\', true, 0, 0),"
    return s[:-1] + ";"

def generate_profile(count: int):
    s = "insert into profile (user_id, name, age, sex, country, city, about, goal, modified) values"
    for i in range(1, count+1):
        s += str(" ({}, \'{}\', {}, \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', timestamp \'2023-12-19 23:12:54\'),").format(i, profile_name_pool[random.randint(0, len(profile_name_pool)-1)], profile_age_pool[random.randint(0, len(profile_age_pool)-1)], profile_sex_pool[random.randint(0, len(profile_sex_pool)-1)], profile_country_pool[random.randint(0, len(profile_country_pool)-1)], profile_city_pool[random.randint(0, len(profile_city_pool)-1)], profile_about_pool[random.randint(0, len(profile_about_pool)-1)], profile_goal_pool[random.randint(0, len(profile_goal_pool)-1)])
    return s[:-1] + ";"

def generate_image(profiles_count: int, count: int):
    s = "insert into image (profile_id, file_path, uploaded) values"
    for i in range(1, count+1):
        s += str(" ({}, \'{}\', timestamp \'2023-12-19 23:12:54\'),").format(random.randint(1, profiles_count), image_path_pool[random.randint(0, len(image_path_pool)-1)])
    return s[:-1] + ";"

def generate_reaction(users_count: int, count: int):
    s = "insert into reaction (from_id, to_id, type, at) values"
    for i in range(1, count+1):
        fromm = 0
        to = 0
        while (fromm == to):
            fromm = random.randint(1, users_count)
            to = random.randint(1, users_count)
        s += str(" ({}, {}, \'{}\', timestamp \'2023-12-19 23:12:54\'),").format(fromm, to, reaction_type_pool[random.randint(0, len(reaction_type_pool)-1)])
    return s[:-1] + ";"

def generate_interest():

    area_s = "insert into area_of_interest (name) values"
    area_n = 1
    interest_s = "insert into interest (area_id, name, created) values"
    for i in area_of_interests_pool.keys():
        area_s += str(" (\'{}\'),").format(i)
        for j in area_of_interests_pool[i]:
            interest_s += str(" ({}, \'{}\', timestamp \'2023-12-19 23:12:54\'),").format(area_n, j)
        area_n += 1
    return area_s[:-1] + ";\n" + interest_s[:-1] + ";"

def generate_profile_interest_relation(profiles_count: int, interests_count: int, count: int):
    s = "insert into profile_interest_relation (profile_id, interest_id) values"
    was = set()
    for i in range(1, count+1):
        profile = 1
        interest = 1
        while ((profile, interest) in was):
            profile = random.randint(1, profiles_count)
            interest = random.randint(1, interests_count)
        was.add((profile, interest))
        s += str(" ({}, {}),").format(profile, interest)
    return s[:-1] + ";"

def generate_field_of_study(profiles_count: int):
    university_s = "insert into university (name, country, city) values"
    university_n = 1
    faculty_s = "insert into faculty (university_id, name) values"
    faculty_n = 1
    field_s = "insert into field_of_study (faculty_id, profile_id, name, year) values"
    for i in university_pool.keys():
        university_s += str(" (\'{}\', \'{}\', \'{}\'),").format(i, university_country_pool[random.randint(0, len(university_country_pool)-1)], university_city_pool[random.randint(0, len(university_city_pool)-1)])
        for j in university_pool[i].keys():
            faculty_s += str(" ({}, \'{}\'),").format(university_n, j)
            for k in university_pool[i][j]:
                field_s += str(" ({}, {}, \'{}\', {}),").format(faculty_n, random.randint(1, profiles_count), k, field_of_study_year_pool[random.randint(0, len(field_of_study_year_pool)-1)])
            faculty_n += 1
        university_n += 1
    return university_s[:-1] + ";\n" + faculty_s[:-1] + ";\n" + field_s[:-1] + ";"


users_count = 5
images_count = 10
reactions_count = 10
interests_count = 0
for i in area_of_interests_pool.values():
    interests_count += len(i)
profile_interest_relations_count = 10

f = open("dml", "w+")
f.write(generate_user(users_count) + "\n")
f.write(generate_profile(users_count) + "\n")
f.write(generate_image(users_count, images_count) + "\n")
f.write(generate_reaction(users_count, reactions_count) + "\n")
f.write(generate_interest() + "\n")
f.write(generate_profile_interest_relation(users_count, interests_count, profile_interest_relations_count) + "\n")
f.write(generate_field_of_study(users_count))
f.close()
