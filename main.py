from config import config
from src.utils import create_database, add_employers_to_database, add_vacancies_to_database
from src.external_api_hh import HeadHunterAPI
from src.db_manager import DBManager


def main():
    params = config()
    api_hh = HeadHunterAPI()
    data_emp = api_hh.get_data_employers()
    data_vac = api_hh.get_data_vacancies()
    create_database("search_vacancies", params)
    add_employers_to_database(data_emp, "search_vacancies", params)
    add_vacancies_to_database(data_vac, "search_vacancies", params)
    output = DBManager("search_vacancies", params)
    output.get_vacancies_with_keyword("ремонт")




if __name__ == "__main__":
    main()
