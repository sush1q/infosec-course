import dns.resolver
from dask import delayed, compute
from dask.distributed import Client


def check_email_domain(email: str) -> bool:
    """
    Проверяет, существует ли домен email и имеет ли он MX-записи.
    """
    try:
        domain = email.split('@')[-1]
        # Проверка MX-записей
        mx_records = dns.resolver.resolve(domain, 'MX')
        return bool(mx_records)
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.Timeout):
        return False



def validate_emails(emails: list[str]) -> list[bool]:
    """
    Параллельная проверка списка email-адресов с использованием Dask.
    """
    # Создаем отложенные задачи для каждого email
    tasks = [delayed(check_email_domain)(email) for email in emails]
    # Запускаем вычисления
    results = compute(*tasks)
    return results


if __name__ == "__main__":
    res = validate_emails(["pavelsirotkin17@yandex.ru"])
    print(res)