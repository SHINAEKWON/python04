def mean(list_args: list) -> float:
    return sum(list_args)/len(list_args)


def median(list_args: list) -> float:
    list_args = sorted(list_args)
    n = len(list_args)
    mid = n // 2

    if n % 2 == 1:
        return list_args[mid]
    else:
        first = list_args[mid - 1]
        # print(first)
        second = list_args[mid]
        # print(second)
        mean_for_median = (first + second) / 2
        return mean_for_median


def quartile1_4(list_args: list) -> float:
    median_value = median(list_args)
    # print("inside quartile1_4, median_value :", median_value)
    new_list = [x for x in list_args if x <= median_value]
    # print("inside quartile1_4, new_list :", new_list)
    quartile1_4 = median(new_list)
    # print("inside quartile1_4, quartile1_4 :", quartile1_4)
    return quartile1_4


def quartile3_4(list_args: list) -> float:
    median_value = median(list_args)
    # print("inside quartile3_4, median_value :", median_value)
    new_list = [x for x in list_args if x >= median_value]
    # print("inside quartile3_4, new_list :", new_list)
    quartile3_4 = median(new_list)
    # print("inside quartile3_4, quartile3_4 :", quartile3_4)
    return quartile3_4


def quartile(list_args: list) -> float:
    list_args = sorted(list_args)
    new_list = []
    new_list.append(quartile1_4(list_args))
    new_list.append(quartile3_4(list_args))
    new_list = [float(x) for x in new_list]
    return new_list


def variation(list_args: list) -> float:
    n = len(list_args)
    mean_val = mean(list_args)
    # print(mean_val)
    diff = [(x - mean_val)**2 for x in list_args]
    # print(diff)
    sum_diff = sum(diff)
    # print(sum_diff)
    variation_val = sum_diff/n
    # print(variation_val)
    return variation_val


def std_deviation(list_args: list) -> float:
    return variation(list_args)**0.5


def ft_statistics(*args: any, **kwargs: any) -> None:
    list_args = tuple(args)
    dict_kwargs = dict(**kwargs)

    if not list_args:
        print("ERROR\nERROR\nERROR")
    elif not dict_kwargs:
        return
    else:
        if "mean" in dict_kwargs.values():
            print("mean :", mean(list_args))
        if "median" in dict_kwargs.values():
            print("median :", median(list_args))
        if "quartile" in dict_kwargs.values():
            print("quartile :", quartile(list_args))
        if "std" in dict_kwargs.values():
            print("std :", std_deviation(list_args))
        if "var" in dict_kwargs.values():
            print("var :", variation(list_args))
