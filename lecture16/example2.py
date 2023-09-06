import threading
from random import randint

total_tickets = 100

mutex = threading.Lock()


def reserve_tickets(user_id, num_tickets):
    global total_tickets

    with mutex:
        if total_tickets >= num_tickets:
            total_tickets -= num_tickets
            print(f"Користувач {user_id} забронював {num_tickets} квитків.")
        else:
            print(f"Користувач {user_id} не вдалося забронювати квитки.")


def main():
    users = []
    for i in range(5):
        user = threading.Thread(target=reserve_tickets, args=(i, randint(20, 50)))
        users.append(user)
        user.start()

    for user in users:
        user.join()

    print(f'Total tickets = {total_tickets}')


if __name__ == "__main__":
    main()
