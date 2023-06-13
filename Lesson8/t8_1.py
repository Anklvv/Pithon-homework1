from os import path

all_data = []
last_id = 0
file_base = base.txt

if not path.exists(file_base):
       with open(file_base, "w", encoding="utf-8") as f:
              pass
              


def read_records():
        global all_data, last_id

        with open(file_base, encoding="utf-8") as f: 
                all_data = [i.strip() for i in f ]
                last_id = int(all_data[-1].split()[0])
        return all_data


# def show_all():
#         print(*all_data)


def main_menu():
    play = True
    while play:
        answer = input("Phone book:\n")
        "1. Show all records\n"
        "2. Add a record\n"
        "3. Search a  record\n"
        "4. Change \n"
        "5. Delete \n"
        "6. Imr\Exp \n"
        "7. Exit \n"
        match answer:
                case "1":
                    print(read_records())
                case "2":
                        pass
                case "3":
                        pass
                case "4":
                        pass
                case "5":
                        pass
                case "6":
                        pass
                case "7":
                        pass
         
        
        
