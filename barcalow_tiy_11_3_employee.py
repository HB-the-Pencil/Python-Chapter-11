class Employee:
    """Model an employee at a company."""
    def __init__(self, first: str, last: str, salary):
        """
        Create an employee instance with name and salary.

        :param first: Employee first name.
        :param last: Employee last name.
        :param salary: Employee salary.
        """
        self.first_name = first
        self.last_name = last
        self.salary = salary

    def give_raise(self, amount=5000):
        """
        Raise an employee's salary.

        :param amount: Amount to increase salary by (default 5000).

        :return: Increases salary.
        """
        self.salary += amount