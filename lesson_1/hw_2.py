def time(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    secs = seconds - hours * 3600 - minutes * 60
    return f"Время {hours}:{minutes}:{secs}"

if __name__ == '__main__':
    seconds = int(input("Введите секунды "))
    print(time(seconds))