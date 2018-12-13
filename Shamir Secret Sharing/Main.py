import random


def generate_random_p(s, n):
    for p in range(1):
        if s > n:
            return random.randint(s, 1000)  #p>s, p>n
        else:
            return random.randint(n, 1000)


def generate_random_a(t):
    a_table = []
    for a in range(t-1):
        a_table.append(random.randint(19, 999))
    return a_table


def create_share(t, i, s, p, table):
    sum = 0
    for j in range(1,t):
        sum = sum + table[j-1]*i**j
    return (s+sum) % p


def create_shares(t, n, s, p, table):
    shares_value = []
    for i in range(1,n+1):
        shares_value.append(create_share(t, i, s, p, table))
        print('Wartości dla', i, 'udziału: (', i, ',', create_share(t, i, s, p, table), ')')
    return shares_value


def find_a_values(t, table):
    find_table = []
    for i in range(t-1):
        find_table.append(table[i])
    return find_table


def find_sum(t, n, table):
    check = []
    for j in range(1, n + 1):
        sum = 0
        for i in range(t-1):
            sum = sum + table[i]*j**(i+1)
        check.append(sum)
    return check


def find_secret(n, p, finded_sums, created_shares):
    s = []
    for i in range(n):
        s.append(((finded_sums[i] % p)-created_shares[i]))
    return s


def main():
    s = 954
    n = 4
    t = 3
    p = generate_random_p(s, n)
    table = generate_random_a(t)
    print('Wyrazy wolne a :', table)
    print('Wartość p :', p)
    created_shares = create_shares(t, n, s, p, table)

    print('Odnalezione wyrazy wolne a (sprawdzenie):', find_a_values(t, table))
    print('Odnalezione sumy bez modulo p i bez sekretu', find_sum(t, n, table))

    finded_sums = find_sum(t, n, table)

    print('Wartość sekretu uzyskana z wszystkich udziałów: ',find_secret(n, p, finded_sums, created_shares))


if __name__ == "__main__":
    main()