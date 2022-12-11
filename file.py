def save_to_file(file_name, jobs):
    file = open(f'{keyword}.csv', 'w', encoding='cp949')
    file.write("Company, Position, Location, URL\n")

    for job in jobs:
        file.write(
            f'{job["company"]},{job["position"]},{job["location"]},{job["link"]}\n'
        )
    file.close()
