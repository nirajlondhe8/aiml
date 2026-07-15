def main():
    my_list = [1, 2, 3]
    my_list[0] = 99
    print("list:", my_list)

    my_dict = {"a": 1}
    my_dict["a"] = 99
    print("dict:", my_dict)

    my_set = {1, 2, 3}
    my_set.add(4)
    print("set:", my_set)

    my_tuple = (1, 2, 3)
    print("tuple:", my_tuple)
    print("Tuples are immutable, so my_tuple[0] = 99 would raise TypeError.")

    tuple_with_list = ([1, 2], 3)
    tuple_with_list[0].append(99)
    print("tuple containing mutable list:", tuple_with_list)


if __name__ == "__main__":
    main()
