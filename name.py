from slugify import slugify
import click
import csv
import json

def load_names(filename, genitives):
    """
    Load approved names into male and female lists
    and find their genitive form while it's at it.
    """
    male_names = []
    female_names = []
    with open(filename) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            # Approved names have Afgreitt == Sam
            if row['Afgreitt'] == 'Sam':
                # Female names are 'ST'
                if row['Tegund'] == 'ST':
                    female_names.append({ 
                        'slug': slugify(row['Nafn']),
                        'name': row['Nafn'],
                        'genitive': genitives.get(row['Nafn'],
                                                  row['Nafn'])
                    })
                # Male names are 'DR'
                elif row['Tegund'] == 'DR':
                    male_names.append({ 
                        'slug': slugify(row['Nafn']),
                        'name': row['Nafn'],
                        'genitive':genitives.get(row['Nafn'], None)
                    })
    return (female_names, male_names)

def load_genitives(filename):
    """
    Load genitives from the Database of Modern Icelandic Inflection's CSV dump
    """
    genitives = {}
    with open(filename) as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        for row in reader:
            # People names in Iceland are tagged 'ism' and genitive is 'EFET'
            if row[3] == 'ism' and row[5] == 'EFET':
                genitives[row[0]] = row[4]
    return genitives

def load_homemade(filename):
    """
    Of course the Database of Modern Icelandic Inflection isn't up to date
    so to add missing names we need a homemade inflection csv file
    (placed in the data/ folder for everyone to use)
    """
    genitives = {}
    with open(filename) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            # Column 0 is just the gender to help find the right genitive form
            # while filling it in manually
            genitives[row[1]] = row[2]
    return genitives


@click.command()
@click.option('-d', '--dmii', help='CSV file for the DMII in Sigrunarsnid')
@click.option('-h', '--homemade-dmii',
              help='CSV file with additional genitives (homemade)')
@click.option('-n', '--names', help='CSV file with Icelandic names')
@click.option('-o', '--output', help='Output json file')
def generate_json_file(dmii, homemade_dmii, names, output):
    genitives = load_genitives(dmii)
    homemade = load_homemade(homemade_dmii)
    genitives.update(homemade)
    (female, male) = load_names(names, genitives)

    with open(output, 'w') as json_file:
        json.dump({'female': female, 'male':male}, json_file)

if __name__ == '__main__':
    generate_json_file()
