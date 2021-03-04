from typing import Optional, List, Any


def number_length(num: int) -> int:
    num = str(num)

    return len(num)


def list_of_multiples(num: int, length: Optional[int]) -> List[int]:
    for n in range(length):
        num *= 2

    return num


def normalize(input_str) -> str:
    #for n in range(input_str):
        #if input_str.upper == input_str:
    pass


def cat_dog(num: int) -> str:
    if num % 3 == 0 and num % 5 != 0:
        print("Cat")
    elif num % 5 == 0 and num % 3 != 0:
        print("Dog")
    elif num % 5 == 0 and num % 3 == 0:
        print('CatDog')
    else:
        print(str(num))