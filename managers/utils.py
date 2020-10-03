def swap(given_list, first_element, second_element):
    placeholder = given_list[first_element]
    given_list[first_element] = given_list[second_element]
    given_list[second_element] = placeholder
