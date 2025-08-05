def mean(list_args: list) -> float:
    """Returns the mean of the values in received list"""
    return sum(list_args)/len(list_args)


def median(list_args: list) -> float:
    """Returns the median of the values in received list"""
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
    """Takes a list of int and returns its 25% quartile"""
    median_value = median(list_args)
    # print("inside quartile1_4, median_value :", median_value)
    new_list = [x for x in list_args if x <= median_value]
    # print("inside quartile1_4, new_list :", new_list)
    quartile1_4 = median(new_list)
    # print("inside quartile1_4, quartile1_4 :", quartile1_4)
    return quartile1_4


def quartile3_4(list_args: list) -> float:
    """Takes a list of int and returns its 75% quartile"""
    median_value = median(list_args)
    # print("inside quartile3_4, median_value :", median_value)
    new_list = [x for x in list_args if x >= median_value]
    # print("inside quartile3_4, new_list :", new_list)
    quartile3_4 = median(new_list)
    # print("inside quartile3_4, quartile3_4 :", quartile3_4)
    return quartile3_4


def quartile(list_args: list) -> float:
    """Takes a list of int and returns a list of quartiles"""
    list_args = sorted(list_args)
    new_list = []
    new_list.append(quartile1_4(list_args))
    new_list.append(quartile3_4(list_args))
    new_list = [float(x) for x in new_list]
    return new_list


def variance(list_args: list) -> float:
    """Takes a list and returns its variance"""
    n = len(list_args)
    mean_val = mean(list_args)
    # print(mean_val)
    diff = [(x - mean_val)**2 for x in list_args]
    # print(diff)
    sum_diff = sum(diff)
    # print(sum_diff)
    variance_val = sum_diff/n
    # print(variance_val)
    return variance_val


def std_deviation(list_args: list) -> float:
    """Takes a list and returns its deviation"""
    return variance(list_args)**0.5


def comment_deviation(list_args: list) -> None:
    """Indicates whether the dataset's standard deviation
is large or small"""
    mean_val = mean(list_args)
    deviation = std_deviation(list_args)
    print("   < 5% difference from mean is considered as small")
    print("   < 15% difference from mean is considered as moderage")
    print("   >= 15% difference from mean is considered as large")
    print(f"   Mean: {mean_val:.4f} | < 5%: {mean_val * 0.05:.4f} | "
          f"< 15%: {mean_val * 0.15:.4f}")
    if deviation <= mean_val * 0.05:
        print("   ⬇️  Deviation of the dataset is small")
    elif deviation <= mean_val * 0.15:
        print("   ⏺️  Deviation of the dataset is moderate")
    else:
        print("   ⬆️  Deviation of the dataset is large")


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
            # comment_deviation(list_args)
        if "var" in dict_kwargs.values():
            print("var :", variance(list_args))
