import datetime


class BankAccount:
    def __init__(self, account_id, initial_balance):
        self.account_id = account_id
        self.balance = initial_balance
        self.is_closed = False

    def deposit(self, amount):
        # TODO: Add the amount to the balance
        self.balance += amount

    def withdraw(self, amount):
        # TODO: Check if the balance is sufficient and subtract the amount
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient balance")

    def apply_interest(self):
        # TODO: Add 1% interest to the balance (truncate to integer)
        self.balance += int(self.balance * 0.01)

    def close(self):
        # TODO: Mark the account as closed
        self.is_closed = True

    def is_active(self):
        # TODO: Return whether the account is still active
        return not self.is_closed

    def get_balance(self):
        # TODO: Return the current balance
        return self.balance


def acct_validation(action, acct_id, rest, accounts_dict):
    if action == "OPEN":
        if acct_id in accounts_dict and accounts_dict[acct_id].is_active():
            raise ValueError("Account ID already exists")
    elif action in ["DEPOSIT", "WITHDRAW", "BALANCE", "CLOSE"]:
        if acct_id not in accounts_dict or not accounts_dict[acct_id].is_active():
            raise ValueError("Account not found")
    elif action == "TRANSFER":
        if acct_id not in accounts_dict or not accounts_dict[acct_id].is_active():
            raise ValueError("Account not found")
        if rest[0] not in accounts_dict or not accounts_dict[rest[0]].is_active():
            raise ValueError("Account not found")

    return True


def process_operations(operation_queue):
    current_date = datetime.datetime.strptime(operation_queue[0][0], "%Y-%m-%d").date()
    accounts_dict = {}
    for op in operation_queue:
        # op = [date, operation type, account ID,  account ID or amount, None or amount]
        date, action, acct_id, *rest = op

        try:
            if action not in ["BALANCE", "CLOSE"]:
                if rest[len(rest) - 1].isdigit():
                    amount = int(rest[len(rest) - 1])
                else:
                    raise ValueError("Invalid transaction amount")

            d2 = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            count_1sts = 0
            current = current_date + datetime.timedelta(days=1)
            while current <= d2:
                if current.day == 1:
                    count_1sts += 1
                current += datetime.timedelta(days=1)

            for _ in range(count_1sts):
                for account in accounts_dict.values():
                    if account.is_active():
                        account.apply_interest()

            current_date = d2

            if acct_validation(action, acct_id, rest, accounts_dict):
                match action:
                    case "OPEN":
                        accounts_dict[acct_id] = BankAccount(acct_id, amount)
                    case "DEPOSIT":
                        accounts_dict[acct_id].deposit(amount)
                    case "WITHDRAW":
                        accounts_dict[acct_id].withdraw(amount)
                    case "BALANCE":
                        print(acct_id, accounts_dict[acct_id].get_balance())
                    case "TRANSFER":
                        accounts_dict[acct_id].withdraw(amount)
                        accounts_dict[rest[0]].deposit(amount)
                    case "CLOSE":
                        accounts_dict[acct_id].close()

        except ValueError as e:
            print(e)

    return accounts_dict


if __name__ == "__main__":
    operation_queue = []
    accounts = []

    while True:
        operation = input()
        if operation == "q":
            break
        operation_queue.append(operation.strip().split())

    # Sort and then process all operations
    operation_queue.sort(key=lambda x: x[0])
    accounts_dict = process_operations(operation_queue)
