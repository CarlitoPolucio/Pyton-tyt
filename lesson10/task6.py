def data(bit):
    errors = 0
    counter = 0
    slice_for_list = 0
    lost_pockets = 0
    output_list = []
    pockets = len(bit) // 4
    while counter != pockets:
        counter += 1
        if errors >= 2:
            lost_pockets += 1
            print("Too much errors", end="\n")
        errors = 0
        print(f"Pocket numba {counter}:", end="\n")
        check_list = bit_list[slice_for_list:slice_for_list + 4]
        for i, num in enumerate(bit_list[slice_for_list:slice_for_list + 4]):
            if not num in range(0, 2):
                errors += 1
                print(f"{i + 1} bit: {num}", end="\n")
                if errors >= 2:
                    check_list = []
            else:
                print(f"{i + 1} bit: {num}", end="\n")
        output_list += check_list
        slice_for_list += 4
    return output_list, f"lost pockets: {lost_pockets}, errors in massage: {errors}"


bit_list = [1, 0, -1, 1, -1, -1, 1, 1, 0, 1, -1, 1]

print(data(bit_list))








