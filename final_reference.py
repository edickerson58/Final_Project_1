import os.path
import csv


def find_file(file):
    if os.path.isfile(file):
        response = input('Overwrite existing file (y/n): ').strip().lower()
        while (response != 'y') and (response != 'n'):
            response = input('Enter y/n: ').strip().lower()
        if response == 'y':
            return 'overwrite'
        else:
            return 'new'
    else:
        return 'overwrite'


def main():
    try:
        file_name = input('Input file name: ').strip()
        with open(f'files/{file_name}', 'r'):
            pass
    except:
        print('File does not exist!')
        file_name = 'DNE'
    while file_name == 'DNE':
        try:
            file_name = input('Input file name: ').strip()
            with open(f'files/{file_name}'):
                pass
        except:
            print('File does not exist!')
            file_name = 'DNE'

    output_file = 'files/' + input('Output file name: ').strip()
    user_ans = find_file(output_file)
    if user_ans == 'new':
        output_file = 'files/' + input('New output file name: ').strip()

    header = ['Email', 'Subject', 'Confidence']
    data = []
    temp = []
    temp2 = [1, 1, 1]
    emails = []
    subjects = []
    confidences = []

    with open(f'files/{file_name}', 'r') as input_file:
        for line in input_file:
            if line.startswith('From: '):
                email = line.split()[1]
                temp.append(email)
            if line.startswith('Subject: '):
                subject = line.split()[4]
                temp.append(subject)
            if line.startswith('X-DSPAM-Confidence: '):
                confidence = line.split()[1]
                temp.append(confidence)

    for email in temp[::3]:
        emails.append(email)
    for subject in temp[1::3]:
        subjects.append(subject)
    for confidence in temp[2::3]:
        confidences.append(confidence)

    for i, email in enumerate(emails):
        temp2[0] = email
        temp2[1] = subjects[i]
        temp2[2] = confidences[i]
        data.append(temp2[:])

    with open(f'{output_file}', 'w', newline='') as file:
        writer = csv.writer(file, delimiter='-')
        writer.writerow(header)
        writer.writerows(data)
    print('Data stored!')


if __name__ == '__main__':
    main()
