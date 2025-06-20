small_storage = {
    'гвозди': 5000,
    'шурупы': 3040,
    'саморезы': 2000
}

big_storage = {
    'доски': 1000,
    'балки': 150,
    'рейки': 600
}

big_storage.update(small_storage)
search = "залупы"
if search in big_storage:
    print(big_storage[search])
else:
    print("There is no this position")