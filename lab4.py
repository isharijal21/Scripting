#!/usr/bin/python3
import csv

filename = "employee_logins .csv"  
#this shows the max amount of login attempts the employees can do 
max_login = 199


def file_reader() -> tuple:  # return type to tuple since two lists are returned
    bad_lst = []
    good_lst = []
    with open(filename, "r") as file_pointer:
        fileRows = csv.reader(file_pointer)
        #avoids the header count
        header = next(file_pointer)
        for row in fileRows:
            if int(row[3]) > max_login or "e" in row[1] or "l" in row[1]:  
                # splits the ip_adress and only takes in the first_ip_adress into account 
                ip_addresses = row[4].split(";") 
                first_ip_address = ip_addresses[0]
                newRow = [row[0].capitalize() + " " + row[1].capitalize(), first_ip_address, row[3], (int(row[3]) - max_login)]  
                bad_lst.append(newRow)
            else:
                newRow = [row[0] + " " + row[1], row[3]]  
                good_lst.append(newRow)
    #closes the file 
    file_pointer.close()
    return bad_lst, good_lst


def create_new(bad_list, good_list):  
    fields = ["Employee Name", "IP Address", "Login Count", "Login Count Excess"]  
    newFile = "rijali1.csv"
    with open(newFile, "w", newline='') as newcsvFile: 
        csvwriter = csv.writer(newcsvFile)
        csvwriter.writerow(fields)
        csvwriter.writerows(bad_list)
        print("'Suspicious_Employee', File Created: Printing info to the console:......")
        print("%-25s %-15s" % (fields[0], fields[1]))
        print("%-25s %-15s" % ('--------', '--------'))
        for person in bad_list:
            #prints out the output in the order the question wants us to 
            print("%-25s %-15s" % (person[0], person[2]))  
        print("%-25s %-15s" % ('--------', '--------'))
        total = len(bad_list)
        goodEmps = len(good_list)
        print("Total number of suspicious employees with suspicious login attempts: %s" % total)
        print("Total number of less suspicious employees: %s" % goodEmps)
    newcsvFile.close()


def main():
    bad_lst = []
    #list that stores info of the suspicious employees 
    good_lst = []
    #list that stores info of the non suspicious employees 
    bad_lst, good_lst = file_reader()
    create_new(bad_lst, good_lst)


if __name__ == "__main__":
    main()
