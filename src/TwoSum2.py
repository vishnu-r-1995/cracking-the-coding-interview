class TwoSum2(object):
    def twoSum(self, numbers, target):
        left_pointer = 0
        right_pointer = 1
        numbers_map = {}
        while (left_pointer < len(numbers) and right_pointer < len(numbers)):
            left_number = numbers[left_pointer]
            right_number = numbers[right_pointer]
            if (left_number + right_number == target):
                return [left_pointer + 1, right_pointer + 1]
            if (left_number in numbers_map.keys() and right_number in numbers_map.keys()):
                left_pointer += 1
                right_pointer += 1
                continue
            numbers_map[left_number] = left_pointer
            temp_list = [x + right_number for x in numbers_map.keys()]
            if (max(temp_list) >= target):
                for i, x in enumerate(temp_list):
                    if (x == target):
                        return [numbers_map.get(x - right_number) + 1, right_pointer + 1]
            left_pointer += 1
            right_pointer += 1
        return [0,0]