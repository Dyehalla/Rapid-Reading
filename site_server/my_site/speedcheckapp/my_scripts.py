from random import choice


def random_text(nums_list_str: str) -> dict:
    nums_list = nums_list_str.split('/')
    data = dict()
    i = choice(nums_list)
    my_text = ['Text 1.txt', 'Text 2.txt', 'Text 3.txt', 'Text 4.txt', 'Text 5.txt', 'Text 6.txt', 'Text 7.txt', 'Text 8.txt'][int(i) - 1]
    text_file = open(f'..\\texts\\' + my_text)
    data['text'] = text_file.readlines()

    length = 0
    for line in data['text']:
        length += len(line.split())

    nums_list.remove(i)
    if len(nums_list) == 0:
        data['new_read_list'] = '1/2/3/4/5/6/7/8'
    else:
        data['new_read_list'] = '/'.join(nums_list)

    data['length'] = length
    data['number'] = i
    data['title'] = my_text.removesuffix('.txt')

    text_file.close()
    return data


def time_converter(time_string: str, words: int):
    if time_string == '0':
        return ['???', 0, 0]
    if len(time_string) == 1:
        seconds = int(time_string[0])
        minutes = 0
    else:
        seconds = int(time_string[-2] + time_string[-1])
        if len(time_string) > 2:
            if len(time_string) == 3:
                minutes = int(time_string[0])
            else:
                minutes = int(time_string[0] + time_string[1])
        else:
            minutes = 0

    speed = words / (minutes + seconds / 60)

    return [speed, minutes, seconds]