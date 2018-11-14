from selenium import webdriver
import argparse
import xlsxwriter

team1 = []
team2 = []

driver = webdriver.Chrome()

def Get_Team_Names(month, month_url):

    print("Month:   " + month)
    driver.implicitly_wait(30)
    driver.get(month_url)

    # output_file = open(month+".txt", "w")

    table_rows = driver.find_element_by_id("schedule").find_element_by_tag_name("tbody").find_elements_by_tag_name("tr")

    no = 0
    for row in table_rows:
        try:

            cells = row.find_elements_by_tag_name("td")
            tm1 = cells[1].find_element_by_tag_name("a").text
            tm2 = cells[3].find_element_by_tag_name("a").text

            team1.append(tm1)
            team2.append(tm2)
            no = no + 1
            # output_file.writelines("%4d. team1: %-40s team2: %s\n" % (no, tm1, tm2))
            print("%4d. team1: %-40s team2: %s" % (no, tm1, tm2))
        except:
            continue
            # print("error")

    # output_file.close()

def Get_Months(url):

    driver.implicitly_wait(3000)
    driver.get(url)

    months = []
    month_urls = []
    month_tags = driver.find_element_by_class_name("filter").find_elements_by_tag_name("a")
    for month_tag in month_tags:
        months.append(month_tag.text)
        month_urls.append(month_tag.get_attribute("href"))

    for i in range(len(months)):
        Get_Team_Names(months[i], month_urls[i])

    # driver.quit()

def Export_TO_EXCEL():
    # print('start')
    workbook = xlsxwriter.Workbook('teams.xlsx')
    worksheet = workbook.add_worksheet()

    worksheet.write_string(0, 0, "team1")
    worksheet.write_string(0, 1, "team2")

    for i in range(0, len(team1)):
        worksheet.write_string(i+1, 0, team1[i])
        worksheet.write_string(i+1, 1, team2[i])

    workbook.close()
    # print('end')

def getData(year):
    url = "https://www.basketball-reference.com/leagues/NBA_%d_games.html" % year
    # print(url)
    Get_Months(url)


parser = argparse.ArgumentParser(description='Input year value.')
parser.add_argument('years', metavar='From', type=int, nargs='+',
                    help='interger list')

years = parser.parse_args().years
if(len(years) == 1):
    getData(years[0])
elif (len(years) == 2):
    start = min(years)
    end = max(years)
    for year in range(start, end+1):
        getData(year)
else:
    years.sort()
    for year in years:
        getData(year)

driver.quit()

Export_TO_EXCEL()

